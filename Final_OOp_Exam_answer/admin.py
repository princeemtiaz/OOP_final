from Bank import Bank

class Admin(Bank):
    def __init__(self):
        super().__init__()
        
    def create_account(self, name, password):
        account = super().create_account(name, password)
        return account

    def check_total_balance(self):
        return self.total_balance
    
    def check_total_loan_amount(self):
        return self.total_loan_amount
    
    def enable_loan_feature(self):
        self.can_take_loan = True
    
    def disable_loan_feature(self):
        self.can_take_loan = False