import threading
from time import sleep

results = []
def calc_square(arr):
    for i in arr:
        sleep(0.1)
        results.append(f'Square of {i}: {i**2}\n')

def calc_cube(arr):
    for i in arr:
        sleep(0.1)
        results.append(f'Cube of {i}: {i**3}')

if __name__ == '__main__':
    arr = [1, 10, 4, 5, 9, 8]
    t1 = threading.Thread(target=calc_cube, args=(arr,))
    t2 = threading.Thread(target=calc_square, args=(arr,))

    print('\n----------Início do programa----------\n')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    for result in results:
        print(result)
    print('\n----------Fim do programa----------\n')