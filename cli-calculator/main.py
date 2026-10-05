


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def get_number(statement):
    try:
        n = int(input(statement))
    except ValueError:
        print("Wrong input selected!")
        print("Please print again")
        print()
        return get_number(statement)

    return n

while True:

    print("===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = get_number("Enter choice : ")

    if operation > 5 or operation < 1:
        print('Wrong choice!')
        continue

    if operation == 5:
        print("Goodbye amigo!")
        break

    num1 = get_number("Enter number 1 : ")
    num2 = get_number("Enter number 2 : ")

    if operation == 1:
        result = add(num1, num2)
        print("Result = ", result)
    elif operation == 2:
        result = sub(num1, num2)
        print("Result = ", result)
    elif operation == 3:
        result = mul(num1, num2)
        print("Result = ", result)
    elif operation == 4:
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            result = div(num1, num2)
            print("Result = ", result)    
    else:
        print("Wrong operation selected.")

    print()
