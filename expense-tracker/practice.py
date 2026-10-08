import csv
expenses = [
    {
        "category": "Food",
        "amount": 250,
        "description": "Lunch"
    },
    {
        "category": "Travel",
        "amount": 100,
        "description": "Bus"
    }
]

with open("expenses.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["category", "amount", "description"]
    )

    writer.writeheader()
    writer.writerows(expenses)

with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    expenses = list(reader)

print(expenses)
