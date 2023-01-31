import pickle
def debug_mode(status):
  if status == True:
     with open("users.pickle","rb") as file:
        print("\n\n\nyour users are---------------")
        print(pickle.load(file))
     with open("cards.pickle","rb") as file:
        print("\n\n\nyour cards are --------------")
        print(pickle.load( file))
     with open("bank.pickle","rb") as file:
        print("\n\n\nyour bank accounts are------------")
        print(pickle.load(file)) 
     with open("trip.pickle","rb") as file:
        print("\n\n\nyour trips are---------")
        print(pickle.load(file))
     input(" \n\n\nhit enter to skip debug")