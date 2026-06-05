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
print("The Model of Device",device1.model)  

#instanc
#bug here fixed this later
class device:
   def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    
    def full_name(self):
      return f"{self.brand}{self.model}"
    

device1=device("Anroid","POCO-x3")
print("The brand of Device is",device1.brand) 
print("The Model of Device",device1.model) 
print(device1.full_name())


#inheritance 
#do in home

#HW WAP display the parent's deals on the student and make a another class of the students and inheritance the parent class


