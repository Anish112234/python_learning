#sum two numbers using input

#num1 = int(input("Enter a first integer:"))
#num2 = int(input("enter a Second integer:"))
#sum = num1 + num2
#print(sum)

#read two number and print a larger one

a=3
b=4
if a>b:
    print("The greate number is a",a)
else:
    print("The greater number is b",b)

#given a dictornary print a name
dict={"name":"Anish","age":20,"Address":"lalitpur"}
print(dict["name"])


#print 1to 10 using loop
for i in range(1,11):
    print(i)


#store 5 numbers in list and print their average
list = [1,2,3,4,5]
avg=sum(list)/len(list)
print(avg)
print("\n")







#write a function number that return in square form
def square(x):
    num=x*x
    print("Anish",num)
square(2)    
print("\n")

#pring print largest,smallest and average based on list 
numbers = [10,20,30,40,50]
for num in numbers:
    if num>numbers:
     print(num)
    
    