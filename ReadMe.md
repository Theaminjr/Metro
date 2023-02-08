# Metro 
this project has 4 diffrent entities that work together to simulate Metro

## Metro users
* metro users are made from  normal users and an admin (admin user is hardcoded at the startup and there is only one admin account)
* normal users should be able to register to metro , buy metro cards and choose trips
* admin is able to add new trips and edit already existing ones or delete them.
* to buy tickets as a metro user you need to enter bank account credentials
* users can only choose from trips that its departure time has not passed yet
 
## BankAccount
* this is a independant entity from metro users. 
* you can register to bank 
* every bank user can do deposit,withdrawl,Transaction 


## metro cards
* there are 3 deffrent types of tickets
* onetime ==> you pay once and is disabled after the first use
* date_chargable ==> you payone and can charge it with whatever amount of credit you desire but it will expire after a month
* chargable ==> no expiration date and you can recharge it again if you ran out of credit


## metro trips
* metro trips are only managed by the admin
* they have attributes such as price, departure time , destination and origin


## database:
* datas are saved in pickle files. all pickle files are loaded at the start up and they are rewritten when datas are changed through the runtime

## validators
* there are some validators written at validators.py to help validate the data
* for example : passwords should be more than 8 characters long consisting uppercase and lower case letters and digits

## menu
* every menu item has its specific function which are written at the menu.py


