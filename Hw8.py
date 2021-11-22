def file_reader_first(file):
    for line in file:
        yield print(line.strip())

def file_reader_second(file):
    while True: 
        line = file.readline()
    
        if not line:
            break
        
        yield print(line.strip())

with open('Cline Ernest. Ready Player One.txt', 'r') as file:
    generator1 = file_reader_first(file)
    next(generator1)
    next(generator1)

    generator2 = file_reader_second(file)
    next(generator2)
    next(generator2)
    
    for i in range(100):  #Вывод 100 строчек
        next(generator2)
    
    assert generator1 == generator2
    #Как я понимаю, я создал 2 генератора, которые считывают попеременно 1 и тот же файл, с того же места
        
