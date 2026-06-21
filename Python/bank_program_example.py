import json
import os
import getpass  # safer password input

DATA_FILE = "data.json"

# ------------------ Data Handling ------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ------------------ Core Features ------------------

def create_account(users):
    username = input("Enter new username: ")

    if username in users:
        print("❌ User already exists.")
        return

    password = getpass.getpass("Enter password: ")
    confirm = getpass.getpass("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    users[username] = {
        "password": password,
        "balance": 0,
        "transactions": []
    }

    print("✅ Account created successfully!")


def login(users):
    username = input("Enter username: ")

    if username not in users:
        print("❌ User not found.")
        return None

    password = getpass.getpass("Enter password: ")

    if users[username]["password"] != password:
        print("❌ Incorrect password.")
        return None

    print(f"✅ Welcome, {username}!")
    return username


def deposit(users, user):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("❌ Amount must be positive.")
            return

        users[user]["balance"] += amount
        users[user]["transactions"].append(f"Deposited: {amount}")

        print("✅ Deposit successful!")

    except ValueError:
        print("❌ Invalid amount.")


def withdraw(users, user):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Amount must be positive.")
            return

        if amount > users[user]["balance"]:
            print("❌ Insufficient balance.")
            return

        users[user]["balance"] -= amount
        users[user]["transactions"].append(f"Withdrew: {amount}")

        print("✅ Withdrawal successful!")

    except ValueError:
        print("❌ Invalid amount.")


def show_balance(users, user):
    print(f"💰 Balance: {users[user]['balance']}")


def show_transactions(users, user):
    print("📜 Transaction History:")
    for t in users[user]["transactions"]:
        print("-", t)


# ------------------ Menu Systems ------------------

def user_menu(users, user):
    while True:
        print("\n--- User Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            deposit(users, user)
        elif choice == "2":
            withdraw(users, user)
        elif choice == "3":
            show_balance(users, user)
        elif choice == "4":
            show_transactions(users, user)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")

        save_data(users)


def main():
    users = load_data()

    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account(users)
            save_data(users)

        elif choice == "2":
            user = login(users)
            if user:
                user_menu(users, user)

        elif choice == "3":
            save_data(users)
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()