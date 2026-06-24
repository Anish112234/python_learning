name = "Anish"
print("Hello",name)


#condition statements
#num1 = int(input("Enter a integer"))

#if( num1>0):
#    print("The number is positive")
#elif(num1<0):
#    print("Ther number is negative")
#else:
#    print("the number is zero")    

#print 1 to 10
#for num in range(1,11):
#    print(num)

#list with sum
numbers = [10,20,30,40,50]
total=sum(numbers)
print(total)

#largest numbers 
numbers = [12,8,25,3,18]
largest_num=numbers[0]

for num in numbers:
    if num > largest_num:
      largest_num = num

print("The Largest number:",largest_num)

#print even or odd 
numbers = [10,21,32,45,50] 
for num in numbers:
   if num%2==0:
      print("The numbers is even:",num)
   else:
    print("The numbers is odd:",num)

#print a square using functions
def square(x):
    return x*x
print("The square of number is:",square(5))  


#mini challenges
student = {
   "name":"Anish",
   "age":20,
   "city":"Lalitpur"
}

print(student["name"])
print(student["age"])
print(student["city"])