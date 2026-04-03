# New Upgraded RPG

import time
import random
import sys
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt


characters 0 [ ]
fake = Faker()

class RandomGenerator:
    def random_name(self):
        return fake.name()

    def random_backstory(self):
        return fake.sentence(nb_words=20)
# ---------------- TYPE PRINT ----------------

delay = 0.06


class DataVisualization:
    def bar_chart(self, character):
        stats = character.stats
        names = list(stats.keys())
        values = list(stats.values())

        plt.bar(names, values)
        plt.title(character.name + " Stats")
        plt.show()

def type_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class StatisticalAnalyzer:
    def analyze(self, df):
        return {
            "mean": df.mean(numeric_only=True),
            "max": df.max(numeric_only=True),
            "min": df.min(numeric_only=True),
            "median": df.median(numeric_only=True)
        }

def to_dataframe():
    data = []
    for c in characters:
        data.append({
            "Name": c.name,
            "Class": c.char_class,
            "Strength": c.stats["Strength"],
            "Health": c.stats["Health"],
            "Wisdom": c.stats["Wisdom"],
            "XP": c.xp,
            "Level": c.level
        })
    return pd.DataFrame(data)

# ---------------- GLOBAL STORAGE ----------------

class Character:
    def __init__(self, name, char_class, stats, weapon):
        self.name = name
        self.char_class = char_class
        self.stats = stats
        self.weapon = weapon
        self.xp = 0
        self.level = 1
        self.inventory = []

# ---------------- CLASS SYSTEM ----------------

classes = {
    1: {"Name": "Fighter",
        "Weapons": ["Greatsword", "Greataxe", "Maul"],
        "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},

    2: {"Name": "Rogue",
        "Weapons": ["Daggers", "Blowgun", "Knives"],
        "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},

    3: {"Name": "Cleric",
        "Weapons": ["Mace", "Warhammer", "Morning Star"],
        "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}
}


# ---------------- HELPERS ----------------

def adding_removing(thing):
    while True:
        type_print(f"Are you adding or removing {thing}?")
        choice = input("ADDING / REMOVING: ").strip().upper()
        if choice in ["ADDING", "REMOVING"]:
            return choice
        print("Invalid input.")


def check_valid_num(num):
    return num.isdigit()


def find_character():
    type_print("\nSearch by:\n1) Name\n2) Class\n3) Level")
    choice = input("Choice: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip().title()
        for c in characters:
            if name in c["Name"]:
                print(c["Name"])

    elif choice == "2":
        cls = input("Enter class: ").strip().title()
        for c in characters:
            if cls in c["Class"]:
                print(f"{c['Name']} - {c['Class']}")

    elif choice == "3":
        lvl = input("Enter level: ").strip()
        if lvl.isdigit():
            lvl = int(lvl)
            for c in characters:
                if c["Level"] == lvl:
                    print(f"{c['Name']} - Level {lvl}")


# ---------------- CREATE CHARACTER ----------------

def create_character():
    type_print("\nChoose a class:")

    for key, value in classes.items():
        print(f"{key}) {value['Name']} - {value['Stats']}")

    try:
        choice = int(input("Class number: "))
    except:
        print("Invalid input.")
        return

    if choice not in classes:
        print("Invalid class.")
        return

    base = classes[choice]

    character = {
        "Name": input("Enter name: ").strip().title(),
        "Class": base["Name"],
        "Stats": base["Stats"].copy(),
        "Weapon": None,
        "Inventory": [],
        "XP": 0,
        "Level": 1
    }

    # random stats
    character["Stats"]["Dexterity"] = random.randint(10, 30)
    character["Stats"]["Intelligence"] = random.randint(10, 30)

    # weapon selection
    print("\nChoose weapon:")
    for i, w in enumerate(base["Weapons"], 1):
        print(f"{i}) {w}")

    while True:
        w = input("Weapon number: ")
        if w.isdigit() and 1 <= int(w) <= len(base["Weapons"]):
            character["Weapon"] = base["Weapons"][int(w) - 1]
            break

    characters.append(character)

    type_print("\nCharacter created successfully!")


# ---------------- VIEW ----------------

def view_character():
    if not characters:
        print("No characters.")
        return

    find_character()

    name = input("\nEnter full name to view: ").strip().title()

    for c in characters:
    if name in c.name:
        type_print(f"""
Name: {c.name}
Class: {c.char_class}
Strength: {c.stats['Strength']}
Health: {c.stats['Health']}
Wisdom: {c.stats['Wisdom']}
Dexterity: {c.stats['Dexterity']}
Intelligence: {c.stats['Intelligence']}
XP: {c.xp}
Level: {c.level}
Weapon: {c.weapon}
Inventory: {c.inventory}
""")
        return


# ---------------- EDIT ----------------

def edit_character():
    if not characters:
        print("No characters.")
        return

    find_character()

    name = input("\nEnter full name to edit: ").strip().title()

    for c in characters:
        if c["Name"] == name:

            while True:
                type_print("""
1) Add XP
2) Reroll Stat
3) Inventory
4) Exit
""")

                choice = input("Choice: ")

                # XP
                if choice == "1":
                    xp = input("XP amount: ")
                    if xp.isdigit():
                        xp = int(xp)
                        mode = adding_removing("XP")

                        if mode == "ADDING":
                            c.xp   
                        else:
                            c["XP"] -= xp

                        print("XP updated:", c["XP"])

                # stats
                elif choice == "2":
                    stat = input("Stat (Strength/Health/Wisdom/Dexterity/Intelligence): ").title()
                    if stat in c["Stats"]:
                        c["Stats"][stat] = random.randint(10, 30)
                        print(stat, "updated!")

                # inventory
                elif choice == "3":
                    item = input("Item name: ").title()
                    mode = adding_removing("inventory")

                    if mode == "ADDING":
                        c["Inventory"].append(item)
                    else:
                        if item in c["Inventory"]:
                            c["Inventory"].remove(item)

                elif choice == "4":
                    return

    print("Character not found.")


# ---------------- MAIN MENU ----------------

def main():
    while True:
        type_print("""
--- MAIN MENU ---
1) Create Character
2) View Character
3) Edit Character
4) Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            create_character()
        elif choice == "2":
            view_character()
        elif choice == "3":
            edit_character()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


# ---------------- RUN PROGRAM ----------------

main()