"""
Create a banking management system where-

User
Can create an account.
Can deposit and withdrawal amount. 
Can check available balance.
Can transfer the amount from his account to another user account.
Can check transaction history.
Can take a loan from the bank twice of his total amount..

Note - User can only withdraw and transfer money from his account if he has money in his account.
If a user is unable to withdraw the amount of money he has deposited in the bank, he will get a message that the bank is bankrupt.

Admin 
Can create an account
Can check the total available balance of the bank.
Can check the total loan amount.
Can on or off the loan feature of the bank.


"""
class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.balance = 0
        self.loan = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited_amount: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn_amount: {amount}")
        else:
            print("Sorry! Withdrawal is not possible due to insufficient funds")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received: {amount} from {self.name}")
        else:
            print("Sorry ! You have insufficient balance to transfer.")

    def available_balance(self):
        print(f"Your current balance is {self.balance}")

    def taking_loan(self,amount):
        if self.loan==0:
            loan_limit= 2* self.balance
            self.loan=loan_limit
            self.balance+=loan_limit
            self.transaction_history.append(f"Loan have been taken {loan_limit}")
        else:
            print("Sorry ! Already you have taken loan")


class Bank:
    def __init__(self):
        self.users = []
        self.total_bank_balance = 0
        self.total_loan_amount = 0
        self.loan_option = True

    def create_account(self, name, username, password):
        user = User(name, username, password)
        self.users.append(user)
        print(f"Congratulations {user.name}, Your account successfully created")

    def admin_check_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total balance in bank: {total_balance}")

    def admin_check_loan_amount(self):
        total_loan = sum(user.loan for user in self.users)
        print(f"Total loan amount in the bank: {total_loan}")

    def admin_toggle_loan_feature(self, enable):
        self.loan_option = enable
        status = "enabled" if enable else "disabled"
        print(f"The loan feature of the bank has been {status}.")




    
    

#======================================================================



# Create user instances
user1 = User("Maidul","maidul1",123)
user2= User("jahid","jahid2",1345)
user1.deposit(5000)
user1.withdraw(4000)
user1.transfer(user2,700)
print(user1.transaction_history)
user1.available_balance()

bank = Bank()
bank.create_account("Maidul", "Maidul", "password")

# Now, you can use the admin methods:
bank.admin_check_balance()
bank.admin_check_loan_amount() 

    
