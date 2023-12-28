def helloWrld():
    print('Parte 1')
    x = yield
    print(x)

    x += yield
    print(x)

    x += yield
    print(x)


try:
    h = helloWrld()
    next(h)
    h.send(1)
    h.send(2)
    h.send(3)
except StopIteration:
    print('Fim da função.')
