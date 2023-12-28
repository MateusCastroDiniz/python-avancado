import requests
import time
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

MAX_THREADS = 80


def extract_movie_details(movie_link):
    time.sleep(random.uniform(0, 0.2))
    response = BeautifulSoup(requests.get(movie_link, headers=headers).content, 'html.parser')
    movie_soup = response

    if movie_soup is not None:
        title = None
        date = None

        movie_data= movie_soup.find('div', attrs={'class': 'sc-e226b0e3-3 dwkouE'})
        if movie_data is not None:
            title = movie_data.find('h1').get_text()
            date = movie_data.find('a', attrs={'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).get_text().strip()

        rating = movie_soup.find('span', attrs={'class': 'sc-bde20123-1 cMEQkK'}).get_text() if movie_soup.find('span', attrs={'class': 'sc-bde20123-1 cMEQkK'}) else None

        plot_text = movie_soup.find('span', attrs={'class': 'sc-466bb6c-2 chnFO'}).get_text() if movie_soup.find('span', attrs={'class': 'sc-466bb6c-2 chnFO'}) else None

        with open('movies.csv', mode='a') as fp:
            movie_writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if all([title, date, rating, plot_text]):
                print(title, date, rating, plot_text)
                movie_writer.writerow([title, date, rating, plot_text])

def extract_movies(soup):
    movies_table = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'}).find('ul')
    movies_table_rows = movies_table.find_all('li')
    movie_link = ['https://imdb.com' + movie.find('a')['href'] for movie in movies_table_rows]

    num_threads = min(MAX_THREADS, len(movie_link))

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(extract_movie_details, movie_link)



def main():
    start_time = time.time()

    # Filmes mais populares da IMDB

    popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    extract_movies(soup)

    end_time = time.time()

    print(f'Total time taken: {round((end_time - start_time), 2)} s')

if __name__ == '__main__':
    main()


