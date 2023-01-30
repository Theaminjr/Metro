from logic import User
admin = User("admin", "admin", "1")
admin.superuser =True
User.users["1"] = admin