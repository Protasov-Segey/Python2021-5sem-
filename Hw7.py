import random
class nucleic_asid:
    def complimentary_chain(self):
        raise NotImplemented
    
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
    
class RNA(nucleic_asid):
    def __init__(self, chain):
        check = lambda s: all(x in bases_of_RNA for x in s)    # Функция проверки на неправильные буквы
        if  check(chain):
            self.chain = chain
        else: 
            raise Exception
        self.compl_chain = ''
    def __str__(self):
        return f'{self.chain}'
    
    def __repr__(self):
        return f'RNA({self.chain})'
    
    def return_index(self, index):
        return f'{self.chain[index]}'
    
    def complimentary_chain(self):
        for i in self.chain:
            self.compl_chain += dict_of_RNA[i]
        return f'{self.compl_chain}'
    
    def __add__(self, other):
        return RNA(self.chain + other.chain)
    
    #def __mul__(self, other):
               
bases_of_RNA = ['A', 'U', 'G', 'C']
bases_of_DNA = ['T', 'A', 'C', 'G']
dict_of_RNA = {'A' : 'U', 'U' : 'A', 'G' : 'C', 'C' : 'G'}
dict_of_DNA = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
            
            
def test():    
    chain1 = RNA('AUUC')
    chain2 = RNA('GGG')
    chain = chain1 + chain2
    print(chain1)
    print(repr(chain2))
    print(RNA.complimentary_chain(chain))

if __name__== '__main__':
    test()
