#TE 2nd Character Creator
import random
import sys
import time

def slow_print(text, delay=0.1):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

classes = { 
1 : {"Name": "Fighter", "Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},
2 : {"Name": "Rogue", "Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},
3 : {"Name": "Cleric", "Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}
}

characters = []

def create_character():

    for key, value in classes.items():
        print(f"{key}: {value['Name']}:{value['Stats']}")

    try:
        c_class = int(input("Enter the number of your class choice: "))
    except ValueError:
        print("Invalid input.")
        return

    if c_class not in classes:
        print("Invalid class choice.")
        return       

    base_class = classes[c_class]

    character = {
        "Class": base_class["Name"],
        "Stats": base_class["Stats"].copy(),
        "Weapon": None
    }

    slow_print("You have two empty stats.")
    print("Rolling for your stats...")  

    character["Stats"]["Dexterity"] = random.randint(10, 30)
    character["Stats"]["Intelligence"] = random.randint(10, 30)

    slow_print(f"Dexterity: {character['Stats']['Dexterity']}, Intelligence: {character['Stats']['Intelligence']}")

    print("Choose your weapon:")
    for i, weapon in enumerate(base_class["Weapons"], 1):
        print(f"{i}: {weapon}")

    # ✅ FIXED INDENTATION (THIS MUST BE INSIDE FUNCTION)
    while True:
        try:
            weapon_choice = int(input("Enter weapon number: "))
            if 1 <= weapon_choice <= len(base_class["Weapons"]):
                character["Weapon"] = base_class["Weapons"][weapon_choice - 1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a valid number.")

    # ✅ FIX: MISSING VALUES
    character["XP"] = 0
    character["Level"] = 1
    character["Inventory"] = []
    character["Spell_slots"] = 0

    character["Name"] = input("Enter your character's name: ").strip().title()

    characters.append(character)
    slow_print(f"Character created:\nName: {character['Name']}\n Class: {character['Class']}\n Stats:\n Strength: {character['Stats']['Strength']}\n Health: {character['Stats']['Health']}\n Wisdom: {character['Stats']['Wisdom']}\n Dexterity: {character['Stats']['Dexterity']}\n Intelligence: {character['Stats']['Intelligence']}\n XP: {character['XP']}\n Level: {character['Level']}\n Weapon: {character['Weapon']}")
"""def main():
    #Main program loop
    while True:
        create_character()
        another = input("Create another? (yes/no): ")
        if another.lower() != 'yes':
            break
main()"""


main()