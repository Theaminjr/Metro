import re

def password_validator(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
    if  re.match(pattern, password) == None:
        raise Exception("Your password should be at least 8 character long and include upper and lower case letters + numbers") 
        

def nationalid_validator(nationalid):
    pattern = "^[0-9]{6,12}$"
    if re.match(pattern, nationalid) == None:
        raise Exception("your national id should be 8-12 characters long")


def fullname_validator(fullname):
    pattern = "^[a-zA-Z ]{3,24}$"
    if re.match(pattern, fullname) == None:
        raise Exception("Name should be between 3-24 characters long")

def balance_validator(balance):
    try :
        balance = int(balance)
    except ValueError:
        raise Exception("Your input should be an integer greater than 100")
    if balance < 100:
        raise Exception("Your input should be an integer greater than 100")
    return balance    

