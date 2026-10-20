expenses = []


def menu():
    print("===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("q. Quit")
    print()


while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter expense description: ")

        if description.strip() == "":
            print("Description cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount in naira: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        expense = {
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n===== YOUR EXPENSES =====")

            for number, expense in enumerate(expenses, start=1):
                print(
                    f"{number}. {expense['description']}: "
                    f"₦{expense['amount']:.2f}"
                )

            print()

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print(f"Total expenses: ₦{total:.2f}")

    elif choice.lower() == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    print()