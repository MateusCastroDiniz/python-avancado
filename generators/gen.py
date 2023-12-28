def mygen():

    n = 1
    print(f'Primeiro print, n é igual a {n}')
    yield n

    n = 2
    print(f'Segundo print, n é igual a {n}')
    yield n

    n = 3
    print(f'Terceiro print, n é igual a {n}')
    yield n