class PrintАverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

class PrintVolume(Exception):
    pass

def Coroutine():
    print("Starting coroutine")
    q = 1
    s = 0
    s_sq = 0
    try:
        while True:
            try:
                x = yield
                s += x
                s_sq += x**2
            except PrintАverage:
                yield s / q
            except PrintDispersion:
                yield (s_sq / q) - (s / q)**2
            except PrintVolume:
                yield q
                q += 1
    finally: 
        print("Stop coroutine")

coroutine = Coroutine()
next(coroutine)

while True:                    
    date = input()             #Ввод данных с клавиатуры. При желании можно считывать с файла или напрямую обрабатывать некий запрос
    try:
        date = float(date)
        coroutine.send(date)
        print("Current average:", coroutine.throw(PrintАverage))
        next(coroutine)
        print("Current dispersion:", coroutine.throw(PrintDispersion))
        next(coroutine)
        print("Current volume:", coroutine.throw(PrintVolume))
        next(coroutine)
    except:
        break

coroutine.close()
