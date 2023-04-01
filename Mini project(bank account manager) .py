#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

class BusinessAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

def main():
    # create accounts
    checking = CheckingAccount()
    savings = SavingsAccount()
    business = BusinessAccount()

    while True:
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Business Account")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter choice: "))
            if ch == 1:
                amount = float(input("Enter amount to deposit: "))
                checking.deposit(amount)
            elif ch == 2:
                amount = float(input("Enter amount to withdraw: "))
                checking.withdraw(amount)
            else:
                print("Invalid choice")

        elif choice == 2:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter choice: "))
            if ch == 1:
                amount = float(input("Enter amount to deposit: "))
                savings.deposit(amount)
            elif ch == 2:
                amount = float(input("Enter amount to withdraw: "))
                savings.withdraw(amount)
            else:
                print("Invalid choice")

        elif choice == 3:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter choice: "))
            if ch == 1:
                amount = float(input("Enter amount to deposit: "))
                business.deposit(amount)
            elif ch == 2:
                amount = float(input("Enter amount to withdraw: "))
                business.withdraw(amount)
            else:
                print("Invalid choice")

        elif choice == 4:
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


# In[ ]:




