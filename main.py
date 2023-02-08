# Metro User : 0311987540  Pass:Amin1378
# Bank User :  0311987540  Pass:Amin1378
# Admin user : 1  Pass:admin

from logic import * 
from menu import *
from admin import *
from database_funcs import *
import pickle
from debug import debug_mode




debug_mode(False) # set it as True so you can see all pickle files

menu1 = {"1" : (" Login to Metro" , login) , "2" : (" Register to Metro",register) ,  "3":(" login to Bank  " , banklogin)  ,"4":(" Register to Bank " , bankregister), "5":(" Adminastrator",adminastration) }
menu2 = { "1" : (" Get ticket" , buyticket) , "2" :(" Buy trip",buytrip) , "3": (" Exit",exit) }
menu3 = {"1" : (" New trip",newtrip) , "2" : (" Edit trip" , edittrip) ,"3":(" Delete trip",deletetrip), "4" : (" Exit",exit)}
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
   




    
