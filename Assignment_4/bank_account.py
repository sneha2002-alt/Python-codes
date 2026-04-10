# Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to deposit, withdraw and check balance

class BankAccount:
  def __init__(self, acc_number, owner_name, balance = 0):
    self.acc_number = acc_number
    self.owner_name = owner_name
    self.balance = balance
    
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")
    else:
      print("Deposit amount must be positive!")   
       
    
  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
        print(f"Withdrew Rs.{amount}. New balance: Rs.{self.balance}")
      else:
        print("Insufficient funds!")
    else:
      print("Withdrawal amount must be positive!")
           
    
  def check_balance(self):
    print(f"Account {self.acc_number} ({self.owner_name}): Balance = Rs.{self.balance}")   
    
    
b1 = BankAccount(12345, "Aman", 60000) 
b1.deposit(1000) 
b1.withdraw(500)   
b1.check_balance()    