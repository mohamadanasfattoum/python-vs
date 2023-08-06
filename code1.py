def count_substring(string, sub_string):
    x = 0
    while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
        x += 1
    return x



print(count_substring())