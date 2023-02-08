from logic import *
from admin import *
from database_funcs import *
import os
from terminal_color import *




def login(loggedin_as): 
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  status = User.authenticate(nationalid, password)
  if status == None:
    print_FAIL("National id or the password is incorrect")
    input(" HIT ENTER TO CONTINUE ")
  else:
    loggedin_as = status
  return loggedin_as
  

def register(loggedin_as):
    fullname = input("FullName ==> ")
    password = input("password ==> ")
    nationalid = input("nationalid ==> ")
    status = User.createuser(fullname,password,nationalid)  
    if status == "success":
        print_OKGREEN(status)
    else:
        print_FAIL(status)
    input(" HIT ENTER TO CONTINUE ")
    save_users()
    return loggedin_as

def adminastration(loggedin_as):
  nationalid = input("enter your nationalid  ")
  password = input("enter your password  ")
  status = User.admin_auth(nationalid,password)
  if status == None:
    print_FAIL("National id or the password is incorrect")
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
    print_FAIL("could not log in")
    input(" HIT ENTER TO CONTINUE ")
    return loggedin_as
  else:
    return status 
   
def buyticket(loggedin_as):
    print_WARNING("WARNING: only permanent cards can be recharged. if you already have other type of card it will be replaced")
    if input("do you want to continue ? (n for no)") == "n":
        return loggedin_as
    print_OPTIONS(" 1-oneuse \n 2-permanent ,chargable without expiration date \n 3-chargable with 30 days expiary date")
    choice = int(input("choose your ticket type ==> "))
   
    if choice == 1:
        account = banklogin(loggedin_as)
        account.withdrawl(3000)
        status = Ticket.onetrip(loggedin_as)
        if status != "success":
             account.deposit(charge) 
             print_FAIL(status)
        print_OKGREEN(status)
        input(" HIT ENTER TO CONTINUE ")
        save_cards()
        save_users()

    if choice == 2 :
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        status = Ticket.chargable(charge,loggedin_as) 
        if status != "success": 
            account.deposit(charge) 
            print_FAIL(status)
        print_OKGREEN(status)
        input(" HIT ENTER TO CONTINUE ")  
        save_cards()
        save_users()

    if choice == 3:
        account = banklogin(loggedin_as)
        charge = int(input("How much you want to charge it ==> "))
        account.withdrawl(charge)
        status = Ticket.date_charge(charge,loggedin_as)
        if status != "success": 
            account.deposit(charge) 
            print_FAIL(status)
        print_OKGREEN(status)
        input(" HIT ENTER TO CONTINUE ")
        save_cards()
        save_users()     
    else:
        print("invalid choice")

    return loggedin_as

def newtrip(loggedin_as):
    departure = input("departure : ")
    arrival = input("arrival : ")
    origin = input("origin : ")
    destination = input("destination : ")
    price = int(input("price : "))
    createdby = loggedin_as
    status = Trip.createtrip(departure, arrival, origin, destination, price , createdby)
    if status != "success": 
        print_FAIL(status)
    else:
        print_OKGREEN(status)
    input(" HIT ENTER TO CONTINUE ")
    save_trips()
    return loggedin_as

def choosetrip(loggedin_as,now):
    i = 0
    for trip in Trip.trips:
        i += 1
        print(i,end=" ")
        if trip.departure< now:
           print(trip,end=" ")
           print_WARNING("Not available")
        else:
           print(trip,end=" ")
           print_OKGREEN("Available")
    choice = int(input("Choose your trip by entering the number ==> "))
    try :
        return Trip.trips[choice - 1]
    except Exception:
        return None


def buytrip(loggedin_as):
    time = datetime.datetime.now().hour
    print_header(f"it is {time} Oclock now")
    trip = choosetrip(loggedin_as,time)
    if trip == None:
        print_FAIL("Trip does not exist")
        return loggedin_as
    status = Trip.buytrip(trip,loggedin_as,time)
    if status != "success": 
        print_FAIL(status)
    else:
        print_OKGREEN(status)
    save_users()
    input(" HIT ENTER TO CONTINUE ")
    return loggedin_as



def edittrip(loggedin_as):
    time = datetime.datetime.now().hour
    trip = choosetrip(loggedin_as,time)
    if trip == None:
        print_FAIL("Trip does not exist")
        input(" HIT ENTER TO CONTINUE ")
        return loggedin_as
    departure = input("departure : ")
    arrival = input("arrival : ")
    origin = input("origin : ")
    destination = input("destination : ")
    price = int(input("price : "))
    createdby = loggedin_as
    status = Trip.edittrip(trip, departure, arrival, origin, destination, price , createdby)
    if status != "success": 
        print_FAIL(status)
        input(" HIT ENTER TO CONTINUE ")
    print_OKGREEN(status)
    input(" HIT ENTER TO CONTINUE ")
    save_trips()
    return loggedin_as

def deletetrip(loggedin_as):
    time = datetime.datetime.now().hour
    trip = choosetrip(loggedin_as,time)
    if trip == None:
        print_FAIL("Trip does not exist")
        input(" HIT ENTER TO CONTINUE ")
        return loggedin_as
    status = trip.deletetrip(trip)
    print_OKGREEN(status)
    save_trips()
    input(" HIT ENTER TO CONTINUE ")
    return loggedin_as


def withdrawl(loggedin_as):
    amount = int(input("How much you want to withdraw ==> "))
    loggedin_as.withdraw(amount)
    if status != "success": 
        print_FAIL(status)
    else:
        print_OKGREEN(status)
    save_bank()
    input(" HIT ENTER TO CONTINUE ")
    return loggedin_as
    

def deposit(loggedin_as):
    amount = int(input("How much you want to deposit ==> "))
    status = loggedin_as.deposit(amount)
    if status != "success": 
        print_FAIL(status)
    else:
        print_OKGREEN(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def transaction(loggedin_as):
    amount = int(input("How much you want to send ==> "))
    reciever = input("Please enter national id of the reciever ==> ")
    status = loggedin_as.transaction(reciever,amount)
    if status != "success": 
        print_FAIL(status)
    else:
       print_OKGREEN(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def bankregister(loggedin_as):
    name = input("please input your name ==> ")
    balance = input("please input you balance ==> ")
    nationalid = input("please input your natioanl id ==> ")
    password = input("please input your password ==> ")
    status = BankAccount.createaccount(name, balance, nationalid, password)
    if status != "success": 
        print_FAIL(status)
    print_OKGREEN(status)
    input(" HIT ENTER TO CONTINUE ")
    save_bank()
    return loggedin_as

def menu_handler(menu,loggedin_as):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header(loggedin_as) if loggedin_as != None else print_header("Welcome to Metro") 
    for k in menu: 
      print_OKBLUE(k + menu[k][0])
    choice = input("what you want to do  ")
    if  choice in menu.keys():
       loggedin_as = menu[choice][1](loggedin_as)
       return loggedin_as


        
 
  
  

