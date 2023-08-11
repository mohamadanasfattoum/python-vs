'''
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):

    string = ""

    for i in s:

        if i.isupper() == True:

            string+=(i.lower())

        else:

            string+=(i.upper())

    return string

print(swap_case(s = 'I Am Anas'))
''' 
'''
def count_substring(string, sub_string):
    x = 0
    while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
    x += 1
    return x
a= count_substring(string='abcdefg', sub_string='de')
print(a)
'''
'''
def count_substring(string, sub_string):
    i = 0
    for i in range(len(string)):
       if string[i:].startswith(sub_string):
        i += 1
    print(i)
count_substring(string='abcdefg', sub_string='cdef')
'''
'''
import textwrap

text = (
    'abcdefghigklm'
)
lines = textwrap.wrap(text,7)

for line in lines:
    print(line)
'''
'''
# set_add()
def set_add():
    for i in range(n):
        Country.add(input())
    return len(Country)
n = int(input())
Country = set()
c = set_add()
print(c)
'''

# hash()
'''
#the hash() method returns the hash value of an object if it has one. Hash values are just integers that are used to compare dictionary keys during a dictionary look quickly.

a = 'i am anas'
print (hash(a))
'''
'''
def int_hash():
    n = int(input())
    result = map(int,input().split())
    t=tuple(result)
    print(hash(t))

int_hash()
'''
'''
if __name__ == '__main__':
    n = int(input())
    result = map(int , input().split())
    print (hash(tuple(result)))
    '''
'''
from itertools import product

input_A = list(map(int, input().split()))
input_B = list(map(int, input().split()))

print(*list(product(input_A, input_B)))
'''
'''
#str1 = x , int1=y
from itertools import permutations
str1, int1 = input().split()

for i in sorted(permutations(str1, int(int1))):
    print (''.join(i))
'''

#???
'''
import re
 
 
# pattern is a string containing the regex pattern
pattern = r"[.*"
 
try:
    re.compile(pattern)
 
except re.error:
    print("Non valid regex pattern")
    exit()
'''
'''
var=input()
eval(var)'''

#  map and lambda problem solving
'''
print (list(map(len, ['Tina', 'Raj', 'Tom'])))  


sum = lambda a, b, c: a + b + c
print (sum(1, 2, 3))
'''
'''???
cube = lambda x: x**3
n = int(input())
def fibonacci(n):
    initiallist = []
    for i in range(n):
        if i < 2:
            initiallist += [i]          
        else:
            initiallist += [initiallist[-1] + initiallist[-2]]
    return initiallist
print(map(cube, fibonacci(n)))
'''
'''
a = int (input())
b = int (input())
m = int (input())
c= a**b
print(c)
print(c**m)
'''
# pow()
'''
a = int (input())
b = int (input())
m = int (input())
c= pow(a,b)
print(c)
print(pow(a,b,m))
'''
#أعد القيمة 4 إلى أس 3 ، المقياس 5 (مثل (4 * 4 * 4)٪ 5):
x = pow(4,3,5)
# 4*4*4/5
print(x)

c = pow(3,4,5)
print(c)
