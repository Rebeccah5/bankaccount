class BankAccount:
    bank ="KCB"
    
    def __init__(self,first_name,last_name,phone_number,bank):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number=phone_number
        self.bank=bank
        self.deposit=deposit[]
        self.withdraw=withdraw[]

        def get_currentTime(self);
        now=datetime.now()
        time_formatted=now.strftime("%b %d %Y,%H %M %S")
        return time_formatteds

    def get_loan(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount<=0:
            print("A loan cannot be offered at the moment")
            else:
                if self.loan=amount
                print("You have sucessfully recieved a loan of {}".format(amount))
    
    def account_name(self):
        name ="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name
    
    def  deposit(self,amount):
        try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount =0:
            print("You cannot deposit a negative amount")
        else:
            self.balance +=amount
            self.deposit.append(deposit)  
            time=date.time()
            formated_time=time.strftime{"%m %drd %Y, %H;%M:%S" }
            print("You have deposited {} on {} ".format(amount,self.account,formated_time))
      

    def get_balance(self):
        return "{} balance is {} ".format(self.account_name(),self.balance)

    def withdraw(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

      if amount=0:
      print("You cannot withdraw zero amount")
      elif amount >self.balance:
          print("You dont have enough balance to make this request")
      else:
          self.balance>=amount
          self.withdraw.append(amount)   
           formated_time=stime.strftime{"%m %drd %Y, %H;%M:%S"}
          print("You have withdrawn {} from {}".format (self.account_name,self.amount,formated_time))

    def deposit_statement(self):
      for deposit in self.deposit:
          time=diposit['time']
          formated_time=time.strftime{"%m %drd %Y, %H;%M:%S"}
          amount=deposit["amount"]
          statement="You have deposited {} on {}. Your new balance is {}".format(self.amount,formated_time,self.balance)
          print(statement)
     


def  withdraw _ statement(self,amount):
   for withdraw in self.withdrawa:
       time=deposit["time"]
       formated_time=time.strftime{"%m %drd %Y, %H:%M:%S"}
       amount withdraw=["amount"]
       statement="You have sucessfully withdrawn {} on {}".format(amount,formated_time)
       print (statement)

def pay_loan(self,amount):
     try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

    if amount>=0:
    print(" You have insufficient balance to repay the loan")
    else:
        if self.loan==0:
            print("You don't have a loan at the moment")
     else:
         if amount> self.loan:
             print("Your loan is {}, an amount less or equal is required".format(self.loan))
            

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