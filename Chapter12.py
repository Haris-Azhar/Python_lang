# Advance python no 1
# Recently added features in python

# walrus operator

if n := len([1,4,6,3,7,8,5]) > 4:
    print(f'the list of ({n} number is too long that >=4)')


from typing import List,Tuple,Dict,Union
n:int = 32
m:str = 'haris'

def sum(a:int,b:int)->int:
    return a+b

print(sum(3,5))


# Match case
def http_science(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Page not found'
        case 500:
            return 'Network issues'
        case _:
            return 'Unknown error'

print(http_science(390))

# # excaption method::::::::::::
try:
    a = int(input('Hay,enter a number plz: ')) # if i pass 'str' they generate an error so,I use Exception method to make a reasonable output using 'try'
    print(a)
except Exception as e:
    print(e)
print('thank you')

# Usinh raise error function::::::::::
a = int(input('Enter a nymber : '))
b = int(input('enter a nymber : '))
if b == 0:
    raise ZeroDivisionError('hey thats not a valied number add some other insted of zero(0)')
else:
    print(f'The division or {a} and {b} is {a/b}')

print('Thank you')

# excaption method::::::::::::
try:
    a = int(input('Hay,enter a number plz: ')) # if i pass 'str' they generate an error so,I use Exception method to make a reasonable output using 'try'
    print(a)
except Exception as e:
    print(e)
finally:
    print('hey thats finally part :::') # finally word works on defs only other wise is same as print function


# using main func to import some other files::::
from Chapter11 import vector2      # It show the code of chp 11 vector2 def fuction ::::


# using global variable
a = 65  # its called global a
def fun():
    global a  # it changes the global a under def function
    a = 21
    print(a)
fun()
print(a)

# using enumerate function 
l = [32,54,True,'haris',34,'fool']
index = 0
for i in l:
    print(f'the item of index {index} is {i} ')  # insted of doing this we use enumerate:::func
    index +=1
for index,i in enumerate(l):
    print(f'the item of index {index} is {i} ') 

# squared the list
lis = [2,5,7,4,3,9]
squarelist = []
for i in lis:
    squarelist.append(i*i)

print(squarelist) # insted of that we use ::::

squarelist2 = [i*i for i in lis]   #easy way

print(squarelist2)


li = [1,2,5,7,3,4,8,9,6]
for item, i in enumerate(li):
    if item == 2 or item ==6 or item == 8:
        print(i)
try:

    with (
        open('1.txt', 'r') as f1,
        open('2.txt','r') as f2,
        open('3.txt','r') as f3

):
        print(f1.read())
        print(f2.read())
        print(f3.read())
except Exception as e:
    print(e)

n = int(input('Enter a number: '))
table = [n*i for i in range(1,11)]
for i in table:
    print(i)

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
if b == 0:
    raise ZeroDivisionError('Please enter a velide number insted of zero(0): ')
else:
    print(f'The division of {a} and {b} is {a/b}')
print('Thank you')


# appending table into a file
n = int(input('Enter a number: '))
table = [n*i for i in range(1,11)]

with open('tables.txt', 'a') as  f4:
    f4.write(f'{str(table)} \n')
for i in table:
    print(i)
    
