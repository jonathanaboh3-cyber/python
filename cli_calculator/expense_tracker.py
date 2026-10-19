def menu():
    print("===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("q. Quit")
    print()

menu()

choice = input("Choose an option: ")

if choice == "q":
    print("Goodbye!")