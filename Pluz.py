def pluz(arg1, arg2):
    try:
        arg = arg1 + arg2
        return arg
    except TypeError :
        pass
    try:
        arg = int(arg1) + arg2
        return arg
    except TypeError :
        pass
    try:
        arg = arg1 + int(arg2)
        return arg
    except TypeError :
        pass
    return arg1 + arg2


def test():
    print(pluz(1, 2))
    print(pluz('1', 2))
    print(pluz(1, '2'))
    print(pluz('1','2'))
    print(pluz([1], [2]))
    print(pluz(1, [2])) # А вот здесь будет TypeError

if __name__ == '__main__':
    test()
