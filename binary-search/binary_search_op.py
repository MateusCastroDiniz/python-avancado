def binary_search(lista, find, low, high):

    while low <= high:
        mid = int(low + (low - high)/2)

        if lista[mid] == find:
            print('Achei!')
            return mid
        elif lista[mid] < find:
            low = mid + 1
        else:
            high = mid - 1


resultado = binary_search([1, 2, 3, 4, 5], 2, 0, (len([1, 2, 3, 4, 5])-1))

print(resultado)