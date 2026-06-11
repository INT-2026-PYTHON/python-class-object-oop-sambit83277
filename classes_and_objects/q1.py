## 1. Bank Account Class 
class BankAccount:
    def __init__(self, name, account_number, opening_balance=0):
        if opening_balance < 0:
            print(
                f"Opening balance cannot be negative "
                f"(got {opening_balance}). Setting balance to 0."
            )
            opening_balance = 0

        self.name = name
        self.account_number = account_number
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit amount must be > 0 (got {amount})")
            return

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal amount must be > 0 (got {amount})")
            return

        if amount > self.balance:
            print(
                f"Insufficient funds for {self.name} "
                f"(balance={self.balance}, asked={amount})"
            )
            return

        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number} - {self.name}]: ${self.balance}"

a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob", "002")
a1.deposit(200)
a1.withdraw(100)
a2.deposit(300)
a2.withdraw(50)
a1.withdraw(2000)  
a1.deposit(-25)
a2.deposit(-50)   
a2.withdraw(500)
print(a1)
print(a2)