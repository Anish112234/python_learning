animal = {"Tiger","Cow","Lion","Monkey","Dog"};
animal.add("goat")#add new animal
print(animal)

animal.update(["Horse","cat"])#upadte animal

animal.remove("Dog");#remove anmal
print(animal)

print(len(animal))#use specific function

#converting
animal_list=list(animal)#set into list
animal_Tuple=tuple(animal)#set into tuple
animal_dict=dict.fromkeys(animal)#set into dict
print("\n animal in lsit:")
print(animal_list)
print("\n animal in tuple:")
print(animal_Tuple)
print("\n animal in dict")
print(animal_dict)

del animal

print("\n The set animals is delected");