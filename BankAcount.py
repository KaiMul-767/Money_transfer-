class BalanceExeception(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance = initialAmount
        self.Name= acctName
        print(
            f"\n account '{self.Name}' created. \n Balance ৳ {self.balance:.2f} ")
        
    def getbalance(self):                                                                  
        print(f"\nAccount '{self.Name}' Balance ৳ {self.balance:.2f}")
    def diposite(self,amount):
        self.balance = self.balance + amount
        print("\n Diposite Completed")
        self.getbalance()
        
    def viableTransection(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceExeception(
                f"\n sorry, account '{self.Name}' only balance has a of ৳{self.balance:.2f}"
                )
    def withdraw(self,amount):
        try:
            self.viableTransection(amount)
            self.balance = self.balance - amount
            print('\n withdraw completed')
            self.getbalance()
        except BalanceExeception as error:
            print(f'\n withdraw interapted: {error}')

    def transfer(self,amount,account):
        try:
            print('\n Begining transfer.....')
            self.viableTransection(amount)
            self.withdraw(amount)
            account.diposite(amount)
            print('\n Transfer Completed')
        except BalanceExeception as error:
            print(f'\n Transfer Interapted....{error}')

class Interstrewards(BankAccount):
    def diposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Diposite complete.")
        self.getbalance()
    
class SavingAccount(Interstrewards):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 20

    def withdraw(self, amount):
        try:
            self.viableTransection(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n withdrow complete.")
            self.getbalance()
        except BalanceExeception as error:
            print(f"\n withdrow interapted:{error}")
            

