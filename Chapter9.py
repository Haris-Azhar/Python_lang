# File I/O

f = open('file.txt')
data = f.read()
print(data)
f.close()

# Read lines in a file
f2 = open('file.txt')  #For read file :::::::::
read_file = f2.readlines()
print(read_file, type(read_file))
f2.close()

# Writing in file:::::::::
str = 'Allah is the beast creaor who creat every thing'
f1 = open('mynewfile.txt', 'w')  # For write in file:::::
f1.write(str)
f1.close()


# Reading lines sepratly:::::::::::
f3 = open('file.txt')
line1 = f3.readline()
print(line1, type(line1))

line2 = f3.readline()
print(line2, type(line2))

line3 = f3.readline()
print(line3, type(line3))

line4 = f3.readline()
print(line4, type(line4))

line5 = f3.readline()
print(line5, type(line5))

line6 = f3.readline()
print(line6 == '')

f3.close()


line = 'hello every one'
f4 = open('file.txt', 'a')  # For appending in line::::::
f4.write(line)
print(f4)


# Closing file using with  statement 
f5 = open('file.txt')
data = f5.read()
print(data)
f5.close()
# Insted of that code we write with statement
with open('file.txt') as f:
    print(f.read())

# PS of chapter 9::::::::::
file = open('poems.txt' , 'r')
f_data = file.read()
if ('twinkle' in f_data):
    print('yes have')
else:
    print('Nothing')
file.close()

import random 
def game():
    print('You are playing a game...')
    score = random.randint(1,50)
    with open('hischore.txt' , 'r')as f8:
        fil = f8.read()
        if fil != '':
            fil= int(fil)
        else:
            fil = 0
    print(f'the score {score}')
    if score>fil:
        with open('hischore.txt' , 'w')as f8:
            fil = f8.write(str(score))
    return score

game()

def word():
    with open('mynewfile.txt' , 'r') as fl:
        data = fl.read()
        if 'python' in data:
            print("yes python exist")
        else:
            print('There is no python word in file')
word() 

with open('mynewfile.txt')as f9:
    lines  = f9.readlines()
linese = 1
for line in lines:
    if 'python' in line:
        print(f'the python word exest in line no ::  {linese}') 
        break
    linese += 1
else:
    print('something went wronge')

# Making copy of file::::
with open('poems.txt') as f0:
    content = f0.read()

with open('poems_copy.txt' , 'w') as f0:
    f0.write(content) 

# comperision bwt files
with open('file.txt') as f11:
    data1 = f11.read()

with open('poems.txt') as f11:
    data2 = f11.read()

if data1 == data2:
    print('These files are identical')
else:
    print("These files are not identical") 

# Wipe out content frome any file
with open('poems_copy.txt','w') as f11:
    f11.write('') 












