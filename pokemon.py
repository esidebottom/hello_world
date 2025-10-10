pikachu = {
    "name": "Pikachu",
    "type": "Electric",
    "Level": 25,
    "HP": 60,
    "Attack": 55,
    "Defense": 40,
    "Speed": 90,
    "Moves": ["Thunder Shock", "Quick Attack", "Electro Ball", "Iron Tail"],
    "Evolves From": "Pichu",
    "Evolves To": "Raichu"
    }
charmander = {
    "name": "Charmander",
    "type": "Fire",
    "Level": 15,
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Speed": 65,
    "Moves": ["Scratch", "Ember", "Smokescreen", "Dragon Rage"],
    "Evolves From": None,
    "Evolves To": "Charmeleon"
    }
ThunderShock = {
    "name": "Thunder Shock",
    "type": "Electric",
    "category": "Special",
    "power": 40,
    "accuracy": 100,
    "PP": 30,
    "effect": "May paralyze the target"
    }
Ember = {
    "name": "Ember",
    "type": "Fire",
    "category": "Special",
    "power": 40,
    "accuracy": 100,
    "PP": 25,
    "effect": "May burn the target"
    }
scratch = {
    "name": "Scratch",
    "type": "Normal",
    "category": "Physical",
    "power": 40,
    "accuracy": 100,
    "PP": 35,
    "effect": "No additional effect"
    }
quick_attack = {
    "name": "Quick Attack",
    "type": "Normal",
    "category": "Physical",
    "power": 40,
    "accuracy": 100,
    "PP": 30,
    "effect": "Always goes first"
    }
electro_ball = {
    "name": "Electro Ball",
    "type": "Electric",
    "category": "Special",
    "power": "Varies",
    "accuracy": 100,
    "PP": 10,
    "effect": "Power increases with user's Speed"
    }
iron_tail = {
    "name": "Iron Tail",
    "type": "Steel",
    "category": "Physical",
    "power": 100,
    "accuracy": 75,
    "PP": 15,
    "effect": "May lower the target's Defense"
}
smokescreen = {
    "name": "Smokescreen",
    "type": "Normal",
    "category": "Status",
    "power": 0,
    "accuracy": 100,
    "PP": 20,
    "effect": "Lowers the target's accuracy"
    }
dragon_rage = {
    "name": "Dragon Rage",
    "type": "Dragon",
    "category": "Special",
    "power": 0,
    "accuracy": 100,
    "PP": 10,
    "effect": "Always inflicts 40 HP damage"
    }
def fight(attacker, defender, move):
    defender["HP"]=defender["HP"]-move["power"]
    if defender["HP"]<0:
        defender["HP"]=0
        print(defender["name"],"fainted!")
fight(pikachu,charmander,ThunderShock)
print(charmander["HP"])