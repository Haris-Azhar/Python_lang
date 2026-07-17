#In chp 6 we talk about Conditional Expressions 
#if_else statements
age = int(input('Enter your age :'))
if age >= 18:
    print('Yes \n you are eligible')
elif age < 0:
    print('thats not age brohhhh')
else:
    print('No \n you are not eligible')

a = float(input('Enter your number :'))
b = int(input('Enter your number :'))
if a%2 == 0:
    print('Even')
elif a% 2!=0:
    print('odd')
elif b%2 == 0:
    print('Even')
elif b% 2!=0:
    print('odd')
else:
    print('Invalid input')

#if else elif Practice work
a1 = int(input('Enter number 1 :'))
a2 = int(input('Enter number 2 :'))
a3 = int(input('Enter number 3 :'))
a4 = int(input('Enter number 4 :'))
if a1 > a2 and a1 > a3 and a1> a4:
    print('a1 is greater:: ',a1)
elif a2 > a1 and a2 > a3 and a2> a4:
    print('a2 is greater:: ',a2)
elif a3 > a1 and a3 > a2 and a3> a4:
    print('a3 is greater:: ',a3)
elif a4 > a1 and a4 > a2 and a4> a3:
    print('a4 is greater:: ',a4)
else:
    print('All are equal brohhhh')


sub1 = int(input('Enter your marks in sub1 :'))
sub2 = int(input('Enter your marks in sub2 :'))
sub3 = int(input('Enter your marks in sub3 :'))
#total percentage
total_percentage = (sub1 + sub2 + sub3)/300*100
if total_percentage >= 40 and sub1 >=33 and sub2 >=33 and sub3>=33:
    print('You are pass now!',total_percentage)
else:
    print('so sad bro you are faild!',total_percentage )


p1 = 'come hare'
p2 = 'click this'
p3 = 'this is free'
p4 = 'so sorry check it'
p5 = 'i love your'
message = input('Enter a comment:: ')

if p1 in message or p2 in message or p3 in message or p4 in message or p5 in message:
    print('This is spam !!!')
else:
    print('Its safe brouuhh, just chilll ')


username = input('Enter your name:;;')
if len(username)<10:
    print('Valide username::::::::',username)
else:
    print('invalide username::::::', username)


list1 = ['harris','ali','ahmad','uzair','ramzan']

name = input('Enter your name::')
if name in list1:
    print(name,'in the list')
else:
    print(name,"are not in the list")

markes = int(input('Enter your markes:'))
if markes <=100 and markes >=90:
    grade = 'A+'
elif markes <90 and markes >80:
    grade = 'A'
elif markes <80 and markes >70:
    grade = 'B'
elif markes <70 and markes >60:
    grade = 'C'
elif markes <60 and markes >50:
    grade = 'D'
elif markes <50:
    grade = 'F'
print('your grade is ', grade)


post = input('Enter your post::')
if 'haris'.lower() in post.lower():   #use lower() to detect haris in any wording shape:::
    print("The post talking about you")
else:
    print("The post is not talking about you")



