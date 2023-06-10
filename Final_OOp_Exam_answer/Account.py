class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []
        
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        return "Amount deposited successfully."
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount))
            return "Amount withdrawn successfully."
        else:
            return "Insufficient Balance. Unable to withdraw."
    
    def transfer(self, amount, recipient):
        if amount <= 0:
            return "Invalid transfer amount."
        
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(("Transfer", amount, recipient.name))
            recipient.transactions.append(("Transfer", amount, self.name))
            return "Amount transferred successfully."
        else:
            return "Insufficient funds. Unable to transfer."
    
    def check_balance(self):
        return f"Available balance: {self.balance}"
    
    def get_transaction_history(self):
        history = "Transaction History:\n"
        for transaction in self.transactions:
            transaction_type = transaction[0]
            amount = transaction[1]
            if transaction_type == "Transfer":
                recipient = transaction[2]
                history += f"{transaction_type} {amount} to {recipient}\n"
            else:
                history += f"{transaction_type} {amount}\n"
        return history