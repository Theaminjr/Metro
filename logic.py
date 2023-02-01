import uuid
import datetime
import pickle
import re

def save_cards():
    with open("cards.pickle","wb") as file:
        pickle.dump(Ticket.tickets, file)

def save_trips():
    with open("trip.pickle","wb") as file:
        pickle.dump(Trip.trips, file)    

def save_users():
    with open("users.pickle","wb") as file:
        pickle.dump(User.users, file)    

def save_bank():
    with open("bank.pickle","wb") as file:
        pickle.dump(BankAccount.bankaccounts, file)




def load_all():
    with open("users.pickle","rb") as file:
       User.users = pickle.load(file)
    with open("cards.pickle","rb") as file:
       Ticket.tickets = pickle.load( file)
    with open("bank.pickle","rb") as file:
       BankAccount.bankaccounts = pickle.load(file)
    with open("trip.pickle","rb") as file:
       Trip.trips = pickle.load(file)

def password_validator(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
    return True if re.match(pattern, password) else False

def nationalid_validator(nationalid):
    pattern = "^[0-9]{6,12}$"
    return True if re.match(pattern, nationalid) else False

def fullname_validator(fullname):
    pattern = "^[a-zA-Z]{3,24}$"
    return True if re.match(pattern, fullname) else False

def balance_validator(balance):
    try :
        balance = int(balance)
    except ValueError:
        return False
    if balance < 100:
        return False
    return True
        


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
        print(f"{self.fullname} , your unique id is {self.id}")


    def createuser(fullname,password,nationalid):
        if fullname_validator(fullname) != True:
            return "name should be between 3-24 characters"
        if password_validator(password) == True and nationalid_validator(nationalid) == True:
           User.users[nationalid] = User(fullname,password,nationalid)
           return "success"
        elif password_validator(password) == False:
            return "Your password should be at least 8 character long and include upper and lower case letters + numbers"
        else:
            return "your national id should be 8-12 characters long"
    

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
        self.__balance = balance  #data hiding
        self.name =name
        self.nationalid = nationalid
        self.password = password
   
    @classmethod
    def createaccount(self,name, balance, nationalid, password):
        if fullname_validator(name) != True:
            return "name should be between 3-24 characters"
        if balance_validator(balance) == False:
            return "your balance should be an integer greater than 100"
        if password_validator(password) == True and nationalid_validator(nationalid) == True:
            BankAccount.bankaccounts[nationalid] = BankAccount(name, balance, nationalid, password)
            return "success"
        elif password_validator(password) == False :
            return "Your password should be at least 8 character long and include upper and lower case letters + numbers"
        else :
            return "your national id should be 8-12 characters long"

    def check_balance(self):
        return f"<{self.__balance}>"


    def deposit(self,other):
        if balance_validator(balance) == False:
            return "your balance should be an integer greater than 100"
        self.__balance += other
        return(f"<{self.name.title()}: {self.__balance}>")


    def withdrawl(self,other):
        if balance_validator(balance) == False:
            return "your balance should be an integer greater than 100"
        self.__balance += other
        self.__balance -= other
        return(f"<{self.name.title()}: {self.__balance}>")


    def transaction(sender , reciever , amount):
        if balance_validator(amount) == False:
            return "your amount should be an integer greater than 100"
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
        return ticket
    
    @classmethod
    def chargable(self,amount,buyer):
        ticket = Ticket(amount,datetime.datetime.max)
        self.tickets.append((buyer.id,ticket))
        return ticket
    
    @classmethod
    def date_charge(self,amount,buyer):
         expdate = datetime.datetime.now() + datetime.timedelta(days=30)
         ticket = Ticket(amount,expdate)
         self.tickets.append((buyer.id,ticket))
         return ticket

    def __repr__(self):
        return f"your balance is {self.balance} and will expire by {self.expiration}"

class Trip():
    trips = []

    def __init__(self,departure,arrival,origin,destination,price,createdby):
        self.departure = departure
        self.arrival = arrival
        self.origin =origin
        self.destination= destination
        self.price = price
        self.createdby = createdby
    
    def createtrip(departure,arrival,origin,destination,price,createdby):
        Trip.trips.append(Trip(departure , arrival, origin, destination, price ,createdby)) 

    def edittrip(trip,departure,arrival,origin,destination,price,createdby):
        trip.departure = departure
        trip.arrival = arrival
        trip.origin = origin
        trip.destination = destination
        trip.price = price
        trip.createdby = createdby

    def __repr__(self):
        return f"from {self.origin} to {self.destination} departure at {self.departure} <price:{3000}> "
    

    


   