# under standing strings consepts 
a = 'happy birthday brooh'
print(a)
print(a[4:10])
print(a[-19:-3])
print(a[3])


a = 'harris'
print(len(a))
print(a[-3:-1])
print(a[3:5])

print(a[:5])    #is same as print(a[0:5])
print(a[0:])    #is same as print(a[1:len(a)-1])
                  
a = "HhhhhharrRrrrrissSsssssss"
print(len(a))
print(a.endswith("ri"))
print(a.startswith('har'))
print(a.count('s'),a.count('r'),a.count('h'))
print(a.capitalize())
print(a.find("har"))
print(a.replace("har","HARR"))
print(a.upper())
print(a.lower())

#Escape sequences
print("hello \n haris")
print('hello \t haris')


#practicceeeeeee
list = "dear name you \nare selected\ndate"
print(list.replace('name','haris').replace('date', "23 sep 2009"))

name = 'harris     '
print(name.find('   '))

var = 'my  name  is  haris azhar'
print(var)  #Strings are immutable
print(var.replace('  ',' '))  










