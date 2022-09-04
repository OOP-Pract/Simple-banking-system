#Parent Class User
#Has a function to show user details

#Child Class : Bank
#Store details about the acc balance
#Stores details about the amount
#Allows for deposites, Widthdraw, View balance


#Parent Class
from msilib.schema import Class


class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def showDetails(self):
        print("Personal Details")
        print(" ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("ACC Balance has been updated : Rs ",self.balance)

    def withdraw (self,amount):
        self.amount=amount

        if self.amount>self.balance:
            print("Insufficient Funds | Balance available : Rs ", self.balance)

        else:
            print("ACC balance has been updated : Rs ", self.balance)

    def view_balance(self):
        self.showDetails()
        print("Acc Blance : ", self.balance)
        





