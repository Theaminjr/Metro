'''
menu:
- login
   - access your bank account 
   - buy ticket 
   - exit
- register
    - register and get your unique id
- adminastration
   - newtrip
   - edit trip
   - exit


# CARDS ARE REPLACED EVERY TIME <Done>
# Validation + setter getter
# STYLING TERMINAL
# CLEANING UP THE CODE
# WRITTING TESTS


'''
from logic import * 
from menu import *
from admin import *
import pickle
from debug import debug_mode



debug_mode(True) # set it as True so you can see all pickle files

menu1 = {"1" : (" Login" , login) , "2" : (" Register to metro",register) ,  "3":(" Bank login" , banklogin)  ,"4":(" Bank Register" , bankregister), "5":(" Adminastrator",adminastration) }
menu2 = { "1" : (" Get ticket" , buyticket) , "2" :(" Buy trip",buytrip) , "3": (" Exit",exit) }
menu3 = {"1" : (" New trip",newtrip) , "2" : (" Edit trip" , edittrip) , "3" : (" Exit",exit)}
menu4 = {"1" : (" Withdrawl",withdrawl), "2":(" Deposit",deposit) , "3" : (" Transaction",transaction) ,"4": (" exit",exit)}





load_all()
loggedin_as = None
while True:
   if loggedin_as == None:
      loggedin_as = menu_handler(menu1,loggedin_as)
   if type(loggedin_as) == User and loggedin_as.superuser == False:
      loggedin_as = menu_handler(menu2, loggedin_as)
   if type(loggedin_as) == User and loggedin_as.superuser == True:
      loggedin_as = menu_handler(menu3, loggedin_as)
   if type(loggedin_as) == BankAccount:
      loggedin_as = menu_handler(menu4, loggedin_as)
   




    
