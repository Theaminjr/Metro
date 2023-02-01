from logic import *
from admin import *
import os
import datetime




def login(loggedin_as): 
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  status = User.authenticate(nationalid, password)
  if status == None:
    print("National id or the password is incorrect")
    input(" HIT ENTER TO CONTINUE ")
  else:
    loggedin_as = status
  return loggedin_as
  

def register(loggedin_as):
    fullname = input("FullName ==> ")
    password = input("password ==> ")
    nationalid = input("nationalid ==> ")
    status = User.createuser(fullname,password,nationalid)  
    print(status)
    input(" HIT ENTER TO CONTINUE ")
    save_users()
    return loggedin_as

def adminastration(loggedin_as):
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  status = User.admin_auth(nationalid,password)
  if status == None:
    print("National id or the password is incorrect")
    input(" HIT ENTER TO CONTINUE ")
  else:
    loggedin_as = status
  return loggedin_as

def exit(loggedin_as):
    loggedin_as = None
    return loggedin_as

def banklogin(loggedin_as):
  print("please enter your bank account credentials")
  nationalid = input("enter your nationalid  ")
  password = input("enter your bank account password  ")
  status  = BankAccount.bank_auth(nationalid, password)
  if status == None:
    print("could not loggin")
    input(" HIT ENTER TO CONTINUE ")
  return loggedin_as

def buyticket(loggedin_as):
    print(" 1-oneuse \n 2-chargable without expiration date \n 3-chargable with 30 days expiary date")
    choice = int(input("choose your ticket type ==> "))
    if choice == 1:
        account = banklogin(loggedin_as)
        account.withdrawl(3000)
        loggedin_as.card = Ticket.onetrip(loggedin_as)
        save_cards()
        save_users()

    if choice == 2 :
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        loggedin_as.card = Ticket.chargable(charge,loggedin_as)    
        save_cards()
        save_users()

    if choice == 3:
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        loggedin_as.card = Ticket.date_charge(charge,loggedin_as)
        save_cards()
        save_users()     

    return loggedin_as

def newtrip(loggedin_as):
    departure = input("departure : ")
    arrival = input("arrival : ")
    origin = input("origin : ")
    destination = input("destination : ")
    price = int(input("price : "))
    createdby = loggedin_as
    Trip.createtrip(departure, arrival, origin, destination, price , createdby)
    save_trips()
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
        input(" HIT ENTER TO CONTINUE ")
    elif loggedin_as.card.balance >= trip.price  and loggedin_as.card.expiration > datetime.datetime.now():
        loggedin_as.card.balance = loggedin_as.card.balance - trip.price
        save_users()
        if loggedin_as.card.type == "onetime":
            loggedin_as.card = None
    else:
        print("sorry,you dont have enough balance or your card has expired")
        input(" HIT ENTER TO CONTINUE ")
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
    save_trips()
    return loggedin_as

def withdrawl(loggedin_as):
    amount = int(input("How much you want to withdraw ==> "))
    loggedin_as.withdraw(amount)
    print(status)
    save_bank()
    input(" HIT ENTER TO CONTINUE ")
    return loggedin_as
    

def deposit(loggedin_as):
    amount = int(input("How much you want to deposit ==> "))
    status = loggedin_as.deposit(amount)
    print(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def transaction(loggedin_as):
    amount = int(input("How much you want to send ==> "))
    reciever = input("Please enter national id of the reciever ==> ")
    status = loggedin_as.transaction(reciever,amount)
    print(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def bankregister(loggedin_as):
    name = input("please input your name ==> ")
    balance = input("please input you balance ==> ")
    nationalid = input("please input your natioanl id ==> ")
    password = input("please input your password ==> ")
    status = BankAccount.createaccount(name, balance, nationalid, password)
    print(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def menu_handler(menu,loggedin_as):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(loggedin_as) if loggedin_as != None else print("Welcome to Metro") 
    for k in menu: 
      print(k + menu[k][0])
    choice = input("what you want to do  ")
    if  choice in menu.keys():
       loggedin_as = menu[choice][1](loggedin_as)
       return loggedin_as


        
 
  
  

