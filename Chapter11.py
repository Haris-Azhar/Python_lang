#  using multi intence classes
# In this chapter 11 we learn about Inheritence and more OOPs
class employee:
        name = 'ali'
        company = 'ARFA'
        def show(self):
            print(f'The employee of the year is {self.name} which work on {self.company}')
            


class languages:
    language = 'py'
    def lang(self):
        print(f"the language of every coder in ARFA is {self.language}")

class programer(employee,languages):
    company = "ARFA kutt"
    def programar(self):
        print(f'This programar work on {self.company} comapny and using {self.language}')

b = programer()
b.programar() 

# Using @classmethod this ignore instence value and print given a class value
class method():
    a = 12
    @classmethod
    def show(cls):
        print(f"The class attributes of 'a' is {cls.a}")

m = method()
m.a = 72
m.show()

# Shows instence value and ignore given a value
class method():
    a = 12
    def show(self):
        print(f"The class attributes of 'a' is {self.a}")

m = method()
m.a = 72
m.show()


class nummbers:
    def __init__(self,n):
        self.n = n
    def  __add__(self, num):
        self.num = num
        return self.n + num.n
    def __mul__(self,num):
        return self.n * num.n
    def __truediv__(self,num):
        return self.n / num.n
    def __floordiv__(self,num):
        return self.n // num.n

n =nummbers(2) 
m =nummbers(5) 
print(n // m)


# PS of chp 11:::::::::::::::
class twoDvector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print(f'the vector a is {self.a} adn b is{self.b}')

class threeDvector(twoDvector):
    def __init__(self,a,b,c):
        self.c = c
        super().__init__(a,b)
    def show(self):
        print(f'the vector a is {self.a} adn b is{self.b} and b is {self.c}')
n = twoDvector(12,23)
n.show()
m = threeDvector(12,23,17)
m.show()
print(m.a,m.b,m.c)


class Animals():
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print('The dog bark like BOW! BOW! hahahahaha')

c = Dog()
c.bark()

class employee:
    pass
