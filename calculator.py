#find bug
#choice statement
#bug here
def addication():
    value1 = float(input("Enter integer"))
    value2 = float(input("Enter integer"))
    return value1 + value2

def subtraction():
    value1 = float(input("Enter integer"))
    value2 = float(input("Enter integer"))
    return value1-value2
     
def multiplication():
    value1 = float(input("Enter integer"))
    value2 = float(input("Enter integer"))
    return value1*value2

def division():
    value1 = float(input("Enter integer"))
    value2 = float(input("Enter integer"))
    if value2 == 0:
         return "Error:division by zero is not avaiable"
    return value1/value2

def calculator():
     print("welocome To calculator:")
     print("1:addication")
     print("2:subtraction")
     print("3:Multiplication")
     print("4:Division")
     print("Enter 'q' to Quute.")

     while True:
        choice = input("\nChoose an operation(1/2/3/4)or 'q' to Quite").strip()
        if choice == 'q':
               print("Existing The calculator.Goodbye!")
               break
          
     if choice == '1':
              print(f"the result of addication is : {addication()}")
     elif choice =='2':
             print(f"the result of subtraction is :{subtraction()}")
     elif choice == '3':
             print(f"the result of multiplication is :{multiplication()}")
     elif choice == '4':
             print(f"the result of division is :{division()}")