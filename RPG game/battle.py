import random
import time

#User------------------------------------------------------------

# User Stats
selfHealth = {"level": "1", "Health": 100} # je krijgt meer health als je meer stats points in deze stat zet
selfAttack = {"level": "1", "bonusAttack": 0} # je krijgt meer attack bonus (meer damage) als je meer stats points in deze stat zet
selfLuck = {"level": "1", "dodgeChance": 0.0, "critChance": 0.05} # de user krijgt meer dodge kans en crit kans al deze stat wordt verhoogd
# punten voor de user
statPoints = 0 
# Attacks (user)
slash = {"naam": "Slash", "schade": 25}
# xp van de user
userXP = 0
# user progress levels
XPlvl1  = {"level": 1,   "XPneeded": 250,   "actief": True} # level 1 is actief doordat je begint met level 1
XPlvl2  = {"level": 2,   "XPneeded": 500,   "actief": False}
XPlvl3  = {"level": 3,   "XPneeded": 750,   "actief": False}
XPlvl4  = {"level": 4,   "XPneeded": 1250,  "actief": False}
XPlvl5  = {"level": 5,   "XPneeded": 2000,  "actief": False}
XPlvl6  = {"level": 6,   "XPneeded": 3000,  "actief": False}
XPlvl7  = {"level": 7,   "XPneeded": 5500,  "actief": False}
XPlvl8  = {"level": 8,   "XPneeded": 7500,  "actief": False}
XPlvl9  = {"level": 9,   "XPneeded": 10000, "actief": False}
XPlvl10 = {"level": 10,  "XPneeded": 0,     "actief": False} # max level nu tijdelijk

#User------------------------------------------------------------


#enemy's---------------------------------------------------------

#orc-------------------------------------------------------------
# orc stats
orcMaxHealth = 135
# orc attacks
brawl   = {"naam": "Brawl",   "schade": 35}
rage   = {"naam": "Rage",   "buff": 10, "debuff": 15, "actief": False,} # buff that gives the orc damage buff but reduces his hp for 3 rounds
tear   = {"naam": "Tear",   "schade": 15, "poison": 5, "actief": False,} # inficts a posion that does more every time (3 rounds)
# orc Xp
orcXp = 75
# lvl buff spit
def update_brawl():
    if XPlvl1["actief"] == True:
        brawl["schade"] = 35
    elif XPlvl2["actief"] == True:
        brawl["schade"] = 40
    elif XPlvl3["actief"] == True:
        brawl["schade"] = 45
    elif XPlvl4["actief"] == True:
        brawl["schade"] = 50
    elif XPlvl5["actief"] == True:
        brawl["schade"] = 55
    elif XPlvl6["actief"] == True:
        brawl["schade"] = 60
    elif XPlvl7["actief"] == True:
        brawl["schade"] = 65
    elif XPlvl8["actief"] == True:
        brawl["schade"] = 70
    elif XPlvl9["actief"] == True:
        brawl["schade"] = 75
    elif XPlvl10["actief"] == True:
        brawl["schade"] = 80

# lvl buff spit
def update_rage():
    if XPlvl1["actief"] == True:
        rage["buff"] = 10
        rage["debuff"] = 15
    elif XPlvl2["actief"] == True:
        rage["buff"] = 15
        rage["debuff"] = 20
    elif XPlvl3["actief"] == True:
        rage["buff"] = 20
        rage["debuff"] = 25
    elif XPlvl4["actief"] == True:
        rage["buff"] = 30
        rage["debuff"] = 30
    elif XPlvl5["actief"] == True:
        rage["buff"] = 35
        rage["debuff"] = 35
    elif XPlvl6["actief"] == True:
        rage["buff"] = 40
        rage["debuff"] = 40
    elif XPlvl7["actief"] == True:
        rage["buff"] = 45
        rage["debuff"] = 40
    elif XPlvl8["actief"] == True:
        rage["buff"] = 50
        rage["debuff"] = 45
    elif XPlvl9["actief"] == True:
        rage["buff"] = 55
        rage["debuff"] = 45
    elif XPlvl10["actief"] == True:
        rage["buff"] = 60
        rage["debuff"] = 50

# lvl buff spit
def update_tear():
    if XPlvl1["actief"] == True:
        tear["schade"] = 15
        tear["poison"] = 5
    elif XPlvl2["actief"] == True:
        tear["schade"] = 20
        tear["poison"] = 5
    elif XPlvl3["actief"] == True:
        tear["schade"] = 25
        tear["poison"] = 10
    elif XPlvl4["actief"] == True:
        tear["schade"] = 35
        tear["poison"] = 10
    elif XPlvl5["actief"] == True:
        tear["schade"] = 40
        tear["poison"] = 15
    elif XPlvl6["actief"] == True:
        tear["schade"] = 45
        tear["poison"] = 15
    elif XPlvl7["actief"] == True:
        tear["schade"] = 50
        tear["poison"] = 20
    elif XPlvl8["actief"] == True:
        tear["schade"] = 55
        tear["poison"] = 20
    elif XPlvl9["actief"] == True:
        tear["schade"] = 55
        tear["poison"] = 20
    elif XPlvl10["actief"] == True:
        tear["schade"] = 60
        tear["poison"] = 25

# lvl buff orc
def update_orcHealth():
    global orcMaxHealth
    if XPlvl1["actief"] == True:
        orcMaxHealth = 135
    elif XPlvl2["actief"] == True:
        orcMaxHealth = 145
    elif XPlvl3["actief"] == True:
        orcMaxHealth = 155
    elif XPlvl4["actief"] == True:
        orcMaxHealth = 165
    elif XPlvl5["actief"] == True:
        orcMaxHealth = 175
    elif XPlvl6["actief"] == True:
        orcMaxHealth = 185
    elif XPlvl7["actief"] == True:
        orcMaxHealth = 195
    elif XPlvl8["actief"] == True:
        orcMaxHealth = 200
    elif XPlvl9["actief"] == True:
        orcMaxHealth = 200
    elif XPlvl10["actief"] == True:
        orcMaxHealth = 200

#round trigger
roundCounter = 0
def round_checker():
    global orcMaxHealth, orcHealth
    if roundCounter == 1:
        if tear["actief"] == True:
            selfHealth - tear["poison"]
        elif rage["actief"] == True:
            brawl["schade"] + rage["buff"]
            tear["schade"] + rage["buff"]
            tear["poison"] + rage["buff"]
            orcHealth - rage["debuff"]
        
            

#orc-------------------------------------------------------------


#slime-----------------------------------------------------------
# slime stats
slimeMaxHealth = 35
# slime attacks
spit   = {"naam": "Spit",   "schade": 10}
absorb = {"naam": "Absorb", "reductie": 0.1}
# slime Xp
slimeXp = 250

# lvl buff spit
def update_spit():
    if XPlvl1["actief"] == True:
        spit["schade"] = 10
    elif XPlvl2["actief"] == True:
        spit["schade"] = 15
    elif XPlvl3["actief"] == True:
        spit["schade"] = 20
    elif XPlvl4["actief"] == True:
        spit["schade"] = 30
    elif XPlvl5["actief"] == True:
        spit["schade"] = 35
    elif XPlvl6["actief"] == True:
        spit["schade"] = 40
    elif XPlvl7["actief"] == True:
        spit["schade"] = 45
    elif XPlvl8["actief"] == True:
        spit["schade"] = 50
    elif XPlvl9["actief"] == True:
        spit["schade"] = 55
    elif XPlvl10["actief"] == True:
        spit["schade"] = 60

# lvl buff absorb
def update_absorb():
    if XPlvl1["actief"] == True:
        absorb["reductie"] = 0.1
    elif XPlvl2["actief"] == True:
        absorb["reductie"] = 0.125
    elif XPlvl3["actief"] == True:
        absorb["reductie"] = 0.15
    elif XPlvl4["actief"] == True:
        absorb["reductie"] = 0.2
    elif XPlvl5["actief"] == True:
        absorb["reductie"] = 0.25
    elif XPlvl6["actief"] == True:
        absorb["reductie"] = 0.3
    elif XPlvl7["actief"] == True:
        absorb["reductie"] = 0.35
    elif XPlvl8["actief"] == True:
        absorb["reductie"] = 0.4
    elif XPlvl9["actief"] == True:
        absorb["reductie"] = 0.45
    elif XPlvl10["actief"] == True:
        absorb["reductie"] = 0.5

# lvl buff slime health
def update_slimeHealth():
    global slimeMaxHealth
    if XPlvl1["actief"] == True:
        slimeMaxHealth = 35
    elif XPlvl2["actief"] == True:
        slimeMaxHealth = 45
    elif XPlvl3["actief"] == True:
        slimeMaxHealth = 55
    elif XPlvl4["actief"] == True:
        slimeMaxHealth = 65
    elif XPlvl5["actief"] == True:
        slimeMaxHealth = 75
    elif XPlvl6["actief"] == True:
        slimeMaxHealth = 85
    elif XPlvl7["actief"] == True:
        slimeMaxHealth = 95
    elif XPlvl8["actief"] == True:
        slimeMaxHealth = 100
    elif XPlvl9["actief"] == True:
        slimeMaxHealth = 100
    elif XPlvl10["actief"] == True:
        slimeMaxHealth = 100
#slime-----------------------------------------------------------

#enemy's---------------------------------------------------------

# Xp needed for showing
def XP_needed():
    if XPlvl1["actief"] == True:
        return XPlvl1["XPneeded"] - userXP
    elif XPlvl2["actief"] == True:
        return XPlvl2["XPneeded"] - userXP
    elif XPlvl3["actief"] == True:
        return XPlvl3["XPneeded"] - userXP
    elif XPlvl4["actief"] == True:
        return XPlvl4["XPneeded"] - userXP
    elif XPlvl5["actief"] == True:
        return XPlvl5["XPneeded"] - userXP
    elif XPlvl6["actief"] == True:
        return XPlvl6["XPneeded"] - userXP
    elif XPlvl7["actief"] == True:
        return XPlvl7["XPneeded"] - userXP
    elif XPlvl8["actief"] == True:
        return XPlvl8["XPneeded"] - userXP
    elif XPlvl9["actief"] == True:
        return XPlvl9["XPneeded"] - userXP
    elif XPlvl10["actief"] == True:
        return XPlvl10["XPneeded"] - userXP

# level up systeem
def check_level_up():
    global statPoints, userXP # maakt de statpoint global en userXP
    if userXP >= XPlvl1["XPneeded"] and XPlvl1["actief"] == True:
        XPlvl1["actief"] = False
        XPlvl2["actief"] = True
        statPoints += 5 # door de global werkt +=
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 2!")

    elif userXP >= XPlvl2["XPneeded"] and XPlvl2["actief"] == True:
        XPlvl2["actief"] = False
        XPlvl3["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 3!")

    elif userXP >= XPlvl3["XPneeded"] and XPlvl3["actief"] == True:
        XPlvl3["actief"] = False
        XPlvl4["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 4!")

    elif userXP >= XPlvl4["XPneeded"] and XPlvl4["actief"] == True:
        XPlvl4["actief"] = False
        XPlvl5["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 5!")

    elif userXP >= XPlvl5["XPneeded"] and XPlvl5["actief"] == True:
        XPlvl5["actief"] = False
        XPlvl6["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 6!")

    elif userXP >= XPlvl6["XPneeded"] and XPlvl6["actief"] == True:
        XPlvl6["actief"] = False
        XPlvl7["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 7!")

    elif userXP >= XPlvl7["XPneeded"] and XPlvl7["actief"] == True:
        XPlvl7["actief"] = False
        XPlvl8["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 8!")

    elif userXP >= XPlvl8["XPneeded"] and XPlvl8["actief"] == True:
        XPlvl8["actief"] = False
        XPlvl9["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 9!")

    elif userXP >= XPlvl9["XPneeded"] and XPlvl9["actief"] == True:
        XPlvl9["actief"] = False
        XPlvl10["actief"] = True
        statPoints += 5
        update_spit()
        update_absorb()
        print("Level up! Je bent nu level 10!")

# aanval keuze
def vraag_aanval(attack):
    keuze = input(f"Which attack do you wanna use? {attack['naam']} ({attack['schade']}): ")
    return keuze.lower()

# keuze menu
def vraag_menu():
    keuzeMenu = input("Where do you wanna go? W (Front), A (Left), S (Back), D (Right), Menu, Profile (stats), Items: ")
    return keuzeMenu.lower()

# Profile menu
def profile_menu():
    profileMenu = input("") # dit moetnog toegevoegt worden en alles moet logic zijn 
    return profileMenu.lower()

# absorb
def absorb_schade(schade):
    verminderd = schade * absorb["reductie"]
    nieuwe_schade = schade - verminderd
    return round(nieuwe_schade)

# random nummer
def random_number():
    while True:
        # Combineer twee willekeurige getallen op een betekenisvolle manier
        random_I = random.randint(1, 11)
        random_II = random.randint(1, 11)

        # Neem het gemiddelde en voeg wat ruis toe
        random_newNumber = (random_I + random_II) / 2 + random.uniform(-1, 1)

        if 1 <= random_newNumber <= 11:
            return round(random_newNumber)
        else:
            continue

# random monster nummer
def random_monster():
    while True:
        # Combineer twee willekeurige getallen op een betekenisvolle manier
        random_l = random.randint(1, 101)
        random_ll = random.randint(1, 101)

        # Neem het gemiddelde en voeg wat ruis toe
        random_newMonster = (random_l + random_ll) / 2 + random.uniform(-1, 1)

        if 1 <= random_newMonster <= 101:
            return round(random_newMonster)
        else:
            continue

slimeBattle = False

#GameLogic--------------------------------------------------------
# slime battle
def slime_battle():
    if slimeBattle == True:
        global slimeMaxHealth, slimeHealth, slime_absorb_actief, selfHealth, userXP
        print("A slime appeared!")
        slimeHealth = slimeMaxHealth  # reset de hp van de slime
        slime_absorb_actief = False  # reset per gevecht
        while True:
            print(f"Slime Health({slimeHealth})")
            # speler beurt
            gekozen = vraag_aanval(slash)
            check_quit(gekozen)

            if gekozen == "slash":
                kans = random_number()

                if slime_absorb_actief:
                    aangepaste_schade = absorb_schade(slash["schade"])  # -10%
                    slime_absorb_actief = False
                else:
                    aangepaste_schade = slash["schade"]  # normaal 25

                if kans <= 8:
                    slimeHealth -= aangepaste_schade
                    print(f"Slash hit! Slime HP: {slimeHealth}")
                    time.sleep(1)

                elif kans > 9:
                    print("Your attack was dodged!")
                    time.sleep(1)

            # slime dood?
            if slimeHealth <= 0:
                userXP += slimeXp
                print("You defeated the slime!")
                check_level_up()
                print(f"You gained {slimeXp}XP, you need {XP_needed()} to level up and you have statpoints({statPoints}) to use!")
                break

            # slime beurt
            slimeAttackKans = random_number()

            if slimeAttackKans <= 6:
                attackKans = random_number()

                if attackKans <= 6:
                    selfHealth["Health"] -= spit["schade"]
                    print(f"Slime used Spit! Your HP: {selfHealth['Health']}")
                    time.sleep(1)

                elif attackKans > 6:
                    print("The slime missed!")
                    time.sleep(1)

            elif slimeAttackKans > 6:
                slime_absorb_actief = True  # maakt de absorb actief voor 1 beurd/continue
                print("Slime used Absorb! Your next attack does less damage.")
                time.sleep(1)

            # speler dood?
            if selfHealth["Health"] <= 0:
                print("You were defeated...")
                break
#orc battle

#GameLogic--------------------------------------------------------

#Admin------------------------------------------------------------

# special def admin fuctions
def check_quit(keuze):
    if keuze == "Quit".lower():
        print("Quitting...")
        time.sleep(0.5)
        quit()

#Admin------------------------------------------------------------

#Game------------------------------------------------------------
while True:
    print("Searching for enemy...")
    time.sleep(1)
    encounter = random_monster()

    if encounter <= 40:
        slimeBattle = True
        slime_battle()
        slimeBattle = False
    elif encounter > 60:
        print("Nothing found...")
        time.sleep(1)
        continue
#Game------------------------------------------------------------