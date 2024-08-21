#Echos of Eternity

#imports
import time
import os
import random

#constants
player_1 = {
    "name": "player 1",
    "state": None,
    "level": 1,
    "xp":0,
    "money": 0,
    "species": "",
    "class": "",
    #player stats
    "strength": 0, "speed": 0,"health max":0, "health":0, "stamina max":0, "stamina":0, "mana max":0, "mana":0,
    #inventory: {wpn name:[sprite/img/symbol], qty, dmg, price}
    "inventory": {
        "kratos": ['✠', 0, 0, 0], 
        "knights Sword": ['🗡', 0, 0, 0], 
        "biezelbub": ['⬤', 0, 0, 0], 
        "zues": ['ϟ', 0, 0, 0], 
        "andromeda":['❃', 0, 0, 0]
    },
    "equip": {
        "weapon": "",
        "moves": []
    }
}

player_2 = {
    "name": "player 2",
    "state": None,
    "level": 1,
    "xp":0,
    "money": 0,
    "species": "",
    "class": "",
    #player stats
    "strength": 0, "speed": 0,"health max":0, "health":0, "stamina max":0, "stamina":0, "mana max":0, "mana":0,
    #inventory: {wpn name:[sprite/img/symbol], qty, dmg, price}, max size is 50
    "inventory": {
        "kratos": ['✠', 0, 0, 'God Slayer', 'Spinning Axe', 0], 
        "knights Sword": ['🗡', 0, 0, 'Dark Blade', 0], 
        "biezelbub": ['⬤', 0, 0, 0], 
        "zues": ['ϟ', 0, 0, 0], 
        "andromeda":['❃', 0, 0, 0]
    },
    "equip": {
        "weapon": "",
        "moves": []
    }
}

active = player_1
other = player_2

def species_select(active):
    global player_1, player_2
    while active["species"] == "":
        os.system('cls')
        print("select the name of the species from the following: ")
        print("1. Human \n2. Dragon \n3. Shifter \n4. Druid")
        print("\nto veiw information about the species type 'info- <name of the species>'")
        choice = input(">>>").strip().lower()
        os.system('cls')
        back = "this is a place holder"
        if choice == "info- human":
            print("lore will be added")
            back = input("to go back to selecting your species, press enter or type 'yes'\n>>>>").strip().lower()
        elif choice == "info- dragon":
            print("lore will be added")
            back = input("to go back to selecting your species, press enter or type 'yes'\n>>>>").strip().lower()
        elif choice == "info- shifter":
            print("lore will be added")
            back = input("to go back to selecting your species, press enter or type 'yes'\n>>>>").strip().lower()
        elif choice == "info- druid":
            print("lore will be added")
            back = input("to go back to selecting your species, press enter or type 'yes'\n>>>>").strip().lower()
        if back == "" or back == "yes":
            continue
        else:
            if choice not in ["human", "dragon", "shifter", "druid"]:
                print("it seems that you didnt enter the name propely, please eneter it again correctly")
                time.sleep(2)
                continue
            else:
                active["species"] = choice
                break

def menu(active):
    #this is the starting menue
    if active["species"] == "":        
        species_select(active)
menu(active)