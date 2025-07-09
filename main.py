import json
from datetime import datetime 

def intro():
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("===== FRESH FRUIT BUNCHES GRADING APPLICATION POM 2 =====")
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
    
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new database.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. starting with an empty database.")
        return {}

def save_json(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=4) #ada perbaikan di sini

    
def login(db):
    username = input("username: ")
    password = input("password: ")
    if username in db and db[username]['password'] == password:
        print(f"Welcome back, {username}!") # ada perbaikan
        return db[username] # ada perbaikan
    else:
        raise ValueError("Invalid number or password. Please try again or register.")
    
def register(db):
    while True:
        username = input("username: ")
        if username in db:
            print("Username already exist. Please choose a different username.")
            continue
        password1 = input("password: ")
        password2 = input("confirm password: ")
        if password1 == password2:
            db[username] = {'username': username, 'password': password1, 'grading': [] }
            save_json('database_grading.json', db)
            print(f'User {username} registered successfully!')
            return db[username]
        else:
            print('password do not match. Please tray again.')        
        
def main_menu():
    print("\n=============================================================")
    print("                        MAIN MENU                            ")
    main_menu_optin = ('add grading', 'show grading', 'edit grading', 'delete grading', 'delete all grading', 'exit grading')
    for i, m in enumerate(main_menu_optin, start=1):
        print(f"{i}. {m}")
        
    print("=============================================================\n")        
            
def get_user_input_menu_choice():
    while True:
        try:
            user_input = int(input("Select item from the main menu: "))
            if 1 <= user_input <= 6:
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 to 6")
        except:
            print("invalid input, Please enter a number") 

def add_grading(grading):
    input_choice= input("Do you wanto to add grading?(y/n): ").lower()
    if input_choice == 'n':
        return grading 
    elif input_choice == "y":
        estate = input("Estate: ")
        division = input("Division: ")
        block = input("Block: ")
        noMobil = input("Plate number: ")
        ripeness_data = {}
        while True:
            try:
                print("\n===Enter Ripeness Percentages===")
                unRipe = int(input("Unripe percentage(0-100): "))
                underRipe = int(input("Underripe percentage(0-100): "))        
                overRipe = int(input("Overripe percentage(0-100): "))        
                emptyFruit = int(input("Empty Fruit percentage(0-100): "))        
                rotten = int(input("Rotten percentage(0-100): "))        
                
                if not all(0 <= p <= 100 for p in [unRipe, underRipe, overRipe, emptyFruit, rotten]):
                    print("All percentages must be between 0 and 100. Please Try again.")
                    continue
                
                total_order = unRipe + underRipe + overRipe + emptyFruit + rotten
                if total_order > 100:
                    print(f"The sum of unripe, underripe, overripe, empty fruit, rotten ({total_order}%) exceeds 100%. Please re-enter.")
                    continue
                ripe = 100 - total_order
                break
            except ValueError:
                print("invalid input, Please enter a number for percentages.")
        print("\n==== Quality ====")
        longStalk = int(input("Long stalk: "))
        stamp = int(input("stamp: "))
        
        ripeness_data = {
            "unRipe": unRipe,
            "underRipe": underRipe,
            "ripe": ripe,
            "overRipe": overRipe,
            "emptyFruit": emptyFruit,
            "rotten": rotten,
            "longStalk": longStalk,
            "stamp": stamp
        }
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        day_of_week = now.strftime("%A")
        
        grade = {
            "date": date_time_str,
            "day": day_of_week,
            "estate": estate,
            "division": division,
            "block": block,
            "noMobil": noMobil,
            "ripeness": ripeness_data
        }
        
        grading.append(grade)
        print("Grading data added sucessfully")
        return grading
    else:
        print("invalid input. Please enter 'y' or 'n': ")
        return grading
        
def show_grading(grading):
    if not grading: # Checks if the list is empty (more pythonic then len(grading) <= 0):
        print("Your grading list is empty.")
        return
    print("\n===== Your Grading Records =====")
    for i, grade_entry in enumerate(grading, start=1):
        print(f"\nRecord {i}.")
        print(f" Date: {grade_entry.get('date', 'N/A')}")
        print(f" Day: {grade_entry.get('day', 'N/A')}")
        print(f" Estate: {grade_entry.get('estate', 'N/A')}")
        print(f" Division: {grade_entry.get('division', 'N/A')}")
        print(f" Block: {grade_entry.get('block', 'N/A')}")
        print(f" Plate Number: {grade_entry.get('noMobil', 'N/A')}")
        
        ripeness = grade_entry.get("ripeness")
        if ripeness and isinstance(ripeness, dict):
            print("ripeness Details:")
            print(f" Unripe: {ripeness.get('unRipe', 'N/A')}%")
            print(f" Under ripe: {ripeness.get('underRipe', 'N/A')}%")
            print(f" Ripe: {ripeness.get('ripe', 'N/A')}%")
            print(f" Over ripe: {ripeness.get('overRipe', 'N/A')}%")
            print(f" Empty Fruit: {ripeness.get('emptyFruit', 'N/A')}%")
            print(f" Rotten: {ripeness.get('rotten', 'N/A')}%")
            print(f" Long stalk : {ripeness.get('longStalk', 'N/A')}%")
            print(f" Stamp: {ripeness.get('stamp', 'N/A')}%")
        else:
            print("ripeness details not available")
            
def edit_grading(grading):
    if not grading:
        print("Your grading is empty. Nothing to edit.")
        return grading
    show_grading(grading)
    while True:
        try:
            record_index =int(intput("Enter the record number you want to edit (or ) ot cancel: "))
            if record_index == 0:
                print("Edit cancelled.")
                return grading 
            if 1 <= record_index <= len(grading):
                break
            else:
                print("invalid record number. Please enter a number within the displayed range.")
        except ValueError:
            print('invalid input. Please enter a number.')
            
        grade_to_edit = grading[record_index -1]
        print(f"\n === Editing Record {record_index} ===")
        print(f"Date(cannot be edited): {grade_to_edit.get('date', 'N/A')}")
        print(f"Day(cannot be edited): {grade_to_edit.get('day', 'N/A')}")
        
            
               
            
            
        
        
        
        

if __name__== "__main__":
    print("starting the Fresh Fruit Bunches Grading Application") 
    intro()
    db = read_json("database_grading.json")
    user = None
    while user is None:
        login_or_register = input("Do you want to 'login' or 'register': "). lower()
        if login_or_register == 'login':
            user = login(db)
        elif login_or_register == 'register':
            user = register(db)
        else: 
            print('invalid input. Please type "login" or "register".')
            
    while True: 
        main_menu()
        user_choice = get_user_input_menu_choice()
        match user_choice:
            case 1:
                add_grading(user['grading']) # di sini bermasalah 'grading' di def login return db[username]
                save_json('database_grading.json', db)
            case 2:
                show_grading(user['grading'])
                print("show grading")
            case 3: 
                print("edit grading")
            case 4: 
                print("delete grading")
            case 5:
                print("delete all grading")
            case 6:
                print("Exit program. Goodbye! ")
                break
                
                
