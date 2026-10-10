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

        choice = int(input("Choose any one of the operation : "))

        if choice == 1:
            create_contact()
        elif choice == 2:
            read_contact()
        elif choice == 3:
            update_contact()
        else:
            print("Breaking the app")
            break
        


def create_contact():
    while True:
        name = input("Enter contact name : ").lower()

        number = input("Enter contact number : ")

        for char in number:
            if char.isdigit():
                continue
            print("Wrong number")
            break


        contacts[name] = number
        print("Contact added")
        break

def  read_contact():
    name = input("Enter the contact name : ").lower()
    info = contacts.get(name)

    if not info:
        print("No contact with this name")
    else:
        print("The contact number is ", info)

def update_contact():
    print("Do you want to update name or number ?")
    print("1. Update name")
    print("2. Update number")

    choice = int(input("Enter number :"))

    if choice == 1:
        update_name()
    elif choice  == 2:
        update_number()
    

def update_number():
    while True:
        name = input("Enter name of the contact that you want to update: ")

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
        name = input("Enter old name : ")

        info = contacts.get(name)

        if not info:
            print("Wrong name")
            continue
        else:
            new_name = input("Enter the new name : ")
            contacts.pop(name)
            contacts[new_name] = info   
        break

def delete_contact():
    while True:
        name = input("Enter the name of the contact that you want to delete : ")
        if contacts.pop(name):
            print("Contact deleted")
            break
        else:
            print("Wrong name")
            continue

start_app()