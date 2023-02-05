import uuid
import datetime
from validators import *
import logging

logging.basicConfig(filename='metro.log', filemode='a',level=logging.DEBUG,format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(process)d-%(levelname)s-%(message)s')

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
            logging.info(f"user was created")
            return "success"
        except Exception as e:
            logging.error("could not create user")
            return e

    def authenticate(nationalid,password):
        if nationalid in User.users.keys():
             if password == User.users[nationalid].password:
                logging.info(f"{User.users[nationalid]} logged in")
                return User.users[nationalid]
        logging.error("could not authenticate")
        return None

    
    def admin_auth(nationalid,password):
          if nationalid in User.users.keys():
              if password == User.users[nationalid].password:
                   if User.users[nationalid].superuser == True:
                        logging.info(f"admin logged in")
                        return User.users[nationalid]
          logging.error("could not authenticate")
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
            logging.info(f"a new bank account was created")
            return "success"
        except Exception as e:
            logging.error("could not create bank user")
            return e

    def check_balance(self):
        return f"<{self.__balance}>"


    def deposit(self,other):
        try:
           other = balance_validator(balance)
        except Exception as e:
            logging.error("could not deposit")
            return e
        self.__balance += other
        logging.info(f"deposit was successful")
        return(f"<{self.name.title()}: {self.__balance}>")


    def withdrawl(self,other):
        try:
           other = balance_validator(other)
        except Exception as e:
            logging.error("could not withdraw")
            return e
        self.__balance += other
        self.__balance -= other
        logging.info(f"withdrawl was successful")
        return(f"<{self.name.title()}: {self.__balance}>")


    def transaction(sender , reciever , amount):
        try:
           amount = balance_validator(other)
        except Exception as e:
            logging.error("invalid amoun for transaction")
            return e
        try:
            reciever = BankAccount.bankaccounts[reciever]
        except KeyError:
            logging.error("key error")
            return "reciever does not exist"
        if sender.__balance >= amount :
            sender.__balance -= amount
            reciever.__balance += amount
            logging.info(f"a transaction was successful")
            return (f"Transaction completed , current balance {sender.__balance}>")
        else :
            logging.error("not enough money for transaction")
            return ("your balance is not enough") 
    
    def bank_auth(nationalid,password):
          if nationalid in BankAccount.bankaccounts.keys():
                if password == BankAccount.bankaccounts[nationalid].password:
                    logging.info(f"user {BankAccount.bankaccounts[nationalid]} logged in to bank")
                    return BankAccount.bankaccounts[nationalid]
          else:
            logging.error("could not authenticate")
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
        logging.info(f"user {buyer} bought onetime trip")
        return "success"
    
    @classmethod
    def chargable(self,amount,buyer):
        try:
           amount = balance_validator(amount)
        except Exception as e:
            logging.error("invalid amount for chargable card")
            return e
        if buyer.card != None:
           if buyer.card.type == "chargable":
               buyer.card.balance += amount
               return "success"
        ticket = Ticket(amount,datetime.datetime.max)
        ticket.type = "chargable"
        self.tickets.append((buyer.id,ticket))
        buyer.card = ticket
        logging.info(f"user {buyer} bought {ticket}")
        return "success"
    
    @classmethod
    def date_charge(self,amount,buyer):
        try:
           amount = balance_validator(amount)
        except Exception as e:
            logging.error("invalid amount for date charge card")
            return e
        expdate = datetime.datetime.now() + datetime.timedelta(days=30)
        ticket = Ticket(amount,expdate)
        self.tickets.append((buyer.id,ticket))
        buyer.card = ticket
        logging.info(f"user {buyer} bought {ticket}")
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
            logging.error("invalid amount for creating a trips price")
            return e
        Trip.trips.append(Trip(departure , arrival, origin, destination, price ,createdby)) 
        logging.info("new trip was created")
        return "success"

    def edittrip(trip,departure,arrival,origin,destination,price,createdby):
        try:
            balance_validator(price)
        except Exception as e:
            logging.error("invalid amount for editting a trips price")
            return e
        trip.departure = departure
        trip.arrival = arrival
        trip.origin = origin
        trip.destination = destination
        trip.price = price
        trip.createdby = createdby
        logging.info("trip was editted")
        return "success"
    @classmethod
    def buytrip(self,trip,loggedin_as,now):
      if trip.departure< now:
        logging.error("the trip was not available")
        return f"The metro is not available at this time, its departure was at {trip.departure}"
      if loggedin_as.card == None :
          logging.error("user did not have card")
          return "sorry,you dont have any card"
      elif loggedin_as.card.balance >= trip.price  and loggedin_as.card.expiration > datetime.datetime.now():
          loggedin_as.card.balance = loggedin_as.card.balance - trip.price
          if loggedin_as.card.type == "onetime":
              loggedin_as.card = None
          logging.info(f"trip {trip} was bought")
          return "success"   
      else:
          logging.error("card did not have enough balance or it has expired")
          return "sorry,you dont have enough balance or your card has expired"
    
    @classmethod
    def deletetrip(cls,trip):
        cls.trips.remove(trip)
        logging.info(f"trip {trip} deleted")
        return "success"


    def __repr__(self):
        return f"from {self.origin} to {self.destination} departure at {self.departure} <price:{3000}> "
    

    

    


   