from logic import User
admin = User("ali", "admin", "1")
admin.superuser =True
User.users["1"] = admin