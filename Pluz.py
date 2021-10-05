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

print(pluz(arg1, arg2))


