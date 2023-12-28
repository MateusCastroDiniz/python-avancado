from functools import reduce

def addition_operation(*args):
    # lista = []
    # _ = map(lambda x: lista.append(x), *args)
    soma = reduce(lambda x, y: x+y, args)
    return soma

def subtraction_op(*args):
    sub = reduce(lambda x, y: x-y, args)
    return sub