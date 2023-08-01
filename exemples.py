
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
#x= text.split(',') # jede Seite von komma wird in string nur wenn komma im text drin ist.
#x= text.split(' ') # jedes Wort  wird in string mit komma
                  # es macht split mit was man gibt 
#x= text.split('anas')
print(x) 
'''
'''
l = [1,2,4,6,7,'anas,true,9,10']
l.insert(3,2000)
print(l)
'''