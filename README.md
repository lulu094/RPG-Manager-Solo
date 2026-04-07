# RPG Upgraded Manager Project
LV 1st RPG Upgraded Project


## Overview

This Python program is a simple RPG character manager that allows users to create and manage characters, assign classes, edit stats, and view character data. It also includes a dashboard system that shows statistics and graphs for all characters.

The program allows the user to:
- Create RPG characters (Fighter, Rogue, Cleric)
- Assign weapons, stats, and skills
- View character information
- Edit XP, inventory, and stats
- Level up characters using an XP system
- View a dashboard with statistics and graphs
- Compare characters using visual charts


## Project Structure

- main_file.py → Main program that runs the RPG system and menu  
- dashboard.py → Handles statistics and dashboard system  
- visualization.py → Handles graphs and charts using matplotlib  
- README.md → Project description  

## How It Works

1. Create Character
Users select a class and create a character. Each character includes:
- Name (random or manual using Faker)
- Weapon selection
- Random stats
- Skills based on class

2. View Characters
Displays all created characters including:
- Level
- XP
- Stats
- Inventory
- Skills

3. Edit Character
Users can:
- Add or remove XP
- Add or remove inventory items
- Reroll stats

Characters can level up when XP reaches the required amount.

4. Level System
When XP reaches a threshold:
- Character levels up
- Stats increase automatically

5. Dashboard
The dashboard displays:
- Total number of characters
- Class distribution
- Level statistics
- Overall summaries

6. Visualization
Graphs include:
- Bar chart of character levels
- Radar chart of stats
- Class comparison charts

## Concepts Used

- Object-Oriented Programming (OOP)
- Classes and objects
- Sets (inventory and skills)
- Random module and Faker library
- Loops and conditionals
- Data analysis with pandas
- Data visualization with matplotlib
- Menu-driven program design

## How to Run

1. Install Python  
2. Open terminal in project folder  
3. Install required libraries:
    - pip install matplotlib pandas faker

## Requirements

Make sure you install:

matplotlib
pandas
faker

## Author
lulu094