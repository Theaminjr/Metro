from logic import *
from admin import *
import os
import datetime
import time



def login(loggedin_as): 
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  loggedin_as = User.authenticate(nationalid, password)
  return loggedin_as
  

def register(loggedin_as):
    fullname = input("FullName ==> ")
    password = input("password ==> ")
    nationalid = input("nationalid ==> ")
    if User.createuser(fullname,password,nationalid) :
         loggedin_as = User.authenticate(nationalid, password)
         return loggedin_as

def adminastration(loggedin_as):
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  loggedin_as = User.admin_auth(nationalid,password)
  return loggedin_as

def exit(loggedin_as):
    loggedin_as = None
    return loggedin_as

def banklogin(loggedin_as):
  print("please enter your bank account credentials")
  nationalid = input("enter your nationalid  ")
  password = input("enter your bank account password  ")
  loggedin_as = BankAccount.bank_auth(nationalid, password)
  return loggedin_as

def buyticket(loggedin_as):
    print(" 1-oneuse \n 2-chargable without expiration date \n 3-chargable with 30 days expiary date")
    choice = int(input("choose your ticket type ==> "))
    if choice == 1:
        account = banklogin(loggedin_as)
        account.withdrawl(3000)
        loggedin_as.card = Ticket.onetrip()

    if choice == 2 :
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        loggedin_as.card = Ticket.chargable(charge)    

    if choice == 3:
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        loggedin_as.card = Ticket.date_charge(charge)     

    return loggedin_as

def newtrip(loggedin_as):
    departure = input("departure : ")
    arrival = input("arrival : ")
    origin = input("origin : ")
    destination = input("destination : ")
    price = int(input("price : "))
    createdby = loggedin_as
    Trip.createtrip(departure, arrival, origin, destination, price , createdby)
    return loggedin_as

def choosetrip(loggedin_as):
    i = 0
    for trip in Trip.trips:
        i += 1
        print(i , trip)
    choice = int(input("Choose your trip ==> "))
    if choice <= len(Trip.trips) + 1:
        return Trip.trips[choice - 1]

def buytrip(loggedin_as):
    trip = choosetrip(loggedin_as)
    if loggedin_as.card == None :
        print("sorry,you dont have any card")
        time.sleep(5)
    elif loggedin_as.card.balance >= trip.price  and loggedin_as.card.expiration > datetime.datetime.now():
        loggedin_as.card.balance = loggedin_as.card.balance - trip.price
        if loggedin_as.card.type == "onetime":
            loggedin_as.card = None
    else:
        print("sorry,you dont have enough balance or your card has expired")
        time.sleep(5)
    return loggedin_as



def edittrip(loggedin_as):
    trip = choosetrip(loggedin_as)
    departure = input("departure : ")
    arrival = input("arrival : ")
    origin = input("origin : ")
    destination = input("destination : ")
    price = int(input("price : "))
    createdby = loggedin_as
    Trip.edittrip(trip, departure, arrival, origin, destination, price , createdby)
    return loggedin_as

def withdrawl(loggedin_as):
    amount = int(input("How much you want to withdraw ==> "))
    loggedin_as.withdraw(amount)
    return loggedin_as
    

def deposit(loggedin_as):
    amount = int(input("How much you want to deposit ==> "))
    loggedin_as.deposit(amount)
    return loggedin_as

def transaction(loggedin_as):
    amount = int(input("How much you want to send ==> "))
    reciever = input("Please enter national id of the reciever ==> ")
    reciever = BankAccount.bankaccounts[reciever]
    loggedin_as.transaction(reciever,amount)
    return loggedin_as

def bankregister(loggedin_as):
    name = input("please input your name ==> ")
    balance = int(input("please input you balance ==> "))
    nationalid = input("please input your natioanl id ==> ")
    password = input("please input your password ==> ")
    return BankAccount.createaccount(name, balance, nationalid, password)

def menu_handler(menu,loggedin_as):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(loggedin_as) if loggedin_as != None else print("Welcome to Metro") 
    for k in menu: 
      print(k + menu[k][0])
    choice = input("what you want to do  ")
    if  choice in menu.keys():
       loggedin_as = menu[choice][1](loggedin_as)
       return loggedin_as


        
 
  
  

