#In chp 5 we understand the concept of dictionary and sets
dict1 = {
    'haris': 100,
    'Uzair': 234,
    'Umar': 345,
    'ali': 456
}
print(dict1, type(dict1))

print(dict1['haris'])
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.update({'haris': 200 , 'hannan':230}))
print(dict1.get('ali'))
print(dict1)
print(dict1.get('hannan22')) #print NONE 
print(dict1['hannan22'])  #print error because hannan is not in the dictionary
print(len(dict1))
emt_dict = {}  #Empty dictionary
print(type(emt_dict))

#About sets::::::::::::::;
set1 = {1,2,3,4,5,6,6,6,6}  #set dosn't allow duplicate values
emt_set = set()    #Empty set :::
print(set1,type(emt_set))
print(len(set1))
set1.add(26)
set1.remove(6)
print(set1)

s1 = {1,2,3,54,45,67,8,90}
s2 =  {32,34,1,2,3,76,78,90,}
print(s1.union(s2))  #union(take and arrange all values) of two sets
print(s1.intersection(s2))  #intersection(common values) of two sets

words = {
    'kutta': 'dog',
    'billi': 'cat',
    'share': 'lion',
    'hatti': 'alephant' 
}
word = input('Enter your word for meaning: ')

print(words[word])

s = set()
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
n = int(input('Enter the number :'))
s.add(n)
print(s)

s4 = set()
s4.add(20)
s4.add(20.0)
s4.add('20')
print(len(s4))

s = {}
print(type(s))

d = {}
name = input('Enter your name :')
lang = input('Enter your language :')
d.update({name: lang})
name = input('Enter your name :')
lang = input('Enter your language :')
d.update({name: lang})
name = input('Enter your name :')
lang = input('Enter your language :')
d.update({name: lang})
name = input('Enter your name :')
lang = input('Enter your language :')
d.update({name: lang})
print(d)
print(len(d))
print(d.items())
print(d.keys())
print(d.values())
