class BankAccount:
    def __init__(self, owner, sort_code, account_num, balance):
        self.owner = owner
        self.sort_code = sort_code
        self.account_num = account_num
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrawn £{amount:.2f}. New balance: £{self.balance:.2f}")
        elif amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            print("❌ Withdrawal amount must be positive.")

    def get_details(self):
        return (f"\n--- Account Details ---\n"
                f"Owner: {self.owner}\n"
                f"Sort Code: {self.sort_code}\n"
                f"Account Number: {self.account_num}\n"
                f"Balance: £{self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, sort_code, account_num, balance, interest_rate):
        super().__init__(owner, sort_code, account_num, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"✨ Interest of £{interest:.2f} added.")


# --- THE UPDATED LOOP ---

my_savings = SavingsAccount("Rayaan", "98-76-34", "46915328", 500, 0.05)

while True:
    print("\n--- Bank Menu ---")
    print("1. View Full Details")
    print("2. Check Balance Only")  # New option
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Add Interest")
    print("6. Exit")

    choice = input("Select an option (1-6): ")

    if choice == "1":
        print(my_savings.get_details())

    elif choice == "2":
        # Accesses the balance variable directly
        print(f"\n💰 Current Balance: £{my_savings.balance:.2f}")


    def deposit(self, amount: {__gt__}) -> None:
        if choice == "3":
            try:
                amt = float(input("Enter deposit amount: £"))
                print(my_savings.deposit(amt)-2)

            except ValueError:
                print("❌ Error: Please enter a number.")

    if choice == "4":
        try:
            amt = float(input("Enter withdrawal amount: £"))
            my_savings.withdraw(amt)
        except ValueError:
            print("❌ Error: Please enter a number.")

    elif choice == "5":
        my_savings.add_interest()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
