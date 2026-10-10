contacts = {

}

def start_app():
    while True:
        print("=== Contact Book ===")
        print("Enter the operation you want to perform : ")
        print("1. Create new contact")
        print("2. Read a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit the app")

        try:
            choice = int(input("Choose any one of the operation : "))
        except ValueError:
            print("Choose a valid option")
            continue

        if choice < 1 or choice > 5:
            print("Invalid input")
            continue
        
        if choice == 1:
            create_contact()
        elif choice == 2:
            read_contact()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        else:
            print("Breaking the app")
            break
        


def create_contact():
    while True:
        name = input("Enter contact name : ").lower().strip()

        number = input("Enter contact number : ")

        if not number.isdigit():
            print("Wrong number")
            continue

        contacts[name] = number
        print("Contact added")
        break

def  read_contact():
    name = input("Enter the contact name : ").lower().strip()
    info = contacts.get(name)

    if not info:
        print("No contact with this name")
    else:
        print("The contact number is ", info)

def update_contact():
    while True:
        print("Do you want to update name or number ?")
        print("1. Update name")
        print("2. Update number")

        try:
            choice = int(input("Enter number :"))
        except ValueError:
            print("Invalid input")
            continue
        if choice < 1 or choice > 2:
            print("Invalid input")
            continue

        if choice == 1:
            update_name()
        elif choice  == 2:
            update_number()

        break
    

def update_number():
    while True:
        name = input("Enter name of the contact that you want to update: ").lower().strip()

        info = contacts.get(name)

        if not info:
            print("Wrong name")
            continue
        else:
            new_number = input("Enter the new number : ")
            contacts[name] = new_number
        break

def update_name():
    while True:
        name = input("Enter old name : ").lower().strip()

        info = contacts.get(name)

        if not info:
            print("Wrong name")
            continue
        else:
            new_name = input("Enter the new name : ").lower().strip()
            contacts.pop(name)
            contacts[new_name] = info   
        break

def delete_contact():
    while True:
        name = input("Enter the name of the contact that you want to delete : ").lower().strip()

        info = contacts.get(name)

        if info:
            contacts.pop(name)
            print("Contact deleted")
            break
        else:
            print("Wrong name")
            continue

start_app()