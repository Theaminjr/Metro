import uuid
import datetime
from validators import *


class User():
    users = {}
    def __init__(self,fullname,password,nationalid):
        self.fullname = fullname
        self.password = password
        nationalid = nationalid
        self.id = uuid.uuid4()
        self.superuser = False
        self.card = None


    def whoami(self):
        return f"{self.fullname} , your unique id is {self.id}"


    def createuser(fullname,password,nationalid):
        try:
            fullname_validator(fullname)
            nationalid_validator(nationalid)
            password_validator(password)
            User.users[nationalid] = User(fullname,password,nationalid)
            return "success"
        except Exception as e:
            return e

    def authenticate(nationalid,password):
        if nationalid in User.users.keys():
             if password == User.users[nationalid].password:
                return User.users[nationalid]
        return None

    
    def admin_auth(nationalid,password):
          if nationalid in User.users.keys():
              if password == User.users[nationalid].password:
                   if User.users[nationalid].superuser == True:
                        return User.users[nationalid]
          return None
          
    
    def __repr__(self):
        return f"Welcome {self.fullname}, your unique id is {self.id} \nyour card status <<{self.card}>>"




class BankAccount():
    bankaccounts = {}

    def __init__(self,name,balance,nationalid,password):
        self.__balance = balance  
        self.name =name
        self.nationalid = nationalid
        self.password = password
   
    @classmethod
    def createaccount(self,name, balance, nationalid, password):
        try:
            fullname_validator(name)
            nationalid_validator(nationalid)
            password_validator(password)
            balance = balance_validator(balance)
            BankAccount.bankaccounts[nationalid] = BankAccount(name,balance,nationalid,password)
            return "success"
        except Exception as e:
            return e

    def check_balance(self):
        return f"<{self.__balance}>"


    def deposit(self,other):
        try:
           other = balance_validator(balance)
        except Exception as e:
            return e
        self.__balance += other
        return(f"<{self.name.title()}: {self.__balance}>")


    def withdrawl(self,other):
        try:
           other = balance_validator(other)
        except Exception as e:
            return e
        self.__balance += other
        self.__balance -= other
        return(f"<{self.name.title()}: {self.__balance}>")


    def transaction(sender , reciever , amount):
        try:
           amount = balance_validator(other)
        except Exception as e:
            return e
        try:
            reciever = BankAccount.bankaccounts[reciever]
        except KeyError:
            return "reciever does not exist"
        if sender.__balance >= amount :
            sender.__balance -= amount
            reciever.__balance += amount
            return (f"Transaction completed , current balance {sender.__balance}>")
        else :
            return ("your balance is not enough") 
    
    def bank_auth(nationalid,password):
          if nationalid in BankAccount.bankaccounts.keys():
                if password == BankAccount.bankaccounts[nationalid].password:
                    return BankAccount.bankaccounts[nationalid]
          else:
            return None

    
    def __repr__(self):
        return f"Welcome {self.name} your bank balance is {self.check_balance()}"

class Ticket():
    tickets = []
    def __init__(self,balance,expiration):
        self.balance = balance
        self.expiration = expiration
        self.type = ""
    
    @classmethod
    def onetrip (self,buyer):
        expdate = datetime.datetime.now() + datetime.timedelta(days=3)
        ticket = Ticket(3000,expdate)
        ticket.type ="onetime"
        self.tickets.append((buyer.id,ticket))
        buyer.card = ticket
        return "success"
    
    @classmethod
    def chargable(self,amount,buyer):
        try:
           amount = balance_validator(amount)
        except Exception as e:
            return e
        if buyer.card != None:
           if buyer.card.type == "chargable":
               buyer.card.balance += amount
               return "success"
        ticket = Ticket(amount,datetime.datetime.max)
        ticket.type = "chargable"
        self.tickets.append((buyer.id,ticket))
        buyer.card = ticket
        return "success"
    
    @classmethod
    def date_charge(self,amount,buyer):
        try:
           amount = balance_validator(amount)
        except Exception as e:
            return e
        expdate = datetime.datetime.now() + datetime.timedelta(days=30)
        ticket = Ticket(amount,expdate)
        self.tickets.append((buyer.id,ticket))
        buyer.card = ticket
        return "success"

    def __repr__(self):
        return f"your balance is {self.balance} and will expire by {self.expiration}"

class Trip():
    trips = []

    def __init__(self,departure,arrival,origin,destination,price,createdby):
        self.departure = int(departure)
        self.arrival = arrival
        self.origin =origin
        self.destination= destination
        self.price = price
        self.createdby = createdby
    
    def createtrip(departure,arrival,origin,destination,price,createdby):
        try:
            balance_validator(price)
        except Exception as e:
            return e
        Trip.trips.append(Trip(departure , arrival, origin, destination, price ,createdby)) 
        return "success"

    def edittrip(trip,departure,arrival,origin,destination,price,createdby):
        try:
            balance_validator(price)
        except Exception as e:
            return e
        trip.departure = departure
        trip.arrival = arrival
        trip.origin = origin
        trip.destination = destination
        trip.price = price
        trip.createdby = createdby
        return "success"
    @classmethod
    def buytrip(self,trip,loggedin_as,now):
      if trip.departure< now:
        return f"The metro is not available at this time, its departure was at {trip.departure}"
      if loggedin_as.card == None :
          return "sorry,you dont have any card"
      elif loggedin_as.card.balance >= trip.price  and loggedin_as.card.expiration > datetime.datetime.now():
          loggedin_as.card.balance = loggedin_as.card.balance - trip.price
          if loggedin_as.card.type == "onetime":
              loggedin_as.card = None
          return "success"   
      else:
          return "sorry,you dont have enough balance or your card has expired"
    
    @classmethod
    def deletetrip(cls,trip):
        cls.trips.remove(trip)
        return "success"


    def __repr__(self):
        return f"from {self.origin} to {self.destination} departure at {self.departure} <price:{3000}> "
    

    

    


   