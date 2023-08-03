# 1:100
# odd even



'''
def number():
    odd=[]
    even=[]
    for n in range (1,101):
        if n%2==0:
            even.append(n)
            
        

        else:
            odd.append(n)
            

    print(f'in even numbers{even}')
    print(f'in odd numbers{odd}')
number()

'''


'''
def number():
    odd=[]
    even=[]
    n=1
    while n<=100:
        if n%2==0:
            even.append(n)
            n+=1

        if n%2!=0:
            odd.append(n)
            n+=1

    print(f'in even numbers{even}')
    print(f'in odd numbers{odd}')
number()
'''

'''
even = [ n for n in list(range (1,101)) if n%2==0]
print(even)


odd= [ n for n in list(range (1,101)) if n%2!=0]
print(odd)
'''

# map
def mul(n):
    return n*2
numbers = list(range(1,11))

result = map(mul,numbers)
print(list(result))