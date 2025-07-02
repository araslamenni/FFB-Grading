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

def main_menu():
   print("\n================================================")
   print("MAIN MENU")
   main_menu = {'add grading', 'all grading', 'edit grading', 'delete grading', 'delete all grading', 'exit program'}
   for i, m in enumerate(main_menu, start=1):
      print(f"{i}. {m}")
   print("================================================\n")


def get_user_input():
   user_input = int(input("select item in main_menu: ")) -1
   if user_input in [1,2,3,4,5,6]:
      return user_input
   else:
      print("invalid input")
      
      
      
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
   
   while True:
      main_menu()
      get_user_input()
      