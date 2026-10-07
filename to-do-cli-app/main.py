# tasks = []


def load_tasks():
    with open("tasks.txt") as f:
        tasks = f.read().splitlines()
    return tasks


def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

    # tasks.append(task)

def show_tasks():
    tasks = load_tasks(); 
    if len(tasks) == 0:
        print("No tasks added yet!")
        return
    print("Tasks")
    for i, x in enumerate(tasks):
        print(i + 1,". ", x)

def delete_task():
    tasks = load_tasks()

    if len(tasks) <= 0:
        print("No tasks to delete")
        return

    while True:
        try:
            num = int(input("Enter the task number that you want to delete : "))
        except ValueError:
            print("Invalid input!")
            continue
        
        if num < 1 or num > len(tasks):
            print("Please select a valid task")
            continue

        tasks.pop(num - 1) # Could also use tasks.remove(tasks[num-1])

        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

        print("Task deleted!")
        break
    

def start_app():

    while True: 
        print("Choose one of the following opertions :")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit App")

        try:
            choice = int(input("Enter the operation that you want to perform : "))
        except ValueError:
            print("Invalid input!")
            continue

        
        if choice == 4:
            print("Exiting app...")
            break

        if choice > 4 or choice < 1:
            print("Invalid input!")
            continue

        if choice == 1:
            show_tasks()
        elif choice == 2:
            task = input("Please enter the task : ")
            add_task(task)
        elif choice == 3:
            
            delete_task()
        
    

start_app()