import pickle
def debug_mode(status):
  if status == True:
     with open("database/users.pickle","rb") as file:
        print("\n\n\nyour users are---------------")
        print(pickle.load(file))
     with open("database/cards.pickle","rb") as file:
        print("\n\n\nyour cards are --------------")
        print(pickle.load( file))
     with open("database/bank.pickle","rb") as file:
        print("\n\n\nyour bank accounts are------------")
        print(pickle.load(file)) 
     with open("database/trip.pickle","rb") as file:
        print("\n\n\nyour trips are---------")
        print(pickle.load(file))
     input(" \n\n\nhit enter to skip debug")