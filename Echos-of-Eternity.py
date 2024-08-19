#Echos of Eternity

#imports
import time
import os
import random

#constants
player_1 = {
    "state": None,
    "level": 1,
    "xp":0,
    "money": 0,
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
    "state": None,
    "level": 1,
    "xp":0,
    "money": 0,
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