# In chapter_8 we understande the consept of ::::
# Function :::::
# Recursions ::::

# for example::::::::
#if:::

# a = 32
# b = 35
# c = 39

# average = (a+b+c)/3
# print(average)

#If we want 50 numbers of avg we use function insted of doing manual:::::

# This is called function defination ::::::::::
def avg():
    a = int(input('Enter your number'))
    b = int(input('Enter your number'))
    c = int(input('Enter your number'))
    

    average = (a+b+c)/3
    print(average)

# we print it many time by using function::::::::::::::
avg()   #This is called function call()
avg()   #This is called function call()

#Quize
def goodday():
    name = input('Enter your name : ')
    print(f'have a good day {name}')

goodday()

#Function with arguments

def goodday(name):
    print('happy birthday ' + name)
goodday('haris')

#Function  with dubble argument:::::::::;;
def weds(name,name2):
    print(name2 + ' weds ' + name)

weds('Hashir', 'Mehak')


def avg():
    a = int(input('Enter your number'))
    b = int(input('Enter your number'))
    c = int(input('Enter your number'))
    

    average = (a+b+c)/3
    print(average)
    return 
a = avg()

def goodday(name = 'haris',ending = 'thank you'): # by defolt ye wali value ly ga adr meny function call kr ky value na dee
    print(f'Have a good day {name}')
    print(ending)

goodday('uzair','no brohhh')

#RECURSION
#lets try it by finding fectorial of numbers ::::::::::
def fectorial(n):
    if n==1 or n==0:
        return 1
    return n * fectorial(n-1)
n = int(input('Enter your number::'))
print(f'The fectorial or {n} is = {fectorial(n)}')

# Practice set
def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>3:
        return n2
    elif n3>n1 and n3>n2:
        return n3

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: ')) 

print(greatest(n1,n2,n3))  

#convert celcius to faranhite temperature::::::::
def f_to_c(f):
    return 5*(f-32)/9
f = int(input('Enter temperature : '))
c = f_to_c(f)
print(round(c ,2)) #Round lets 3.333333333333333 value into 3.33


# to ignore new line in function we use::::::::::
# lets spose
print('a')
print('b')   
print('c',end = '') #use to avoide new line 
print('d',end = '') #use to avoide new line 

# using recursion::::::::::;
def sum(n)  :
    if n==1 or n==0:
        return 1
    return sum(n-1) + n

print(sum(5))

def stars(n):
    if n == 0 :
        return 
    print("*"* n)
    stars(n -1)
print(stars(5))

def inch_to_cms(inch):
    return inch * 2.54
inch = int(input('Enter value in inches : ')) 
i = inch_to_cms(inch)
print(f'The {inch} inch in cms is : {round(i)} cm')

def multi(n):
    for i in range (1,11):
        print(f'{n}*{i} = {n*i}')

n = int(input('Enter your number : '))
print(multi(n))

# Ending



