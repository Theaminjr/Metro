import pickle
from logic import *
def save_cards():
    with open("database/cards.pickle","wb") as file:
        pickle.dump(Ticket.tickets, file)

def save_trips():
    with open("database/trip.pickle","wb") as file:
        pickle.dump(Trip.trips, file)    

def save_users():
    with open("database/users.pickle","wb") as file:
        pickle.dump(User.users, file)    

def save_bank():
    with open("database/bank.pickle","wb") as file:
        pickle.dump(BankAccount.bankaccounts, file)

def load_all():
    with open("database/users.pickle","rb") as file:
       User.users = pickle.load(file)
    with open("database/cards.pickle","rb") as file:
       Ticket.tickets = pickle.load( file)
    with open("database/bank.pickle","rb") as file:
       BankAccount.bankaccounts = pickle.load(file)
    with open("database/trip.pickle","rb") as file:
       Trip.trips = pickle.load(file)


