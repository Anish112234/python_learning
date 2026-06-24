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
numbers = [10,32,30,21,47]
largest_num=numbers[0]
for num in numbers:
    if num>largest_num:
        largest_num=num
        print("Largest num:",largest_num)

print("\n")
#for smallest 
smallest_num=numbers[0]
for num in numbers:
    if num<smallest_num:
        smallest_num=num
        print("samllest num",smallest_num)
    
    #for avg
    total=0
    for num in numbers:

      total += num

avg=total/len(numbers)
print("average number:",avg)

print("\n")
#count even numbers
even_counnt=0
odd_count=0
for num in numbers:
    if num%2==0:
     even_counnt+=1
    else:
        odd_count+=1
    
print("even",even_counnt)
print("odd",odd_count)


    