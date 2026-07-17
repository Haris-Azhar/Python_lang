# OOPs
'''class employe():
    language = 'C++'   # These are class attributes
    salary = 140000 
    work = 'on_site'

haris = employe()
haris.name = 'haris azhar'   # These are object attributes
print(haris.language,haris.work,haris.name)

# Using function under classes
class home():
    member = 'ali'
    net_work = '5G'
    phone = 'nokia'

    def __init__(self,phone,member,net_work):  # This is dunder attribute which autometicaly called::::::::

        print('good morning brooh')

    def funk(self):
        print(f'{self.member} is the member of home which have {self.phone} phone with {self.net_work} net work')

    @staticmethod
    def greet(): # Insted of using self we use @staticmethod 
        print('hello Alii')
ali = home('haris','4G','hawavy')
print(ali.member,ali.phone)
ali.funk()
ali.greet()
# Creating Calculatror:::::::::::::::::
class calculator():
    def __init__(self,n):
        self.n = n
    def sq(self):
        print(f'the square  of {self.n} is {self.n*self.n}')
    def cube(self):
        print(f'the square  of {self.n} is {self.n*self.n*self.n}')
    def sq_root(self):
        print(f'the square  of {self.n} is {self.n**1/2}')

cel = calculator(4)
cel.sq()
cel.cube()
cel.sq_root()'''


import random 
class train():
    def __init__(self,trainNO):
        self.trainNO = trainNO
    def book(self,fro,to):
        self.fro =fro
        self.to = to
        print(f'The train from {self.fro} to {self.to}')
    def time(self,tim):
        print(f'the train no : {self.trainNO} araive on time')
    def tigit(self):
        print(f'the tigit price of  train from {self.fro} to {self.to} is {random.randint(500,1500)}')

cl = train(47)
cl.book('karachi', 'lahore')
cl.time('11:46pm')
cl.tigit()

# Same question but using  slf or name like haris or sonme other insted of self....

import random 
class train():
    def __init__(slf,trainNO):
        slf.trainNO = trainNO
    def book(self,fro,to):
        self.fro =fro
        self.to = to
        print(f'The train from {self.fro} to {self.to}')
    def time(self,tim):
        print(f'the train no : {self.trainNO} araive on time')
    def tigit(self):
        print(f'the tigit price of  train from {self.fro} to {self.to} is {random.randint(500,1500)}')

cl = train(47)
cl.book('karachi', 'lahore')
cl.time('11:46pm')
cl.tigit()