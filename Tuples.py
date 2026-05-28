#A built-in data type that lets us create immutables sequences of values
tup = (3,4,5,6,7,3)
print(type(tup))
print(tup[3])
#tup[3]=4 #this cannot work here because it is immutable 
print(tup[1:3])
#tuples method
print(tup.index(5))#to find element index

print(tup.count(3))#used to count how many times element repeated

#pratice
#movies = []
#movname1 = input("Enter movie name1: ")
#movname2 = input("Enter movie name2: ")
#movname3 = input("Enter movie name3: ")

#movies.append(movname1)
#movies.append(movname2)
#movies.append(movname3)
#print(movies)

#list into tupple
my_list = [2,3,5,6]
my_tuple = tuple(my_list)
print(my_tuple)
#change tuples into lsit
my_tuples= (2,4,5,5)
my_list=list[my_tuples]
print(my_list)

mystring= "hello_World";
tups=list[mystring]
print(tups)

tups=tuple(mystring)
print(tups)
#for join
tups =('H','e','l','l','o') 
my_string =''.join(tups)
print(my_string) 

#to convert dict into tuples
my_dict={"name":"ram","age":16 ,"class":10}
my_tuples= tuple(my_dict.items())
print(my_tuples)

#convet tuples into dict
my_tuples =(('name','ram'),('age',16),('class',10))
my_dict=dict(my_tuples)
print(my_dict)

#convert dict into list
my_dict = {"name":"Anish","age":20,"program":"BCSIT"}
my_list = list[my_dict.items()]
print(my_list)