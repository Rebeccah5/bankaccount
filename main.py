class BankAccount:
    bank ="KCB"
    
    def __init__(self,first_name,last_name,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number=phone_number
    def get_loan(self,amount):
        self.loan+=amount
        print("You have sucecfully recieved {} shillings Mkopa loan".format(self.first_name,self.last_name())) 
    
    def account_name(self):
        name ="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name
    
    def  deposit(self,amount):
        self.balance += amount
        print("You have deposited {} shillings to your account".format(amount))
    def get_balance(self):
        return "{} balance is {} ".format(self.account_name(),self.balance)
    def withdraw(self,amount):
      self.balance-=amount
      print("You have succesfully withdrawn {} from your account".format(amount))
    def deposit(self,amount):
      if self.balance>=amount:
        self.balance-=amount
        print("You have withdrawn",amount)
      else:
       print("You have insufficient balance in your account")
    def display(self,amount):
       self.balance=amount
       print("Your account balance {}is {} ".format(self.balance_name))
acc1 = BankAccount("Clara","Makungu")
acc2 = BankAccount("Rebeccah","Wambui")
def  withdraw _ statement(self,amount):
    statement withdraw ="The amount withdrawn for {} is {}".format(self.first_name,self.last_name,amount)
    return statement withdrawn
def pay_loan(self,amount):
    if amount>=100
    self.repay=self.loan-amount
    print("Congratulations for paying{} shillings to mkopa agency"format(amount))

acc1.deposit(1000)
acc2.deposit(500)
acc1.deposit(470)
acc2.deposit(-100)
acc1.withdraw(300)
acc2.withdraw(350)
acc1.display(1700)
acc2.display()
print(acc2.get_balance())
print(acc1.get_balance()) 