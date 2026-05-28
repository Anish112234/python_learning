marks = [30,56,64,23,43,56];
print(marks[0])#For individual access
print(len(marks))#for length 
print(type(marks))
print(marks[1:3])#slice part

student = ["Arjun",2,"kathmandu"]
print(student)
student[2] = "bhaktapur"#changing the list value
print(student)
#In python string are immutable(non changable thing)
#but lists are mutable(like changable thing)

#List method
student.append(55.6)
print(student)#(append method)adding a new item in last 
 
marks.sort()
print(marks) #sort method arrange in a order

marks.sort(reverse=True)
print(marks)#for decending

marks.insert(2,12)#replace value
print(marks)

#Remove method
marks.pop(1)
print(marks)