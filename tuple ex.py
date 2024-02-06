#creating a tuple 

t1=(10,20,30)
print(t1)
t2=(10,20,30,'vishal')
print(t2)
t3 = (1,2,3,'vishal',[10,20])
print(t3)

(first,sec,thi)=t1
print(first)


tz=(100,)
print(tz)


a1=type(tz)
print(a1)

#accessing values in tuple
a=t1[:2]
print(a)

q=t1[2:3]
print(q)

#deleting values in tuple
del t2


t6=t3[:3] + t3[4:]
print(t6)

#concat the tuple
tr=(12,13)
te=(45,46)
t7=tr+te
print(t7)

#operator repatation
tv=tr*3
print(tv)

#membership operator
print(1 in t3)

