def decorator(func):
    def wrapper():
        return func()
    return wrapper
@decorator
def greet():
    return "Anish"
@decorator
def know():
    return "Are u programmer"
print("Welcome",greet())
print(know())

#sum two number using function and decorstor
def decorator(func):
    def wrapper(a,b):
        result = a+b
        return result
    return wrapper
@decorator
def sum(a,b):
     return a+b
result =sum(2,4)
print("The sum of two number is",result)

#for a multiplication
@decorator 
def mul(a,b):
    return a*b
result = mul(2,2)
print("Multiplication of Two number",result)
