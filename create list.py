list1 = [1,2,3,4]
print(list1)
list2=['vishal','prajwal']
print(list2)
list3=[10,20,'prajwal']
print(list3)
#by using constructor
l1= list([10,20])
print(l1)
#creating the list by using range function
l2= list(range(0,5))
print(l2)
#creating list with included character
l4= list("ABC")
print(l4)

#accessing values in list
print(list1[0])

print(list1[-1])

print(list1[3:])

print(list1[1:])
print(list1[0:4:2])
print(list1[1:3])


#deleting the elements from list

list1.pop(1)
print(list1)



list1.remove(4)
print(list1)

del list1[0]
print(list1)



#updating list

list1[0]='x'
print(list1)


#updating the list by using append method
list1.append(100,)
print(list1)


#updating list by using extend method
list1.extend([101,102,420])
print(list1)

#updating the list by using insert
list1.insert(1,[440,220])
print(list1)


#built in functions in list
lz= [1,2,3,4,5,6,7,8]
a=len(lz)
print(a)

z=max(lz)
print(z)

v=min(lz)
print(v)


s=sum(lz)
print(s)


i=lz.index(3)
print(i)


lz.reverse()
print(lz)



lz.sort()
print(lz)

















