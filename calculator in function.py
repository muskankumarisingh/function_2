def main(num1,num2):
    if user=="add":
        add(num1,num2)
    elif user=="subtract":
        subtract(num1,num2)
    elif user=="multiply":
        multiply(num1,num2)
    elif user=="divide":
        divide(num1,num2)
    else:
        pass
def add (num1,num2):
    print(num1+num2)
def subtract (num1,num2):
    print(num1-num2)
def multiply (num1,num2):
    print(num1*num2)
def divide (num1,num2):
    print(num1%num2)
user=input("add,subtract,multiply,divide")
num1=int(input("enter the number"))
num2=int(input("enter the number"))
main(num1,num2)