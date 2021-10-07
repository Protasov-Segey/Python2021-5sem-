import random

class Movie:
    def __init__(self, name, director, year, country, duration, age_rating):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
    def is_allowed(self, other):
        if 2021 - other.year_of_birth >= self.age_rating :
            return True
        else:
            return False
    def __str__(self):
        return f'Я {self.name}'

class Human:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth

class Cartoon(Movie):
    def __init__(self,  name, director, year, country, duration, age_rating, technique):
        super().__init__(name, director, year, country, duration, age_rating)
        self.technique = technique
    
class Anime(Cartoon):
    def __init__(self,  name, director, year, country, duration, age_rating, technique):
        super().__init__(name = name, director = director, year = year, country = 'Japan', duration = duration, age_rating = age_rating, technique = 'drawn')

movie = Movie(name="Dune", director="Denis Villeneuve", year=2021, country="USA", duration=155, age_rating=13)
cartoon = Cartoon(name="Soul", director="Pete Docter", year=2020, country="USA", duration=106, age_rating=7, technique = 'video')

human1 = Human(name="Neo", sex="M", year_of_birth=1964)
human2 = Human(name="Trinity", sex="F", year_of_birth=1967)

print(cartoon.is_allowed(human1))           


# In[99]:


import random

class Human:
    def __init__(self, name, sex, year_of_birth, hair_length, nail_length, nail_color = "бесцветные"):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color
    
    def __str__(self):
        return f'Я {self.name}, и у меня почему-то волосы длины {self.hair_length} и {self.nail_color} ногти длины {self.nail_length}'

class Worker:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth

class Manicurist(Worker):
    def do_job(self, other) :
        if other.nail_length > 1 :
            other.nail_length -= 1
        other.nail_color = random.choice(['красные', 'фиолетовые', 'зелёные'])

class Hairdresser(Worker):
    def do_job(self, other) :
        if other.hair_length > 1 :
            other.hair_length -= 1

class Barber(Worker):
    def do_job(self, other) :
        if other.sex == "M" :
            if other.hair_length > 1 :
                other.hair_length -= 1
        else: 
            raise ValueError

neo = Human(name="Neo", sex="M", year_of_birth=1964, hair_length=10, nail_length=2)
trinity = Human(name="Trinity", sex="F", year_of_birth=1967, hair_length=30, nail_length=5)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
hairdresser = Hairdresser(name = "Kate", sex="F", year_of_birth=1999)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(trinity)
barber.do_job(neo)

print(neo)
print(trinity)
