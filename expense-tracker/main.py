expense = []

def start_app():

    print("=== Expense tracker app ===", end="\n")

    while True:
        print("Enter the operation which you want to perform : ")
        print("1. Show expense")
        print("2. Add expense")
        print("3. Delete expense")
        print("4. Exit")


        while True:
            try:
                choice = int(input("Enter the operation : "))
            except ValueError:
                print("Invalid input!")
                continue

            if choice < 1 or choice > 4:
                print("Invalid input!")
                continue

            break

            

        if choice == 1:
            show_expense()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            delete_expense()  
        else:
            print("Exiting...")
            break
        

def show_expense():
    if len(expense) == 0:
        print("No expenses to show")
        return

    for index, item in enumerate(expense):
        print(
            index + 1,
            item["category"],
            item["amount"],
            item["description"]
        )

def add_amount():
    while True:
        try:
            amount = int(input("Enter amount : "))
        except ValueError:
            print("Invalid input!")
            continue

        if amount < 1:
            print("Invalid input!")
            continue
        break

    return amount

def add_catgeory_description(text):
    while True:
        data = input(text)
        if len(data) < 1:
            print("Enter something!")
            continue
        break

    return data
    
def add_expense():
    category = add_catgeory_description("Enter the category you want to add the expense into : ")
    amount = add_amount()
    description = add_catgeory_description("Enter the description : ") 

    expense.append({
        "category": category,
        "amount": amount,
        "description" :description
    })

    print("Expense added")

def delete_expense():
    if len(expense) == 0:
        print("No expense to delete")
        return
    show_expense()
    while True:
        try:
            index = int(input("Enter the expense you want to delete : "))
        except ValueError:
            print("Invalid input!")
            continue  

        if index < 1 or index > len(expense):
            print("Invalid input!")
            continue
        break

    expense.pop(index - 1)

    print("Expense deleted")
    

start_app()