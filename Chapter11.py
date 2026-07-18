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
<<<<<<< HEAD

class employee:
    pass
=======

class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return complex(self.r + c2.r, self.i +  self.i)
    def __mul__(self,c2):
        return complex(self.r * c2.r, self.i *  self.i)

    def __str__(self):
        return f'{self.r} + {self.i}i'

c1 = complex(5,7)
c2 = complex(2,4)
print(c1 +c2)
print(c1 *c2)

# Find the len of vector
class vector:
    def __init__(self,lis):
        self.lis = lis

    def __len__(self):
        return len(self.lis)

v1 = vector([3,4,6,7,5,7,9])
print(len(v1))

class vector2:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    def __add__(self,var):
        work = vector2(self.a + var.a, self.b + var.b ,self.c + var.c)
        return work

    def __mul__(self,var):
        return vector2(self.a * var.a, self.b * var.b ,self.c * var.c)

    def __str__(self):
        return f'{self.a}i + {self.b}j + {self.c}k'

v3 = vector2(1,3,4)
v4 = vector2(5,7,9)
v5 = vector2(6,1,2)

print(v3 + v4 + v5)
print(v3 * v4 * v5)



class vector2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, var):
        return vector2(
            self.a + var.a,
            self.b + var.b,
            self.c + var.c
        )

    def __mul__(self, var):
        return vector2(
            self.a * var.a,
            self.b * var.b,
            self.c * var.c
        )

    def __str__(self):
        return f'{self.a}i + {self.b}j + {self.c}k'


v3 = vector2(1, 3, 4)
v4 = vector2(5, 7, 9)
v5 = vector2(6, 1, 2)

print(v3 + v4 + v5)
print(v3 * v4 * v5)


>>>>>>> a97a365 (Updated chapter11.py)
