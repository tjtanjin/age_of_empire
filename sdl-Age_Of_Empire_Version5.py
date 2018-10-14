"""
Create a Turn Based Strategy Game "Age of Empire". Ccplayers play as Egyptians against the Greeks.
Each round, they are given 3 options explained below:
Attack: Sum up attack of all available units and attack the castle, might fail or succeed.
        If the attack is successful, some gold will be plundered and enemy castle will lose health. There may or may not be allied casualties.
        If the attack is unsuccessful, there is a higher rate of allied casualties.
Repair: 3 options to repair castle at 100 gold, 200 gold and 300 gold.
Hire: Hire more units to increase attack strength. Knight has lower death rate than warrior and warrior has lower death rate than soldier.
Egyptians and Greeks will take turns until one of their castle health hits 0. Have fun!
"""
import random
import time
#-Empire class-
class Empire():
    def __init__(self, name):
        self.name = name #name of the empire
        self.castle_health = {'castle_health': 2000} #starting castle health (also the max)
        self.gold = {'amount': 900} #starting gold (no max, increases by 100 every turn)
        self.soldier = {'price': 20, 'num': 30, 'attack': 5, 'armor': 5, 'desc': "A light infantry unit with weak attack"} #soldier properties
        self.warrior = {'price': 50, 'num': 15, 'attack': 10, 'armor': 7, 'desc': "A toughened soldier with moderate attack"} #warrior properties
        self.knight = {'price': 100, 'num': 5, 'attack': 20, 'armor': 10, 'desc': "A heavily armored unit with strong attack"} #knight properties
#-controller function-    
def controller(cplayer, nplayer, gamemode_choice):
    """
    Checks the value of playerturn() and computerturn() functions to regulate turns between player and player or player and computer.
    When false, the turn continues to alternate. When true, the game is won and end() function is called.
    Args:
        cplayer: current player
        nplayer: next player
        gamemode_choice: 1 or 2 (Player VS Player or Player VS AI)
    """
    while True:
        if gamemode_choice == 1:
            while playerturn(cplayer, nplayer) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
            while playerturn(nplayer, cplayer) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
        elif gamemode_choice == 2:
            while playerturn(cplayer, nplayer) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
            while computerturn(cplayer, nplayer, gamemode_choice) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
        elif gamemode_choice == 3:
            while computerturn(nplayer, cplayer, gamemode_choice) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
            while computerturn(cplayer, nplayer, gamemode_choice) == True:
                break
            if cplayer.castle_health['castle_health'] == 0 or nplayer.castle_health['castle_health'] == 0:
                end(cplayer, nplayer, gamemode_choice)
                break
#-playerturn function-
def playerturn(cplayer, nplayer):
    """
    Executes during player's turn.
    Args:
        cplayer: current player
        nplayer: next player
    """
    cplayer.gold['amount'] = cplayer.gold['amount'] + 100 #plus 100 gold at every start of turn
    #player's main display at the beginning of his/her turn
    print("-----------Castle-----------")
    print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
    print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
    print("-----------Income-----------")
    print("Gold: %r | +100 Every Turn" % cplayer.gold['amount'])
    print("-----------Units------------")
    print("Soldier(s): %r" % cplayer.soldier['num'])
    print("Warrior(s): %r" % cplayer.warrior['num'])
    print("Knight(s): %r" % cplayer.knight['num'])
    print("----------------------------")
    print("What will the %r do?\n1. Attack\n2. Repair\n3. Hire Troops" % cplayer.name)
    #end of player's main display, start of options
    while True:
        cplayer_choice = input("> ").upper()
        #player attack option
        if cplayer_choice == "1" or cplayer_choice == "A":
            cplayer_attack_strength = cplayer.soldier['attack'] * cplayer.soldier['num'] + cplayer.warrior['attack'] * cplayer.warrior['num'] + cplayer.knight['attack'] * cplayer.knight['num'] #summing up for attack strength
            print("Preparing Forces...")
            time.sleep(2) #simulate loading time
            print("Attack Strength: %r" % cplayer_attack_strength)
            print("Launching Attack...")
            time.sleep(5) #simulate loading time #simulate loading time
            luck = random.randint(1,10) #determine 70/30 success/failure of attack
            if luck < 8: #execute if attack successful
                nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] - cplayer_attack_strength #subtract defending castle's health
                if nplayer.castle_health['castle_health'] < 0: #ensure castle health cannot be negative
                    nplayer.castle_health['castle_health'] = 0
                s_luck = random.randint(0, cplayer.soldier['num']//4) #randomly give casualty to the attacker
                w_luck = random.randint(0, cplayer.warrior['num']//6) #randomly give casualty to the attacker
                k_luck = random.randint(0, cplayer.knight['num']//8) #randomly give casualty to the attacker
                g_luck = random.randint(100,200) #randomly loot gold
                cplayer.soldier['num'] = cplayer.soldier['num'] - s_luck #subtract casualty from initial amount
                cplayer.warrior['num'] = cplayer.warrior['num'] - w_luck #subtract casualty from initial amount
                cplayer.knight['num'] = cplayer.knight['num'] - k_luck #subtract casualty from initial amount
                cplayer.gold['amount'] = cplayer.gold['amount'] + g_luck #add gold to attacker
                nplayer.gold['amount'] = nplayer.gold['amount'] - g_luck #subtract gold from defender
                if nplayer.gold['amount'] < 0: #ensure gold cannot be negative
                    disparity = -(nplayer.gold['amount'])
                    nplayer.gold['amount'] = 0
                    cplayer.gold['amount'] = cplayer.gold['amount'] - disparity #ensure no "overloot"
                    print("The attack was a success! You plundered all their gold!")
                if nplayer.gold['amount'] > 0:
                    print("The attack was a success! You plundered %r gold!" % g_luck)
                print("%r Castle took %r damage!" % (nplayer.name, cplayer_attack_strength))
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                break
            else: #execute if attack failed
                s_luck = random.randint(0, cplayer.soldier['num']//3) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                w_luck = random.randint(0, cplayer.warrior['num']//4) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                k_luck = random.randint(0, cplayer.knight['num']//6) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                cplayer.soldier['num'] = cplayer.soldier['num'] - s_luck #subtract casualty from initial amount
                cplayer.warrior['num'] = cplayer.warrior['num'] - w_luck #subtract casualty from initial amount
                cplayer.knight['num'] = cplayer.knight['num'] - k_luck #subtract casualty from initial amount
                print("The attack was repelled!")
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                break
        #player repair option
        elif (cplayer_choice == "2" or cplayer_choice == "R") and cplayer.gold['amount'] >= 100: #ensure enough gold for minimal repair
            while True:
                #3 options to repair castle health
                print("How much do you wish to repair?\n1. 100 Health (Cost 100 Gold)\n2. 200 Health (Cost 200 Gold)\n3. 300 Health (Cost 300 Gold)")
                cplayer_repair = input("> ")
                if (cplayer_repair == "1" or cplayer_repair == "100") and cplayer.gold['amount'] >= 100: #repair 100 health
                    repair = 100
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 100
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 100 #subtract 100 gold
                    break
                elif (cplayer_repair == "2" or cplayer_repair == "200") and cplayer.gold['amount'] >= 200: #repair 200 health
                    repair = 200
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 200
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 200 #subtract 200 gold
                    break
                elif (cplayer_repair == "3" or cplayer_repair == "300") and cplayer.gold['amount'] >= 300: #repair 300 health
                    repair = 300
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 300
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 300 #subtract 300 gold
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            if cplayer.castle_health['castle_health'] > 2000: #ensure castle health does not exceed max health, set castle health to max and refund gold if so
                gold_refund = cplayer.castle_health['castle_health'] - 2000
                cplayer.castle_health['castle_health'] = 2000
                cplayer.gold['amount'] = cplayer.gold['amount'] + gold_refund
                print("%r Castle already at full health! Extra %r gold returned!" % (cplayer.name, gold_refund))
            elif cplayer.castle_health['castle_health'] <= 2000:
                print("Repairing Castle...")
                time.sleep(5) #simulate loading time
                print("The %r Castle has repaired %r health!" % (cplayer.name, repair))
            break
        #player repair option but not enough gold
        elif (cplayer_choice == "2" or cplayer_choice == "R") and cplayer.gold['amount'] < 100:
            print("Not enough gold to repair! Choose another option!")
        #player hire option
        elif (cplayer_choice == "3" or cplayer_choice == "H") and cplayer.gold['amount'] >= cplayer.soldier['price']: #ensure enough gold for minimal hire
            while True:
                #3 hire options
                print("Which unit do you wish to hire?")
                print("1. Soldier - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.soldier['price'], cplayer.soldier['attack'], cplayer.soldier['armor'], cplayer.soldier['desc']))
                print("2. Warrior - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.warrior['price'], cplayer.warrior['attack'], cplayer.warrior['armor'], cplayer.warrior['desc']))
                print("3. Knight - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.knight['price'], cplayer.knight['attack'], cplayer.knight['armor'], cplayer.knight['desc']))
                cplayer_hire = input("> ")
                if (cplayer_hire == "1" or cplayer_hire == "S") and cplayer.gold['amount'] >= cplayer.soldier['price']: #ensure enough gold for at least 1 soldier
                    while True:
                        print("How many Soldiers do you want to hire?")
                        s_hire = input("> ")
                        if s_hire.isdigit() and int(s_hire) > 0 and int(s_hire)*cplayer.soldier['price'] <= cplayer.gold['amount']: #ensure enough gold for stated amount of soldier
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.soldier['num'] = cplayer.soldier['num'] + int(s_hire) #Add soldier once hire is successful
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(s_hire)*cplayer.soldier['price'] #Subtract hire price
                    print("Hiring Soldiers...")
                    time.sleep(5) #simulate loading time
                    print("%r Soldiers hired!" % int(s_hire))
                    break
                elif (cplayer_hire == "2" or cplayer_hire == "W") and cplayer.gold['amount'] >= cplayer.warrior['price']: #ensure enough gold for at least 1 warrior
                    while True:
                        print("How many Warriors do you want to hire?")
                        w_hire = input("> ")
                        if w_hire.isdigit() and int(w_hire) > 0 and int(w_hire)*cplayer.warrior['price'] <= cplayer.gold['amount']: #ensure enough gold for stated amount of warrior
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.warrior['num'] = cplayer.warrior['num'] + int(w_hire) #Add warrior once hire is successful
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(w_hire)*cplayer.warrior['price'] #Subtract hire price
                    print("Hiring Warriors...")
                    time.sleep(5) #simulate loading time
                    print("%r Warriors hired!" % int(w_hire))
                    break
                elif (cplayer_hire == "3" or cplayer_hire == "300") and cplayer.gold['amount'] >= cplayer.knight['price']: #ensure enough gold for at least 1 knight
                    while True:
                        print("How many Knights do you want to hire?")
                        k_hire = input("> ")
                        if k_hire.isdigit() and int(k_hire) > 0 and int(k_hire)*cplayer.knight['price'] <= cplayer.gold['amount']: #ensure enough gold for stated amount of knight
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.knight['num'] = cplayer.knight['num'] + int(k_hire) #Add knight once hire is successful
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(k_hire)*cplayer.knight['price'] #Subtract hire price
                    print("Hiring Knights...")
                    time.sleep(5) #simulate loading time
                    print("%r Knights hired!" % int(k_hire))
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            break
        #player hire option but not enough gold
        elif cplayer_choice == "3" or cplayer_choice == "H" and cplayer.gold < 20:
            print("Not enough gold to hire! Choose another option!")
        #for all other invalid options
        else:
            print("Please choose a valid option!")
    #at the end of an executed decision, print updated player display and call up next player's turn
    print("-----------Castle-----------")
    print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
    print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
    print("-----------Income-----------")
    print("Gold: %r | +100 Every Turn" % cplayer.gold['amount'])
    print("-----------Units------------")
    print("Soldier(s): %r" % cplayer.soldier['num'])
    print("Warrior(s): %r" % cplayer.warrior['num'])
    print("Knight(s): %r" % cplayer.knight['num'])
    print("----------------------------")
    if nplayer.castle_health['castle_health'] == 0: #end game if castle health is 0
        return True
    elif nplayer.castle_health['castle_health'] > 0: #change turn if castle health is greater than 0
        return False
#-computerturn function-
def computerturn(cplayer, nplayer, gamemode_choice):
    """
    Executes only in AI gamemode and during AI's turn.
    """
    nplayer.gold['amount'] = nplayer.gold['amount'] + 100 #plus 100 gold at every start of turn
    if gamemode_choice == 3: #print AI display if in AI vs AI mode
        print("-----------Castle-----------")
        print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
        print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
        print("-----------Income-----------")
        print("Gold: %r | +100 Every Turn" % nplayer.gold['amount'])
        print("-----------Units------------")
        print("Soldier(s): %r" % nplayer.soldier['num'])
        print("Warrior(s): %r" % nplayer.warrior['num'])
        print("Knight(s): %r" % nplayer.knight['num'])
        print("----------------------------")
    print("The %r are considering their move..." % nplayer.name)
    time.sleep(3) #simulate loading time
    while True:
        #strength and health used to give the AI some "intelligence":
        #if castle health below 650, chances of AI repairing is higher
        #if attack strength is below 320, chance of AI hiring is higher
        if nplayer.soldier['attack'] * nplayer.soldier['num'] + nplayer.warrior['attack'] * nplayer.warrior['num'] + nplayer.knight['attack'] * nplayer.knight['num'] > 320:
            strength = 4
        else:
            strength = 5
        if nplayer.castle_health['castle_health'] > 650:
            health = 1
        else:
            health = 0
        nplayer_choice = random.randint(health,strength)
        #computer attack option
        if nplayer_choice == 2 or nplayer_choice == 3:
            nplayer_attack_strength = nplayer.soldier['attack'] * nplayer.soldier['num'] + nplayer.warrior['attack'] * nplayer.warrior['num'] + nplayer.knight['attack'] * nplayer.knight['num']
            print("The %r decided to launch an attack!" % nplayer.name)
            print("%r Attack Strength: %r" % (nplayer.name, nplayer_attack_strength))
            print("%r launching Attack..." % nplayer.name)
            time.sleep(5) #simulate loading time
            luck = random.randint(1,10)
            if luck < 8:
                cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] - nplayer_attack_strength
                if cplayer.castle_health['castle_health'] < 0: #ensure castle health cannot be negative
                    cplayer.castle_health['castle_health'] = 0
                s_luck = random.randint(0, nplayer.soldier['num']//4) #randomly give casualty to the attacker
                w_luck = random.randint(0, nplayer.warrior['num']//6) #randomly give casualty to the attacker
                k_luck = random.randint(0, nplayer.knight['num']//8) #randomly give casualty to the attacker
                g_luck = random.randint(100,200)
                nplayer.soldier['num'] = nplayer.soldier['num'] - s_luck #subtract casualty from initial amount
                nplayer.warrior['num'] = nplayer.warrior['num'] - w_luck #subtract casualty from initial amount
                nplayer.knight['num'] = nplayer.knight['num'] - k_luck #subtract casualty from initial amount
                cplayer.gold['amount'] = cplayer.gold['amount'] - g_luck #subtract gold from defender
                nplayer.gold['amount'] = nplayer.gold['amount'] + g_luck #add gold to attacker
                if cplayer.gold['amount'] < 0: #ensure gold cannot be negative
                    disparity = -(cplayer.gold['amount'])
                    cplayer.gold['amount'] = 0
                    nplayer.gold['amount'] = nplayer.gold['amount'] - disparity #ensure no "overloot"
                    print("The %r attack was a success! They plundered all the gold!" % nplayer.name)
                if cplayer.gold['amount'] > 0:
                    print("The %r attack was a success! They plundered %r gold!" % (nplayer.name, g_luck))
                print("%r Castle took %r damage!" % (cplayer.name, nplayer_attack_strength))
                print("The %r army lost %r soldiers, %r warriors and %r knights in their attack!" % (nplayer.name, s_luck, w_luck, k_luck))
                break
            else:
                s_luck = random.randint(0, nplayer.soldier['num']//3) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                w_luck = random.randint(0, nplayer.warrior['num']//4) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                k_luck = random.randint(0, nplayer.knight['num']//6) #randomly give casualty to the attacker (Higher casualty rate than successful attack)
                nplayer.soldier['num'] = nplayer.soldier['num'] - s_luck #subtract casualty from initial amount
                nplayer.warrior['num'] = nplayer.warrior['num'] - w_luck #subtract casualty from initial amount
                nplayer.knight['num'] = nplayer.knight['num'] - k_luck #subtract casualty from initial amount
                print("The attack was repelled!")
                print("The %r army lost %r soldiers, %r warriors and %r knights in their attack!" % (nplayer.name, s_luck, w_luck, k_luck))
                break
        #computer repair option
        elif (nplayer_choice == 1 and nplayer.gold['amount'] >= 100 and nplayer.castle_health['castle_health'] < 2000) or (nplayer_choice == 0 and nplayer.gold['amount'] >= 100 and nplayer.castle_health['castle_health'] < 2000): #ensure enough gold for minimal repair
            while True:
                #3 repair options, randomized
                nplayer_repair = random.randint(1,3)
                if nplayer_repair == 1 and nplayer.gold['amount'] >= 100: #repair 100 health
                    repair = 100
                    nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 100
                    nplayer.gold['amount'] = nplayer.gold['amount'] - 100 #subtract 100 gold
                    break
                elif nplayer_repair == 2 and nplayer.gold['amount'] >= 200: #repair 200 health
                    repair = 200
                    nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 200
                    nplayer.gold['amount'] = nplayer.gold['amount'] - 200 #subtract 200 gold
                    break
                elif nplayer_repair == 3 and nplayer.gold['amount'] >= 300: #repair 300 health
                    repair = 300
                    nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 300
                    nplayer.gold['amount'] = nplayer.gold['amount'] - 300 #subtract 300 gold
                    break
                else:
                    continue
            if nplayer.castle_health['castle_health'] > 2000: #ensure castle health does not exceed max health, set castle health to max and refund gold if so
                gold_refund = nplayer.castle_health['castle_health'] - 2000
                nplayer.castle_health['castle_health'] = 2000
                nplayer.gold['amount'] = nplayer.gold['amount'] + gold_refund
                print("%r Castle already at full health! Extra %r gold returned!" % (nplayer.name, gold_refund))
            elif nplayer.castle_health['castle_health'] <= 2000:
                print("%r repairing Castle..." % nplayer.name)
                time.sleep(5) #simulate loading time
                print("The %r Castle has repaired %r health!" % (nplayer.name, repair))
            break
        #computer hire option
        elif (nplayer_choice == 4 and nplayer.gold['amount'] >= 100) or (nplayer_choice == 5 and nplayer.gold['amount'] >= 100) : #ensure enough gold for minimal hire of 100 gold worth of soldiers (purposely to make AI hire more)
            while True:
                #3 hire options, randomized
                nplayer_hire = random.randint(1,3)
                if nplayer_hire == 1 and nplayer.gold['amount'] >= nplayer.soldier['price']: #ensure enough gold for at least 1 soldier
                    while True:
                        s_hire = random.randint(5,20)
                        if int(s_hire)*nplayer.soldier['price'] <= nplayer.gold['amount']: #ensure enough gold for randomized amount of soldier, else reroll
                            break
                        else:
                            continue
                    nplayer.soldier['num'] = nplayer.soldier['num'] + int(s_hire) #Add soldier once hire is successful
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(s_hire)*nplayer.soldier['price'] #Subtract hire price
                    break
                elif nplayer_hire == 2 and nplayer.gold['amount'] >= nplayer.warrior['price']: #ensure enough gold for at least 1 warrior
                    while True:
                        w_hire = random.randint(2,8)
                        if int(w_hire)*nplayer.warrior['price'] <= nplayer.gold['amount']: #ensure enough gold for randomized amount of warrior, else reroll                            break
                            break
                        else:
                            continue
                    nplayer.warrior['num'] = nplayer.warrior['num'] + int(w_hire) #Add warrior once hire is successful
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(w_hire)*nplayer.warrior['price'] #Subtract hire price
                    break
                elif nplayer_hire == 3 and nplayer.gold['amount'] >= nplayer.knight['price']: #ensure enough gold for at least 1 knight
                    while True:
                        k_hire = random.randint(1,4)
                        if int(k_hire)*nplayer.knight['price'] <= nplayer.gold['amount']: #ensure enough gold for randomized amount of knight, else reroll
                            break
                        else:
                            continue
                    nplayer.knight['num'] = nplayer.knight['num'] + int(k_hire) #Add knight once hire is successful
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(k_hire)*nplayer.knight['price'] #Subtract hire price
                    break
                else:
                    continue
            print("%r hiring units..." % nplayer.name)
            time.sleep(5) #simulate loading time
            if nplayer_hire == 1:
                print("The %r have hired %r soldiers!" % (nplayer.name, s_hire))
            elif nplayer_hire == 2:
                print("The %r have hired %r warriors!" % (nplayer.name, w_hire))
            elif nplayer_hire == 3:
                print("The %r have hired %r knights!" % (nplayer.name, k_hire))
            break
        #if an option fails to execute, randomize for another option
        else:
            continue
    if cplayer.castle_health['castle_health'] == 0 and (gamemode_choice == 2): #end game and print final player display if castle health is 0 (player vs AI mode)
        print("-----------Castle-----------")
        print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
        print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
        print("-----------Income-----------")
        print("Gold: %r | +100 Every Turn" % cplayer.gold['amount'])
        print("-----------Units------------")
        print("Soldier(s): %r" % cplayer.soldier['num'])
        print("Warrior(s): %r" % cplayer.warrior['num'])
        print("Knight(s): %r" % cplayer.knight['num'])
        print("----------------------------")
        return True
    elif cplayer.castle_health['castle_health'] > 0 and (gamemode_choice == 2): #change turn if castle health greater than 0
        return False
    elif cplayer.castle_health['castle_health'] == 0 and (gamemode_choice == 3): #end game and print final AI display if castle health greater is 0 (AI vs AI mode)
        print("-----------Castle-----------")
        print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
        print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
        print("-----------Income-----------")
        print("Gold: %r | +100 Every Turn" % nplayer.gold['amount'])
        print("-----------Units------------")
        print("Soldier(s): %r" % nplayer.soldier['num'])
        print("Warrior(s): %r" % nplayer.warrior['num'])
        print("Knight(s): %r" % nplayer.knight['num'])
        print("----------------------------")
        return True
    elif cplayer.castle_health['castle_health'] > 0 and (gamemode_choice == 3): #change turn and print final AI display if castle health greater than 0 (AI vs AI mode)
        #at the end of an executed decision, print updated player display and call up next player's turn
        print("-----------Castle-----------")
        print("%r Castle Health: %r" % (nplayer.name, nplayer.castle_health['castle_health']))
        print("%r Castle Health: %r" % (cplayer.name, cplayer.castle_health['castle_health']))
        print("-----------Income-----------")
        print("Gold: %r | +100 Every Turn" % nplayer.gold['amount'])
        print("-----------Units------------")
        print("Soldier(s): %r" % nplayer.soldier['num'])
        print("Warrior(s): %r" % nplayer.warrior['num'])
        print("Knight(s): %r" % nplayer.knight['num'])
        print("----------------------------")
        return False
#-end function-
def end(cplayer, nplayer, gamemode_choice):
    """
    Executes when one of the castle's health hits 0 and a winner has been decided
    Args:
        cplayer: current player
        nplayer: next player
        gamemode_choice: 1 or 2 (Player VS Player or Player VS AI)
    """
    if gamemode_choice == 1: #if player vs player
        print("The %r are Victorious!" % cplayer.name)
    if gamemode_choice == 2 and cplayer.castle_health['castle_health'] == 0: #if player vs AI and AI won
        print("The Greeks are Victorious!")
    if gamemode_choice == 2 and nplayer.castle_health['castle_health'] == 0: #if player vs AI and player won
        print("The Egyptians are Victorious!")
    if gamemode_choice == 3 and cplayer.castle_health['castle_health'] == 0: #if AI vs AI and Greek won
        print("The Greeks are Victorious!")
    if gamemode_choice == 3 and nplayer.castle_health['castle_health'] == 0: #if AI vs AI and Egyptian won
        print("The Egyptians are Victorious!")
    print("----------------------------")
    while True:
        #reset all values
        cplayer.castle_health['castle_health'] = 2000
        cplayer.gold['amount'] = 900
        cplayer.soldier['num'] = 30
        cplayer.warrior['num'] = 15
        cplayer.knight['num'] = 5
        nplayer.castle_health['castle_health'] = 2000
        nplayer.gold['amount'] = 900
        nplayer.soldier['num'] = 30
        nplayer.warrior['num'] = 15
        nplayer.knight['num'] = 5
        try_again = input("Would you like to try again? ").upper()
        if try_again == "YES" or try_again == "Y":
            start() #rerun if try again
            break
        elif try_again == "NO" or try_again == "N":
            print("Thank you for playing!") #thank player if not trying again
            break
        else:
            print("Invalid input!")
#introduction body (ask user for name)
print("\t\t\tWelcome to Age of Empire!\nIn this game, The Egyptians and Greeks are having an all out war!\nFor a start, may we know your name?")
cplayer = Empire("Egyptians") #declare cplayer as an instance of Empire class
nplayer = Empire("Greeks") #declare nplayer as an instance of Empire class
valid_name = False
while valid_name == False:
    cplayername = (input("> "))
    if len(str(cplayername)) == 0: #checks for a valid name
        print("Please enter a valid name!")
    else:
        valid_name = True
#welcome user by name and ask for gamemode choice before launching into the game
def start():
    print("Welcome %s! Your army awaits! Which gamemode would you like to choose?\n1. Player VS Player \n2. Player VS AI \n3. AI VS AI" % cplayername)
    while True:
        gamemode_choice = input("> ")
        if gamemode_choice == "1": #player vs player
            print("Play as an Egyptian against your Greek friend!\nLoading...")
            time.sleep(2) #simulate loading time
            controller(cplayer, nplayer, gamemode_choice = 1) #launch player vs player mode
            break
        elif gamemode_choice == "2": #player vs AI
            print("Play as an Egyptian against the Greek AI!\nLoading...")
            time.sleep(5) #simulate loading time
            controller(cplayer, nplayer, gamemode_choice = 2) #launch player vs AI mode
            break
        elif gamemode_choice == "3": #AI vs AI
            print("Watch the Egyptian AI battle the Greek AI!\nLoading...")
            time.sleep(5) #simulate loading time
            controller(cplayer, nplayer, gamemode_choice = 3) #launch AI vs AI mode
            break
        else:
            print("Please enter a valid input!")
start()