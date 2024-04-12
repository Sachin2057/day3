import random
class BankAccount:
    def __init__(self,accountNumber,balance,accountType):
        print("Constructor for bankaccount")
        self.accountNumber=accountNumber
        self.balance=balance
        self.accountType=accountType
    def __del__(self):
        print("BackAccount Object Deleted")
class Customer:
    def __init__(self,name,age,address,accountType) -> None:
        print("Constructor for customer")
        self.name=name
        self.age=age
        self.address=address
        self.account=BankAccount(random.randrange(200,300),random.randrange(200,300),accountType)
    def __del__(self):
        print("Customer object deleted")
customer=Customer("Sachin",23,"Pepsicola","savings")