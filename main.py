import json

def intro():
   print("================================================")
   print("++++ FRESH FRUIT BUNCHES GRADING APLICATION ++++")
   print("================================================\n")

def read_json(filename):
   with open(filename, 'r') as file:
      data = json.load(file)
      return data

def save_json(filename, db):
   with open(filename, 'w') as file:
      json.dump(todos, file)
      
def login(db):
   username = input("username: ")
   password = input("password: ")
   if username in db and db[username]['password'] == password:
      print(f"Welcome back, {username}")
      return db[username]
   else:
      print("username or password not invalid, please register.")

   

if __name__ == "__main__":
   db = read_json("database_grading.json") 
   intro()
   login(db)