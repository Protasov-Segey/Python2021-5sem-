import os
import sys
import threading

def thread_job(file, string, num):
    with open(file, 'r') as book:
        while True:
            line = book.readline()
            if not line:
                break
            if string in line:
                print(f'{books[num]}:', line)
        sys.stdout.flush()

s = str(sys.argv[1])
directory = str(sys.argv[2])
books = os.listdir(directory)

if __name__=='__main__':
    threads = [
        threading.Thread(target=thread_job, args=(os.path.join(directory, books[i]), s, i))
        for i in range(len(books))
    ]
    for thread in threads:
        thread.start()  
    for thread in threads:
        thread.join()  
