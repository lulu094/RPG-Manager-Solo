# LV, TE, LD 1st RPG

import random
import time
import os


# GLOBAL STYLE REPLACED WITH CLASS WRAPPER 
class RPG:

    def __init__(self):
        self.classes = {
            1: {
                "Name": "Fighter",
                "Weapons": ("Greatsword", "Greataxe", "Maul"),  # TUPLE
                "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}
            },
            2: {
                "Name": "Rogue",
                "Weapons": ("Daggers", "Blowgun", "Knives"),  # TUPLE
                "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}
            },
            3: {
                "Name": "Cleric",
                "Weapons": ("Mace", "Warhammer", "Morning Star"),  # TUPLE
                "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}
            }
        }

        self.characters = []

        # SET 
        self.skill_pool = {"Slash", "Block", "Heal", "Stealth"}

    # ORIGINAL STYLE FUNCTION 
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def type_print(self, string, delay=0.06):
        for char in string:
            print(char, end="", flush=True)
            time.sleep(delay)

    # CLOSURE FUNCTION 
    def xp_needed_factory(self, class_name):
        def xp_needed(level):
            if class_name in ["Fighter", "Rogue"]:
                return level * 15
            return level * 20
        return xp_needed

    # MENU 
    def menu(self):
        self.clear_screen()
        while True:
            print("\nMain Menu")
            print("1. View Character")
            print("2. Create Character")
            print("3. Edit Character")
            print("4. Exit")

            menu_option = input("Select an option (1-4): ")

            if menu_option == "1":
                self.view_character()
            elif menu_option == "2":
                self.create_character()
            elif menu_option == "3":
                self.edit_character()
            elif menu_option == "4":
                self.type_print("Goodbye adventurer!\n")
                break
            else:
                print("Invalid option.")

    # CREATE CHARACTER 
    def create_character(self):

        def another_character():
            while True:
                another = input("Create another character? (yes/no): ").strip().lower()
                if another != "yes":
                    return
                else:
                    self.create_character()

        print("\nCreate Character")

        print("\n1. Fighter")
        print("2. Rogue")
        print("3. Cleric")

        try:
            c_class = int(input("Enter class number: "))
        except ValueError:
            return

        if c_class not in self.classes:
            print("Invalid class.")
            return

        base = self.classes[c_class]

        # SET USAGE
        character = {
            "Name": input("Name: ").title().strip(),
            "Class": base["Name"],
            "Weapon": None,
            "Inventory": set(),   # SET
            "Skills": set(),      # SET
            "XP": 0,
            "Level": 1,
            "Stats": base["Stats"].copy()
        }

        # random extra stats (same style as yours)
        character["Stats"]["Dexterity"] = random.randint(10, 30)
        character["Stats"]["Intelligence"] = random.randint(10, 30)

        print("\nChoose weapon:")
        for i, w in enumerate(base["Weapons"], 1):
            print(f"{i}. {w}")

        try:
            weapon_choice = int(input("> "))
            character["Weapon"] = base["Weapons"][weapon_choice - 1]
        except:
            print("Invalid weapon.")
            return

        # SET OPERATIONS (RUBRIC)
        character["Skills"].update(random.sample(list(self.skill_pool), 2))

        self.characters.append(character)

        self.type_print(f"\nCharacter created: {character['Name']}\n")

        another_character()

    # FIND CHARACTER
    def find_character(self, future_action):

        while True:
            self.type_print(f"\nHow would you like to find character for {future_action}?\n")
            print("1) Name\n2) Class\n3) Level")

            find = input("> ").strip()

            if find == "1":
                name = input("Name: ").lower()
                return [c for c in self.characters if name in c["Name"].lower()]

            elif find == "2":
                cls = input("Class: ").title()
                return [c for c in self.characters if c["Class"] == cls]

            elif find == "3":
                level = input("Level: ")
                if level.isdigit():
                    level = int(level)
                    return [c for c in self.characters if c["Level"] == level]

            else:
                print("Invalid input.")

    # VIEW CHARACTER 
    def view_character(self):

        if not self.characters:
            self.type_print("No characters found.\n")
            return

        results = self.find_character("viewing")

        if not results:
            print("No matches found.")
            return

        for chara in results:
            self.type_print(f"""
Viewing Character:
Name: {chara['Name']}
Class: {chara['Class']}
Weapon: {chara['Weapon']}
Level: {chara['Level']}
XP: {chara['XP']}
Stats: {chara['Stats']}
Inventory: {list(chara['Inventory'])}
Skills: {list(chara['Skills'])}
""")

    # LEVEL SYSTEM 
    def level_up(self, character):

        xp_func = self.xp_needed_factory(character["Class"])
        needed = xp_func(character["Level"])

        if character["XP"] >= needed:
            character["XP"] -= needed
            character["Level"] += 1
            character["Stats"]["Strength"] += 1
            character["Stats"]["Health"] += 1
            print(f"{character['Name']} leveled up!")

    # EDIT CHARACTER 
    def edit_character(self):

        results = self.find_character("editing")

        if not results:
            print("No character found.")
            return

        chara = results[0]

        # INNER FUNCTION (RUBRIC)
        def adding_removing(item_type):
            while True:
                ans = input(f"Adding or removing {item_type}? ").strip().upper()
                if ans in ["ADDING", "REMOVING"]:
                    return ans
                print("Invalid input.")

        def check_number(num):
            return num.isdigit()

        def edit_menu():
            print("\n1) XP")
            print("2) Reroll Stat")
            print("3) Inventory")
            return input("> ")

        choice = edit_menu()

        if choice == "1":
            mode = adding_removing("XP")

            xp = input("Amount: ")
            if check_number(xp):
                xp = int(xp)

                if mode == "ADDING":
                    chara["XP"] += xp
                else:
                    chara["XP"] -= xp

                self.level_up(chara)

        elif choice == "2":
            stat = input("Stat: ").title()
            if stat in chara["Stats"]:
                chara["Stats"][stat] = random.randint(10, 30)

        elif choice == "3":
            mode = adding_removing("inventory")

            item = input("Item: ").title()

            if mode == "ADDING":
                chara["Inventory"].add(item)
            else:
                chara["Inventory"].discard(item)


menu()