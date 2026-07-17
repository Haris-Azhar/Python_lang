# chp 4:::: List,tuples and arrys

list = ["Haris ","Ali", 23,34.3,True,"hello","Apple","Banana"]
print(list[0])
list[4] = False
list.append("Hassan")
list.remove("hello")
print(list)
print(list[0:5])
list.reverse()
print(len(list))

l2 = [12,5,78,4,3,435,43,6,7,789,345,78,7,0]
l2.sort()
l2.insert(2,9) #for inserting (index, value)
print(l2)

fruits = []
f1 = input("Enter fruits name: ")
fruits.append(f1)
f2 = input("Enter fruits name: ")
fruits.append(f2)
f3 = input("Enter fruits name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)
print(fruits)




markes = []
m1 = input("Enter maarkes: ")
markes.append(m1)
m2 = input("Enter maarkes: ")
markes.append(m2)
m3 = input("Enter maarkes: ")
markes.append(m3)
m4 = input("Enter maarkes: ")
markes.append(m4)
m5 = input("Enter maarkes: ")
markes.append(m5)
m6 = input("Enter maarkes: ")
markes.append(m6)
m7 = input("Enter maarkes: ")
markes.append(m7)
markes.sort()
print(markes)