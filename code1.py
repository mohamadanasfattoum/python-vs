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
def count_substring(string, sub_string):
    i = 0
    for i in range(len(string)):
       if string[i:].startswith(sub_string):
        i += 1
    print(i)
count_substring(string='abcdefg', sub_string='cdef')
'''