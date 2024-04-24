#use difine function
def a(a):
    print("vishal and prajwal",a)
a("rakesh")



#addition using function

def b(x,y):
    print(x+y)
b(10,20)



#display the list by using function

def z():
    list1=[1,2,3,4]
    list2=[5,6,7,8]
    print(list1,list2)
z()



#sum of 10 to 20 no using function

def c():
    s=0
    for i in range (11,21,1):
        s=s+i
        print(s)

c()


#types of argument


#require argement

def add1(x,y):
    print(x+y)
add1(10,20)


#keyword argument
def sa(name,roll):
    print (name,roll)


roll= 10
name= "vishal"

sa(roll,name)


#dafault argument
def g(name ,roll=12,enrr=22):
    print(name,roll,enrr)
g("vishal",13,21)


#variable length argument
def display1(q,*l1):
    print(q,l1)
display1(12,13,14)
























