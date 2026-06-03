#To rev the string
string = "hello World"
rev = string[::-1]
print(rev)

#to rev the string without usingout slicing
string = "hello world"
for char in string:
    rev = char + rev
    print(rev)

    #to rev the string using recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
string = "Hello World"
rev = reverse_string(string)
print(rev)