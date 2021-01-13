class Bank:
    def create_account(self,acno,person_name,balance,bank_name):
        self.acno=acno
        self.person_name=bank_name
        self.balance=balance
        self.bank_name=bank_name

    def deposit(self,amount):
        self.balance+=amount
        print("your acounno",self.acno,"has been credited with amount",amount,"your balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient balance in your accno",self.acno)
        else:
            self.balance-=amount
            print("your account has been debiter with amount",amount)

    def balance_enq(self):
        print("your balance",self.balance)

obj=Bank()
obj.create_account(12121,"testuser",4000,"asd")
obj.deposit(5000)
obj.withdraw(1000)
obj.balance_enq()