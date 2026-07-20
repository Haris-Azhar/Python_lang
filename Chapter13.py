# Advance python 2
# Lamda func:::::
square = lambda x: x*x
print(square(5))

sum = lambda a,b,c:a + b + c
print(sum(1,2,3))

# join func
a = ['haris','uzair','ali']
reasult = '::'.join(a)
print(reasult)

# format:::::
f = '{} is a good {}'.format('haris','boy')
print(f)

# Map function:::::::
l = [21,34,65,43,23]
sq = lambda x:x*x
sqlist = map(sq,l)
print(list(sqlist))


# filter function::::::
def even(n):
    if n%2==0:
        return True
    return False
onlyeven = filter(even,l)
print(list(onlyeven))

name = input('Enter a name : ')
marks = int(input('Enter marks : '))
number = int(input('Enter you phone number : '))
s = 'The {} gain {} % marks and his phpne number is {}'.format(name,marks,number)
print(s)

table = [7*i for i in range(1,11)]
print(str(table))
for t in table:
    print(t)

def divisibal5(n):
    if n %5 == 0:
        return True
    return False
m = [43,65443,567654,657654,56735,2456432,375,435755,4,555,785]
f =list( filter(divisibal5,m))
print(f)

from functools import reduce
l = [43,76,43,76,45,87,65,90]
def greater(a,b):
    if a>b:
        return a
    return b
r = reduce(greater,l)
print(r)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

