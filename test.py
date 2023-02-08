import unittest
from logic import *
from datetime import datetime



class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("test", "Test1234", "12345678")
        self.admin = User("admin", "admin", "1")
        self.admin.superuser =True


    def test_createuser(self):
        self.assertEqual(User.createuser("test", "Test1234", "12345678"), "success")
        self.assertRaises(Exception,User.createuser("test", "test1234", "12345678") )
        self.assertRaises(Exception,User.createuser("test", "Test1234", "123456A78"))
        self.assertRaises(Exception,User.createuser("A", "Test1234", "12345678"))
        

    def test_authenticate(self):
        self.assertEqual(User.authenticate("12345678", "test1234"), None)




class TestBank(unittest.TestCase):
    

    def setUp(self):
        self.account1 =BankAccount('test', 400000, "123456781", "Test1234")
        self.account2 =BankAccount('test2', 400000, "123456782", "Test1234")
        
    
    def test_deposit(self):
        self.assertEqual(BankAccount.deposit(self.account1, 100000), f"<{self.account1.name.title()}: {self.account1.check_balance()}>")
        self.assertRaises(Exception,BankAccount.deposit(self.account1, 10))
    
    def test_withdrawl(self):
        self.assertEqual(BankAccount.withdrawl(self.account1, 100000), f"<{self.account1.name.title()}: {self.account1.check_balance()}>")
        self.assertRaises(Exception,BankAccount.deposit(self.account1, 10))
        

    def test_transaction(self):
        BankAccount.createaccount('testtwo', 400000, "123456782", "Test1234")
        self.assertEqual(BankAccount.transaction(self.account1,"123456782",50000) , f"Transaction completed , current balance {self.account1.check_balance()}>")
        self.assertEqual(BankAccount.transaction(self.account1,"123456782",50000000) , "your balance is not enough")
    

    def test_zbank_auth(self):
        BankAccount.createaccount('test', 400000, "123456781", "Test1234")
        self.assertEqual(BankAccount.bank_auth("123456781", "Test1234"), BankAccount.bankaccounts["123456781"])
        self.assertEqual(BankAccount.bank_auth("1234567", "test1234"), None)




class TestTrip(unittest.TestCase):

    def setUp(self):
        self.user = User("test", "Test1234", "12345678")
        self.trip = Trip("24", "2", 'karaj', "tehran", 3000, "test")
        Ticket.date_charge(30000,self.user)



    def test_create(self):
        self.assertEqual(Trip.createtrip("1", "2", 'karaj', "tehran", 3000, "test"),"success")
        

    
    def test_buytrip(self):
        time = datetime.now().hour
        self.assertEqual(Trip.buytrip(self.trip, self.user, time),"success" )
        

class TestTicket(unittest.TestCase):

    
    def setUp(self):
        self.user = User("test", "Test1234", "12345678")


    def test_onetrip(self):
        self.assertEqual(Ticket.onetrip(self.user),"success")

    def test_chargable(self):
        self.assertEqual(Ticket.chargable(30000,self.user),"success")
        self.assertRaises(Exception, Ticket.chargable(10, self.user))

    def test_chargable(self):
        self.assertEqual(Ticket.date_charge(30000,self.user),"success")
        self.assertRaises(Exception, Ticket.date_charge(10, self.user))







if __name__ == '__main__':
    unittest.main()