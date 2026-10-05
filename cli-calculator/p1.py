


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


while True:

    print("===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = input("Enter your choice: ")

    if operation == "5":
        print("Goodbye amigo!")
        break

    num1 = int(input("Enter number 1 : ")) #input always gives string
    num2 = int(input("Enter number 2 : "))

    if operation == "1":
        result = add(num1, num2)
        print("Result = ", result)
    elif operation == "2":
        result = sub(num1, num2)
        print("Result = ", result)
    elif operation == "3":
        result = mul(num1, num2)
        print("Result = ", result)
    elif operation == "4":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            result = div(num1, num2)
            print("Result = ", result)    
    else:
        print("Wrong operation selected.")

    print()
