import multiprocessing

results = []

def calc_square(arr):
    global results
    for i in arr:
        print(f'Square of {i}: {i**2}\n')
        results.append(i**2)
    return results


if __name__ == '__main__':
    arr = [1, 10, 4, 5, 9, 8]
    m1 = multiprocessing.Process(target=calc_square, args=(arr,))

    m1.start()

    m1.join()

    print(f'resultados: {results}')