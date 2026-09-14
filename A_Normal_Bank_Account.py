class BalanceException(Exception) :
    pass
class BankAccount :

    def __init__ (self, initialAmount , actname) :
        self.balance = initialAmount
        self.name = actname
        print(f"\nAccount {self.name} created.\nBalance = {self.balance :.2f}")
    # this code help us to see how much money we have
    def getBalance (self) :
             print(f"Account {self.name} , balance = {self.balance :.2f}") 
    # get money into another account
    def deposite(self , amount): 
          self.balance = self.balance + amount
          print(f"\nDeposite complete.")
          self.getBalance()
    # pick up our money from our account 

    def checkTransaction(self , amount) :
          if self.balance >= amount :
                return
          else : 
                raise BalanceException(f"Sorry account {self.name} only has balance of ${self.balance}")
                                    
                 
                
          


    # This help us to see our checktransaction
    def withdraw (self , amount) :
          try:
            self.checkTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw is compeleted")
            self.getBalance()
          except BalanceException as eror :
            print(f"\nwithdraw intrupted:{eror}")

    def transfer (self , amount , actname):
         try:
            print("\n*************\n Transfer started")
            self.checkTransaction(amount)
            self.withdraw(amount)
            actname.deposite(amount)
            print("\n*************\n Transfer completed")
           
            
         except BalanceException as eror :
            print(f"\nTransfer is intrupted:{eror}")
          


# This help us to put an IntrestReward on our Account
class IntrestRewardAccount(BankAccount) :
     def deposite(self, amount):
         self.balance += (amount * 1.05)
         print("\nDeposite completed.")
         self.getBalance()

class SavingAccount(IntrestRewardAccount):
     def __init__(self, initialAmount, actname):
          super().__init__(initialAmount, actname)
          self.fee = 5

     def transfer(self, amount, actname):
          try :
               print("\n*************\n Transfer started")
               
               self.checkTransaction(amount + self.fee)
               self.balance = self.balance - (amount + self.fee)
               self.withdraw(amount + self.fee)
               actname.deposite
          except BalanceException as eror :
               print("\nTransfer intrrupted : {eror}")
