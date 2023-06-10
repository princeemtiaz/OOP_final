from Account import Account
class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True
    
    def create_account(self, name, password):
        account = Account(name, password)
        self.accounts.append(account)
        return account
    
    def check_total_balance(self):
        return f"Total available balance: {self.total_balance}"
    
    def check_total_loan_amount(self):
        
        return f"Total loan amount: {self.total_loan_amount}"
    
    #---------------------Its not working----------------------------------
    
    # def check_total_balance(self):
    #     total_balance = 0
    #     for account in self.accounts:
    #         total_balance += account.balance
    #     return f"Total available balance: {total_balance}"

    #---------------------Its not working--------------------------------
    
    def enable_loan_feature(self):
        self.loan_feature_enabled = True
    
    def disable_loan_feature(self):
        self.loan_feature_enabled = False