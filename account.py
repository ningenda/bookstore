class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class is created for checking""" 
    type="Checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee

gaurav_checking=Checking("gaurav.txt",50)
gaurav_checking.transfer(-8000)
print(gaurav_checking.balance)
gaurav_checking.commit()
print(gaurav_checking.type)

ankita_checking=Checking("ankita.txt",50)
ankita_checking.transfer(-8000)
print(ankita_checking.balance)
ankita_checking.commit()
print(ankita_checking.type)
