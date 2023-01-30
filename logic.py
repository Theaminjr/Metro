import uuid
import datetime

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
        User.users[nationalid] = User(fullname,password,nationalid)
        return True
    

    def authenticate(nationalid,password):
        if nationalid in User.users.keys():
            if password == User.users[nationalid].password:
                return User.users[nationalid]

    
    def admin_auth(nationalid,password):
          if nationalid in User.users.keys():
              if password == User.users[nationalid].password:
                   if User.users[nationalid].superuser == True:
                        print(User.users[nationalid].id)
                        return User.users[nationalid]
    
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
         BankAccount.bankaccounts[nationalid] = BankAccount(name, balance, nationalid, password)
         return BankAccount.bankaccounts[nationalid]

    def check_balance(self):
        return f"<{self.__balance}>"


    def deposit(self,other):
        self.__balance += other
        return(f"<{self.name.title()}: {self.__balance}>")


    def withdrawl(self,other):
        self.__balance -= other
        return(f"<{self.name.title()}: {self.__balance}>")


    def transaction(sender , reciever , amount):
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
    
    def __repr__(self):
        return f"Welcome {self.name} your bank balance is {self.check_balance()}"

class Ticket():
    tickets = []
    def __init__(self,balance,expiration):
        self.balance = balance
        self.expiration = expiration
        self.type = ""
    
    @classmethod
    def onetrip (self):
        expdate = datetime.datetime.now() + datetime.timedelta(days=3)
        ticket = Ticket(3000,expdate)
        ticket.type ="onetime"
        return ticket
    
    @classmethod
    def chargable(self,amount):
        return Ticket(amount,datetime.datetime.max)
    
    @classmethod
    def date_charge(self,amount):
         expdate = datetime.datetime.now() + datetime.timedelta(days=30)
         return Ticket(amount,expdate)
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
    

    


   