import json

def intro():
   print("\n================================================")
   print("++++ FRESH FRUIT BUNCHES GRADING APLICATION ++++")
   print("================================================\n")

def read_json(filename):
   with open(filename, 'r') as file:
      data = json.load(file)
      return data

def save_json(filename, db):
   with open(filename, 'w') as file:
      json.dump(db, file)
      
      
def login(db):
   username = input("username: ")
   password = input("password: ")
   if username in db and db[username]['password'] == password:
      print(f"Welcome back, {username}")
      return db[username]
   else:
      print("username or password not invalid, please register.")

def register(db):
   username = input("username: ")
   password1 = input("password: ")
   password2 = input("confirm password: ")
   if username  not in db and password1 == password2:
      db[username] = {'name': username, 'password': password1, 'grading': []}
      save_json('database_grading.json', db)

if __name__ == "__main__":
   db = read_json("database_grading.json") 
   intro()
   login_or_register = input('login_or_register: ')
   if login_or_register == 'login':
      user = login(db)
   elif login_or_register == 'register':
      user = register(db)
   else:
      print('wrong input')