class BankAccount:
    def __init__(self, owner: str, balance:int):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int):
        self.balance += amount
        print(f"You've deposited {amount} and your new balance is {self.balance}")

    def withdraw(self, amount: int):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! your new balance is {self.balance}")
    def __str__(self) -> str:
        return f"owner: {self.owner}, balance: {self.balance}"


new_account = BankAccount('Osaretin', 5000)
new_account.deposit(50)
new_account.withdraw(1000)
print(new_account)