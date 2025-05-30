from lib.helpers import create_user, add_transaction, view_user, view_transactions

def main():
    print("📊 Welcome to Budget Buddy CLI 📊\n")

    while True:
        print("Please choose an option:")
        print("1. Create user")
        print("2. Add transaction")
        print("3. View user")
        print("4. View transactions")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ")
            budget = float(input("Enter budget: "))
            create_user(name, budget)

        elif choice == "2":
            name = input("Enter name: ")
            description = input("Enter transaction description: ")
            amount = float(input("Enter amount: "))
            add_transaction(name, description, amount)

        elif choice == "3":
            name = input("Enter name: ")
            view_user(name)

        elif choice == "4":
            name = input("Enter name: ")
            view_transactions(name)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
