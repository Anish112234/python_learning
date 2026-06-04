class person:

    def __init__(self,name,age):

     self.name=name
     self.age=age

person1=person("Anish",20)
person2=person("Aakash",23)

print(person1.name)
print(person1.age)
#for print person2
print(person2.name)
print(person2.age)

print("\n")
#new class for devices
class device:
   def __init__(self,brand,model):
    self.brand=brand
    self.model=model
device1=device("Anroid","POCO-x3")
print("The brand of Device is",device1.brand) 
print("The Mode of Device",device1.model)  