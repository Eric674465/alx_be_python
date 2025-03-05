class BankAccount:
    def __init__(self, initial_balance = 0):
        self._balance = initial_balance

    def deposit(self, amount):
        if self.balance <= 0:
            print("You have insufficeient funds")
            return
            self._balance += amount
            print("deposit successful")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self._balance:
            print("You have insufficient funds.")
            return False
        self._balance -= amount
        print("Withdrawal successful. New balance: $(amount)")
        return True
    
    def display_balance(self):
        print(f"Account Balance: {self.balance}")
