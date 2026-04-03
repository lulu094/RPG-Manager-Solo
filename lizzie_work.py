# Lizzie's File for Code

import time
import random

delay = 0.06

characters = []

def type_print(string):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ---------------- INVENTORY HELPER ----------------

def adding_removing(thing):
    while True:
        type_print(f"Are you adding or removing {thing}?\n")
        a_r = input("Enter ADDING or REMOVING: ").strip().upper()

        if a_r in ["ADDING", "REMOVING"]:
            return a_r
        else:
            print("Invalid input. Try again.")


def check_valid_num(num):
    if num.isdigit():
        return True
    print("Please enter a valid whole number.")
    return False


# ---------------- FIND CHARACTER ----------------

def find_character(future_action):
    while True:
        type_print(f"\nHow would you like to find your character for {future_action}?\n1) Name\n2) Class\n3) Level\n")
        find = input("Choice: ").strip()

        if find == "1":
            name = input("Enter name: ").strip().title()
            type_print(f"\nMatches for '{name}':")
            for c in characters:
                if name in c["Name"]:
                    print(c["Name"])
            return

        elif find == "2":
            class_name = input("Enter class: ").strip().title()
            type_print(f"\nMatches for class '{class_name}':")
            for c in characters:
                if class_name in c["Class"]:
                    print(f"{c['Name']} - {c['Class']}")
            return

        elif find == "3":
            level = input("Enter level: ").strip()
            if not level.isdigit():
                print("Invalid level.")
                continue

            level = int(level)
            type_print(f"\nCharacters with level {level}:")
            for c in characters:
                if c["Level"] == level:
                    print(f"{c['Name']} - Level {c['Level']}")
            return

        else:
            print("Invalid input.")


# ---------------- VIEW CHARACTER ----------------

def view_character():
    if not characters:
        type_print("No characters found. Create one first.\n")
        return

    find_character("viewing")

    name = input("\nType full character name to view: ").strip().title()

    for c in characters:
        if c["Name"] == name:
            type_print(f"""
Viewing Character:
Name: {c['Name']}
Class: {c['Class']}
Strength: {c['Stats']['Strength']}
Health: {c['Stats']['Health']}
Wisdom: {c['Stats']['Wisdom']}
Dexterity: {c['Stats']['Dexterity']}
Intelligence: {c['Stats']['Intelligence']}
XP: {c['XP']}
Level: {c['Level']}
Weapon: {c['Weapon']}
Inventory: {c['Inventory']}
""")
            return

    print("Character not found.")


# ---------------- EDIT CHARACTER ----------------

def edit_character():
    if not characters:
        type_print("No characters found. Create one first.\n")
        return

    find_character("editing")

    name = input("\nType full character name to edit: ").strip().title()

    for c in characters:
        if c["Name"] == name:

            while True:
                type_print("""
What would you like to edit?
1) XP
2) Reroll Stat
3) Inventory
4) Exit
""")

                action = input("Choice: ").strip()

                # -------- XP --------
                if action == "1":
                    while True:
                        xp = input("Enter XP amount: ")
                        if check_valid_num(xp):
                            xp = int(xp)
                            break

                    choice = adding_removing("XP")

                    if choice == "ADDING":
                        c["XP"] += xp
                    else:
                        c["XP"] -= xp

                    print(f"XP is now {c['XP']}")

                # -------- REROLL STAT --------
                elif action == "2":
                    type_print("Which stat? Strength / Health / Wisdom / Dexterity / Intelligence")
                    stat = input("Stat: ").title()

                    if stat in c["Stats"]:
                        new_val = random.randint(10, 30)
                        c["Stats"][stat] = new_val
                        print(f"{stat} is now {new_val}")
                    else:
                        print("Invalid stat.")

                # -------- INVENTORY --------
                elif action == "3":
                    item = input("Item name: ").strip().title()
                    choice = adding_removing("inventory")

                    if choice == "ADDING":
                        c["Inventory"].append(item)
                    else:
                        if item in c["Inventory"]:
                            c["Inventory"].remove(item)
                        else:
                            print("Item not found.")

                # -------- EXIT --------
                elif action == "4":
                    return

                else:
                    print("Invalid option.")

            return

    print("Character not found.")



type_print("\nTesting View Character\n")
view_character()

type_print("\nTesting Edit Character\n")
edit_character()