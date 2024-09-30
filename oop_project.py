from BankAcount import*


Shojol_Vai = BankAccount(100000,"Shojol_Vai")
Reza_Vai = BankAccount(100000,"Reza_Vai")
Noman_vai = BankAccount(100000,"Noman_Vai")

Shojol_Vai.getbalance() 
Reza_Vai.getbalance()
Noman_vai.getbalance()

Shojol_Vai.diposite(5000)
Reza_Vai.diposite(6000)
Shojol_Vai.withdraw(1000)
Shojol_Vai.transfer(4000,Reza_Vai)

anik = Interstrewards(1000,"anik")
anik.getbalance()
anik.diposite(1000)
anik.transfer(100,Reza_Vai)

ferdus = SavingAccount(1000,"ferdus")
ferdus.getbalance()
ferdus.diposite(1000)
ferdus.transfer(100, anik)

