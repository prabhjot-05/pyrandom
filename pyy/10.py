from array import *
array1 = array('i', [10,20,30,40,50])

for x in array1:
 print(x)

print (array1[0])

print (array1[2])


array1.insert(1,60)
for x in array1:
 print(x)

array1.remove(40)
for x in array1:
 print(x)


print (array1.index(20))

array1[2] = 80
for x in array1:
 print(x)



array1[2:5] = array('i', [4, 6, 8])
for x in array1:
 print(x)