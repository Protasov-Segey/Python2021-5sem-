from multiprocessing import Pool, Process, Queue
import sys
from time import time
from time import sleep

def factor(N):
    k = 2
    factors = []
    
    while N != 1:
        if N % k == 0:
            factors.append(k)
            N = N // k
        else:
            k += 1
    
    return factors

var = sys.argv[1:]
for j in range(len(var)):
    var[j] = int(var[j])

if __name__=='__main__':
    pool = Pool(processes=10)  #Я поставил 10 процессов, но не знаю, от чего должно зависеть выбранное количество
    results = pool.map(factor, var)
    for i in range(len(results)):
        print(f'{var[i]}: ', " ".join(map(str, results[i])))  