#IN thast chapter we understand about loops
#like :: for or while
#while loop
i = 1
while(i<51):  #while loop dose not stope untill the condetion is fales
    print(i)
    i += 1

i = 1
while(i <10):
    print('So easy haris brohhh')
    i = i+1


l = ['haris','mee','you','uzair',12,True,654.45]
i = 0
while(i<7):
    print(l[i])
    i += 1 


#for loops
for i in range(5):
    print(i)

for i in range(0,100,4):
    print(i)

print('Thats list output')
list1 = [12,43,456,654,'hariss',True]  #Itrate in lists
for i in list1:
    print(i)

print('That tuple output')
tuple = (123,43,34,543,'hariss',True)   #Itrate in tuples
for i in tuple:
    print(i)


s = 'haris'     #Itrate in strings
for i in s:
    print(i)

l3 = [1,43,54,6]
for item in l3:
    print(item)
else:
    print("done")

#using break function:::::::
i = 0 
for i in range(100):
    if i==56:
        break   #Exit the loop ritght now
    print(i)
i = 0 
for i in range(100):
    if i==56:
        continue  #Skip this Iteration
    print(i)

for i in range(7):
    print('haris')
    if i == 5:
        break
    print(i)
   

for i in range(7):
    print('haris')
    if i == 5:
        continue
    print(i)
   

#Using pass function :::::::
for i in range(15):
    pass     #use pass fuction to stop code for later sole it
    

i = 0
while(i<10):
    if i == 5:
        break
    print('haris')
    i = i+1


# for practice
num = int(input('Enter your number'))
for i in range(1,11):
    print(f'{num} * {i} = {num*i}')


l = ['haris','hamza','hassan','hadi','ali','ahmad','sara']
for name in l:
    print(name.startswith('h'))
    print(f'hello {name}')

#printing tablle::::::::::::::

num = int(input('Enter your number'))
i = 0
while(i<11):
    print(f'{num} * {i} = {num*i}')
    i = i+1

#check prime num is have or not ::::::
num = int(input('Enter your number'))
for i in range(2,num):
    if num%i == 0:
        print('number is not prime')
        break
else:
    print('number is prime')

n = int(input('Enter your number'))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)

#Find factorial of the number:::::::::::::::::
num = int(input('Enter your number'))
product = 1
for i in range(1,num+1):
    product = product * i
print(f'the fictorial of {num} is {product}')

#for printting stars by sequence of 2::::::::
n = int(input('Enter your number'))
for i in range(1 , n+1):
    print(''*(n-i), end='')
    print('*'*(2*i-1),end='')
    print('')

# for printing stars without sequence
n = int(input('Enter your number'))
for i in range(1,n+1):
    print(''* (n-i), end = '')
    print('*'* i,end = '')
    print('')

n = int(input('Enter your number'))
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'*n, end = '')
    else:
        print('*',end = '')
        print(' '*(n-2), end = '')
        print('*',end = '')
    print('')

n = int(input("Enter your number: "))
for i in range(1, n+1):
    if i == 1 or i == n:
        print('*' * n)
    else:
        print('*', end='')
        print(' ' * (n-2), end='')   # Yahan space hai
        print('*')

#Print reverce of table using for looop :::::::::::::::::"::"":":":"
n = int(input('Enter your number : '))
for i in range(1,11):
    print(f'{n} * {11-i} = {n * (11-i)}')
    

