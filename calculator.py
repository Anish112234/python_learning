#find bug
#choice statement
#fixed bug already
def addition():
    value1 = int(input("Enter integer"))#use int(bug apper)
    value2 = int(input("Enter integer"))
    return value1 + value2

def subtraction():
    value1 = int(input("Enter integer"))
    value2 = int(input("Enter integer"))
    return value1-value2
     
def multiplication():
    value1 = int(input("Enter integer"))
    value2 = int(input("Enter integer"))
    return value1*value2

def division():
    value1 = int(input("Enter integer"))
    value2 = int(input("Enter integer"))
    if value2 == 0:
         return "Error:division by zero is not avaiable"
    return value1/value2

def calculator():
     print("welcome To calculator:")
     print("1:addition")
     print("2:subtraction")
     print("3:Multiplication")
     print("4:Division")
     print("Enter 'q' to Quit.")

     while True:
        choice = input("\nChoose an operation(1/2/3/4)or 'q' to Quit").strip()
        if choice == 'q':
               print("Exiting The calculator.Goodbye!")
               break
          
        if choice == '1':
              print(f"the result of addition is : {addition()}")
        elif choice =='2':
             print(f"the result of subtraction is :{subtraction()}")
        elif choice == '3':
             print(f"the result of multiplication is :{multiplication()}")
        elif choice == '4':
             print(f"the result of division is :{division()}")
        else:
             print("Invalid choice")     #I missed else (bug apper)

calculator()