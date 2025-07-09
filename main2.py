import json
from datetime import datetime # Import the datetime module

def intro():
    print("\n===================================================")
    print("+++ FRESH FRUIT BUNCHES GRADING APPLICATION POM 2 +++")
    print("===================================================\n")

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"'{filename}' not found. Creating a new database.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'. Starting with an empty database.")
        return {}

def save_json(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=4) # Use indent for pretty printing JSON

def login(db):
    username = input("Username: ")
    password = input("Password: ")
    if username in db and db[username]['password'] == password:
        print(f"Welcome back, {username}!")
        return db[username]
    else:
        raise ValueError("Invalid username or password. Please try again or register.")

def register(db):
    while True:
        username = input("Enter new username: ")
        if username in db:
            print("Username already exists. Please choose a different username.")
            continue
        password_1 = input("Enter password: ")
        password_2 = input("Confirm password: ")
        if password_1 == password_2:
            db[username] = {'name': username, 'password': password_1, 'grading': []}
            save_json('database_grading.json', db)
            print(f"User '{username}' registered successfully!")
            return db[username]
        else:
            print("Passwords do not match. Please try again.")

def main_menu():
    print("\n================================================")
    print("MAIN MENU")
    main_menu_options = ('Add Grading', 'See Grading', 'Edit Grading', 'Delete Grading', 'Delete All Grading', 'Exit Program')
    for i, m in enumerate(main_menu_options, start=1):
        print(f"{i}. {m}")
    print("================================================\n")

def get_user_input_menu_choice():
    while True:
        try:
            user_input = int(input("Select an item from the main menu: "))
            if 1 <= user_input <= 6:
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_grading(grading):
    input_choice = input("Do you want to add grading? (y/n): ").lower()
    if input_choice == "n":
        return grading
    elif input_choice == 'y':
        estate = input("Estate: ")
        division = input("Division: ")
        block = input("Block: ")
        noMobil = input("Plate number: ")
        
        kematangan_data = {}
        while True:
            try:
                unRipe = int(input("Unripe percentage (0-100): "))
                halfRipe = int(input("Half Ripe percentage (0-100): "))
                overRipe = int(input("Over ripe percentage (0-100): "))
                emptyFruit = int(input("Empty fruit percentage (0-100): "))
                rotten = int(input("Rotten percentage (0-100): "))
                
                if not all(0 <= p <= 100 for p in [unRipe, halfRipe, overRipe, emptyFruit, rotten]):
                    print("All percentages must be between 0 and 100. Please try again.")
                    continue
                
                total_other = unRipe + halfRipe + overRipe + emptyFruit + rotten
                if total_other > 100:
                    print(f"The sum of unripe, half ripe, over ripe, empty fruit, and rotten ({total_other}%) exceeds 100%. Please re-enter.")
                    continue
                
                ripe = 100 - total_other
                break
            except ValueError:
                print("Invalid input. Please enter a number for percentages.")

        print("\n--- Quality ---")
        longStalk = input("Long Stalk (e.g., 'yes'/'no' or quantity): ")
        stamp = input("Stamp (e.g., 'yes'/'no' or type): ")
        
        kematangan_data = {
            "unRipe": unRipe,
            "halfRipe": halfRipe,
            "ripe": ripe,
            "overRipe": overRipe,
            "emptyFruit": emptyFruit,
            "rotten": rotten,
            "longStalk": longStalk,
            "stamp": stamp
        }
        
        # Get current date and time
        now = datetime.now()
        # Format the date and time as a string for storage
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S") 
        day_of_week = now.strftime("%A") # Get the full weekday name

        grade = {
            "date": date_time_str,      # Add date and time
            "day": day_of_week,         # Add day of the week
            "estate": estate,
            "division": division,
            "block": block,
            "noMobil": noMobil,
            "kematangan": kematangan_data
        }
        grading.append(grade)
        print("Grading data added successfully!")
        return grading
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return grading

def see_grading(grading):
    if not grading:
        print("Your grading list is empty.")
        return

    print("\n--- Your Grading Records ---")
    for i, grade_entry in enumerate(grading, start=1):
        print(f"\nRecord {i}:")
        print(f"  Date: {grade_entry.get('date', 'N/A')}") # Display date
        print(f"  Day: {grade_entry.get('day', 'N/A')}")   # Display day
        print(f"  Estate: {grade_entry.get('estate', 'N/A')}")
        print(f"  Division: {grade_entry.get('division', 'N/A')}")
        print(f"  Block: {grade_entry.get('block', 'N/A')}")
        print(f"  Plate Number: {grade_entry.get('noMobil', 'N/A')}")
        
        kematangan = grade_entry.get('kematangan')
        if kematangan and isinstance(kematangan, dict):
            print("  Kematangan Details:")
            print(f"    Unripe: {kematangan.get('unRipe', 'N/A')}%")
            print(f"    Half Ripe: {kematangan.get('halfRipe', 'N/A')}%")
            print(f"    Ripe: {kematangan.get('ripe', 'N/A')}%")
            print(f"    Over Ripe: {kematangan.get('overRipe', 'N/A')}%")
            print(f"    Empty Fruit: {kematangan.get('emptyFruit', 'N/A')}%")
            print(f"    Rotten: {kematangan.get('rotten', 'N/A')}%")
            print(f"    Long Stalk: {kematangan.get('longStalk', 'N/A')}")
            print(f"    Stamp: {kematangan.get('stamp', 'N/A')}")
        else:
            print("  Kematangan details not available.")

def edit_grading(grading):
    if not grading:
        print("Your grading list is empty. Nothing to edit.")
        return

    see_grading(grading) # Show existing gradings to the user
    while True:
        try:
            record_index = int(input("Enter the record number you want to edit (or 0 to cancel): "))
            if record_index == 0:
                print("Edit cancelled.")
                return grading
            if 1 <= record_index <= len(grading):
                break
            else:
                print("Invalid record number. Please enter a number within the displayed range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    grade_to_edit = grading[record_index - 1]
    print(f"\n--- Editing Record {record_index} ---")
    
    # You might not want to edit the date and day directly, 
    # as they represent when the record was *created*. 
    # If you need to record an 'updated_at' timestamp, you could add another field.
    print(f"  Date (cannot be edited): {grade_to_edit.get('date', 'N/A')}")
    print(f"  Day (cannot be edited): {grade_to_edit.get('day', 'N/A')}")

    grade_to_edit['estate'] = input(f"Estate (current: {grade_to_edit.get('estate', 'N/A')}): ") or grade_to_edit.get('estate', 'N/A')
    grade_to_edit['division'] = input(f"Division (current: {grade_to_edit.get('division', 'N/A')}): ") or grade_to_edit.get('division', 'N/A')
    grade_to_edit['block'] = input(f"Block (current: {grade_to_edit.get('block', 'N/A')}): ") or grade_to_edit.get('block', 'N/A')
    grade_to_edit['noMobil'] = input(f"Plate number (current: {grade_to_edit.get('noMobil', 'N/A')}): ") or grade_to_edit.get('noMobil', 'N/A')

    kematangan = grade_to_edit.get('kematangan', {})
    print("\n--- Editing Kematangan Details ---")
    while True:
        try:
            unRipe = int(input(f"Unripe percentage (current: {kematangan.get('unRipe', 'N/A')}): ") or kematangan.get('unRipe', 0))
            halfRipe = int(input(f"Half Ripe percentage (current: {kematangan.get('halfRipe', 'N/A')}): ") or kematangan.get('halfRipe', 0))
            overRipe = int(input(f"Over ripe percentage (current: {kematangan.get('overRipe', 'N/A')}): ") or kematangan.get('overRipe', 0))
            emptyFruit = int(input(f"Empty fruit percentage (current: {kematangan.get('emptyFruit', 'N/A')}): ") or kematangan.get('emptyFruit', 0))
            rotten = int(input(f"Rotten percentage (current: {kematangan.get('rotten', 'N/A')}): ") or kematangan.get('rotten', 0))

            if not all(0 <= p <= 100 for p in [unRipe, halfRipe, overRipe, emptyFruit, rotten]):
                print("All percentages must be between 0 and 100. Please try again.")
                continue
            
            total_other = unRipe + halfRipe + overRipe + emptyFruit + rotten
            if total_other > 100:
                print(f"The sum of unripe, half ripe, over ripe, empty fruit, and rotten ({total_other}%) exceeds 100%. Please re-enter.")
                continue
            
            ripe = 100 - total_other
            break
        except ValueError:
            print("Invalid input. Please enter a number for percentages.")

    kematangan['unRipe'] = unRipe
    kematangan['halfRipe'] = halfRipe
    kematangan['overRipe'] = overRipe
    kematangan['emptyFruit'] = emptyFruit
    kematangan['rotten'] = rotten
    kematangan['ripe'] = ripe

    kematangan['longStalk'] = input(f"Long Stalk (current: {kematangan.get('longStalk', 'N/A')}): ") or kematangan.get('longStalk', 'N/A')
    kematangan['stamp'] = input(f"Stamp (current: {kematangan.get('stamp', 'N/A')}): ") or kematangan.get('stamp', 'N/A')

    grade_to_edit['kematangan'] = kematangan
    print("Grading record updated successfully!")
    return grading

def delete_grading(grading):
    if not grading:
        print("Your grading list is empty. Nothing to delete.")
        return

    see_grading(grading) # Show existing gradings to the user
    while True:
        try:
            record_index = int(input("Enter the record number you want to delete (or 0 to cancel): "))
            if record_index == 0:
                print("Delete cancelled.")
                return grading
            if 1 <= record_index <= len(grading):
                confirm = input(f"Are you sure you want to delete record {record_index}? (y/n): ").lower()
                if confirm == 'y':
                    deleted_grade = grading.pop(record_index - 1)
                    print(f"Record {record_index} (Plate Number: {deleted_grade.get('noMobil', 'N/A')}) deleted successfully!")
                else:
                    print("Delete cancelled.")
                return grading
            else:
                print("Invalid record number. Please enter a number within the displayed range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def delete_all_grading(grading):
    if not grading:
        print("Your grading list is already empty.")
        return

    confirm = input("Are you absolutely sure you want to delete ALL grading records? This action cannot be undone! (y/N): ").lower()
    if confirm == 'y':
        grading.clear()
        print("All grading records have been deleted.")
    else:
        print("Deletion of all grading records cancelled.")
    return grading

if __name__ == "__main__":
    db = read_json("database_grading.json") 
    intro()
    user = None
    
    while user is None:
        login_or_register = input('Do you want to "login" or "register"? ').lower()
        if login_or_register == "login":
            try:
                user = login(db)
            except ValueError as e:
                print(e)
        elif login_or_register == "register":
            user = register(db)
        else:
            print('Invalid input. Please type "login" or "register".')

    while True:
        main_menu()
        user_choice = get_user_input_menu_choice()
        
        if user_choice == 1:
            user['grading'] = add_grading(user['grading'])
            save_json("database_grading.json", db) # Save after adding
        elif user_choice == 2:
            see_grading(user['grading'])
        elif user_choice == 3: 
            user['grading'] = edit_grading(user['grading'])
            save_json("database_grading.json", db) # Save after editing
        elif user_choice == 4: 
            user['grading'] = delete_grading(user['grading'])
            save_json("database_grading.json", db) # Save after deleting
        elif user_choice == 5: 
            user['grading'] = delete_all_grading(user['grading'])
            save_json("database_grading.json", db) # Save after deleting all
        elif user_choice == 6:
            print("Exiting program. Goodbye!")
            break # Exit the while True loop