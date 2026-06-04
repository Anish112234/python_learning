def greet(name):
    print("Hello",name)
greet("anish")

def year(age):
    print("I am",age,"years old")
year(20)
    

#genarate username based on name
name = input("Enter Your name:")
username = name+""+str(len(name)) 
print(username+"@gmail.com")