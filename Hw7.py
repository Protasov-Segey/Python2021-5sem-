import random 
class nucleic_asid:
    
    def __str__(self):
        raise NotImplemented
    
    def __repr__(self):
        raise NotImplemented
    
    def return_index(self):
        raise NotImplemented
    
    def __add__(self, other):
        raise NotImplemented
    
    def __mul__(self, other):
        raise NotImplemented
    
    def __eq__(self, other):
        raise NotImplemented

class RNA(nucleic_asid):
    def __init__(self, chain):
        check = lambda s: all(x in bases_of_RNA for x in s)    # Функция проверки на неправильные буквы
        if  check(chain):
            self.chain = chain
        else: 
            raise Exception
        self.compl_chain1 = ''
        self.compl_chain2 = ''
        self.mul_chain = ''
    
    def __str__(self):
        return f'{self.chain}'
    
    def __repr__(self):
        return f'RNA({self.chain})'
    
    def return_index(self, index):
        return f'{self.chain[index]}'
    
    def complimentary_chains_of_DNA(self):
        for i in self.chain:
            self.compl_chain1 += dict_of_RNA_to_DNA[i]
            if i == 'U':
                self.compl_chain2 += 'T'
            else:
                self.compl_chain2 += i
        return [self.compl_chain1, self.compl_chain2]
    
    def __add__(self, other):
        return RNA(self.chain + other.chain)
    
    def __mul__(self, other):
        for i in range(min(len(self.chain), len(other.chain))):
            par = random.randint(1, 2)
            if par == 1:
                self.mul_chain += self.chain[i]
            else:
                self.mul_chain += other.chain[i]
        if len(self.chain) >= len(other.chain):
            return RNA(self.mul_chain + self.chain[len(other.chain) : len(self.chain)])
        else:
            return RNA(self.mul_chain + other.chain[len(self.chain) : len(other.chain)])
    
    def __eq__(self, other):
        return self.chain == other.chain

class DNA(nucleic_asid):
    def __init__(self, chain):   #Задаётся только одна цепочка ДНК, вторая комплементарно достраивается в init'е
        self.chain = ['', '']
        check = lambda s: all(x in bases_of_DNA for x in s)    # Функция проверки на неправильные буквы
        if  check(chain):
            for j in chain:
                self.chain[0] += j
                self.chain[1] += dict_of_DNA[j]
        else: 
            raise Exception
        self.mul_chain = ''
        self.mul_compl_chain = ''
    
    def __str__(self):
        return f'{self.chain}'
    
    def __repr__(self):
        return f'DNA({self.chain})'
    
    def return_index(self, index):
        return [self.chain[0][index], self.chain[1][index]]
    
    def __add__(self, other):
        return DNA(self.chain[0] + other.chain[0])
    
    def __mul__(self, other):
        for i in range(min(len(self.chain[0]), len(other.chain[0]))):
            par = random.randint(1, 2)
            if par == 1:
                self.mul_chain += self.chain[0][i]
                #self.mul_compl_chain += dict_of_DNA(self.chain[0][i])
            else:
                self.mul_chain += other.chain[0][i]
                #self.mul_compl_chain += dict_of_DNA(other.chain[0][i])
        if len(self.chain[0]) >= len(other.chain[0]):
            return DNA(self.mul_chain + self.chain[0][len(other.chain[0]) : len(self.chain[0])])
        else:
            return DNA(self.mul_chain + other.chain[0][len(self.chain[0]) : len(other.chain[0])])
    
    def __eq__(self, other):
        return self.chain[0] == other.chain[0] and self.chain[1] == other.chain[1] #возможно избыточно второе условие, но это надежнее
            
bases_of_RNA = ['A', 'U', 'G', 'C']
bases_of_DNA = ['T', 'A', 'C', 'G']
dict_of_RNA_to_DNA = {'A' : 'T', 'U' : 'A', 'G' : 'C', 'C' : 'G'}
dict_of_DNA = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
            
            
def test():    
    chain1 = RNA('AUGCG')
    chain2 = RNA('AUGCC')
    chain_RNA_1 = chain1 + chain2
    chain_RNA_2 = chain1 * chain2
    print(chain1.return_index(2))
    print(chain1)
    print(repr(chain2))
    print(RNA.complimentary_chains_of_DNA(chain1))
    print(chain_RNA_1)
    print(chain_RNA_2)
    print(chain1 == chain_RNA_2) #Иногда True, иногда False (потому что случайный последний нуклеотид в chain)
    
    print()
    
    chain3 = DNA('TACG')
    chain4 = DNA('ACTG')
    chain_DNA_1 = chain3 + chain4
    chain_DNA_2 = chain3 * chain4
    print(chain3.return_index(2))
    print(chain3)
    print(repr(chain4))
    print(chain_DNA_1)
    print(chain_DNA_2) 
    print(chain3 == chain_DNA_2) #Аналогично иногда True, иногда False

if __name__== '__main__':
    test()
