from admin import Admin
from Bank import Bank
from Account import Account

bank = Bank()

# Creating user accounts --- Create two new accounts for checking transfers history
user1 = bank.create_account("Emtiaz", "emtiaz2060")
user2 = bank.create_account("Efty", "emtiazahmedefty")


#we can check deposit history and aslo check withdraw history
user1.deposit(1000000)
user1.withdraw(5000)
user2.deposit(7000)

# Transferring amount
user1.transfer(300, user2)

# Checking available balance
print(user1.check_balance())
print(user2.check_balance())

# Checking transaction history
print(user1.get_transaction_history())

# Checking total available balance and loan amount
print(bank.check_total_balance())
print(bank.check_total_loan_amount())


#-------------------------Its not working--------------
# Enabling or disabling loan feature
bank.enable_loan_feature()
bank.disable_loan_feature()