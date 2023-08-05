
'''
x=10
print(x==10)
print(x!=10)
print(x!=11)
print(x==10)

x=10
x= x+1
x+=2
x-=1
x*=3
x/=4
print(x)
'''

# neasted if
'''
x=100
if x<200:
    print('x<200')
    if x==150:
        print('150')
    elif x==50:
        print('50')
elif x>500:
    print('x>500')
print('End')
'''
'''
U='anas'
P=1111
if U=='anas' and P==1111 :
    print(True)
if U=='anas' or P==11111 :
    print(False)
'''

'''
for x in {'ahmad':18,'ali':56,'hasan':40,'mohamad':25}:
    print(x)
'''
'''
print (list(range(10)))
print (list(range(2,10,)))
print (list(range(2,10,3)))
'''
'''
for x in range (1,11,1):
    print(x)
'''
'''
x=1
while x<11:
    print(x,'\t',x**2,'\t',x**3)
    x+=1
'''
'''
start= int(input('Enter Start: ' ))
end= int(input('Enter End: ' ))

print('Numbers,\t,result')
print('-------------------')
for x in range(start,end+1):
    print(x,'\t',x**2,'\t',x**3)
'''
'''
for x in range (1,101):
    if x % 5==0 and x%10==0:
        print(x)
'''
'''
def division(x,y):
    for n in range (1,101):
        if n%x ==0 and n%y ==0 :
            print(n)
division(5,10)
'''
'''
def mysum(x,y):
    return x+y
b=mysum(5,15)
print(b)
'''
'''
mysum = lambda x,y : x+y
a=mysum(5,10)
print(a)
'''
'''
text= 'anas s a python developer , he is 25 years old'
x= text.split(',') # jede Seite von komma wird in string nur wenn komma im text drin ist.
x= text.split(' ') # jedes Wort  wird in string mit komma
print(x) 
'''
# list unpacking
numbers=[1,2,3,4,5,6]
#*z,x,y=numbers
#print(z,x,y)
'''
*_,x,y=numbers
print(*_,x,y)
print(x,y)

'''
'''
for _ in range (10):
    print(_)

'''
'''
for x,y in enumerate(['anas','ali','ahmad']):
    if x == 2:
        print('-----')

    print(f'{x} {y}\t:welcome')
'''

#docs & comments 
#explain
'''

class Calc:
    
    def sum(self,x,y):
        
                                                                                                                                                                                          
        return x+y
x= int(input('EnterX: ')) # FIX #BUG #TODO
y= int(input('EnterY: '))
c = Calc()
print(c.sum(x,y))
print(help(Calc))
'''
'''
#list comprehension

names = ['anas','ali','omar','mahmoud']
length = []
def length_name():
    for x in names:
        if len(x)>3 and x in names:
            length.append(x)
    print(length) 
length_name()

result = [len(x) for x in names]
print(result)

result2 = [x for x in names if len(x)>3]
print(result2)
'''







# map

'''
def mul(n):
    return n*2
numbers = list(range(1,11))

result = map(mul,numbers)
print(list(result))
'''
'''
def length(n):
    if len(n)>=4:
        return len(n)

names= ['anas','ali','omar','mahmoud']
result = map(length,names)
print (list (result))


def length(n):
    if len(n)>=4:
        return n

names= ['anas','ali','omar','mahmoud']
result = map(length,names)
print (list (result))

''' 
'''
names= ['anas','ali','omar','mahmoud']
result = map(lambda n :len(n),names)
print (list (result))
'''
'''
##1 return n with filter
def length(n):
    if len(n)>=4:
        return n

names= ['anas','ali','omar','mahmoud']
result = filter(length,names)
print (list (result))

##2 return n with map
def length(n):
    if len(n)>=4:
        return n

names= ['anas','ali','omar','mahmoud']
result = map(length,names)
print (list (result))

print('----------------------')


##3 return len(n) with filter
def length(n):
    if len(n)>=4:
        return len(n)

names= ['anas','ali','omar','mahmoud']
result = filter(length,names)
print (list (result))

##4 return len(n) with map
def length(n):
    if len(n)>=4:
        return len(n)
    

names= ['anas','ali','omar','mahmoud']
result = map(length,names)
print (list (result))

print('----------------------')
'''
'''
from functools import reduce
numbers= list(range(1,11))
def add_sum(x,y):
    return x+y
print(reduce(add_sum,numbers))

'''
'''
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
myset = {"apple", "banana", "cherry"}
print(type(myset))

set1 = {"abc", 34, True, 40, "male"}
print(set1)
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
'''



'''
#The sorted() function returns a sorted list of the specified iterable object.
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
x=[0,3,1,5,4,8,9]
y=('a','c','b')
a=sorted(y)
print(a)
'''
'''
a = ("h", "b", "a", "c", "f", "d", "e", "g")

x = sorted(a, reverse=False)

print(x)
'''
'''
# reverse
#The reverse() method reverses the sorting order of the elements.
b = ["h", "b", "a", "c", "f", "d", "e", "g"]

b.reverse()

print(b)
'''
