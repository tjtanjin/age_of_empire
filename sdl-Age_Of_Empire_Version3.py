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
#Defining Empire class and attributes
class Empire():
    def __init__(self, name):
        self.name = name
        self.castle_health = {'castle_health': 2000} #max/starting castle health
        self.gold = {'amount': 900} #starting gold
        self.soldier = {'price': 20, 'num': 30, 'attack': 5, 'armor': 5, 'desc': "A light infantry unit with weak attack"} #Soldier properties
        self.warrior = {'price': 50, 'num': 15, 'attack': 10, 'armor': 7, 'desc': "A toughened soldier with moderate attack"} #Warrior properties
        self.knight = {'price': 100, 'num': 5, 'attack': 20, 'armor': 10, 'desc': "A heavily armored unit with strong attack"} #Knight properties
#Code to run when a winner is declared
def end(cplayer, nplayer, turn):
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
    if turn == 1 or turn == 2: #If pvp
        print("The %r are Victorious!" % cplayer.name)
    if turn == 0 and cplayer.castle_health['castle_health'] == 0: #if pvai and ai won
        print("The Greeks are Victorious!")
    if turn == 0 and nplayer.castle_health['castle_health'] == 0: #if pvai and player won
        print("The Egyptians are Victorious!")
    print("----------------------------")
    while True:
        #Reset all values
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
            start() #Rerun if try again
            break
        elif try_again == "NO" or try_again == "N":
            print("Thank you for playing!") #Thank player if not trying again
            break
        else:
            print("Invalid input!")
def change_turn(turn):
    #Change player's turn
    if turn == 1:
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
        turn = 2
        player1 = nplayer
        player2 = cplayer
        playerturn(player1, player2, turn)
    elif turn == 2:
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
        turn = 1
        player1 = cplayer
        player2 = nplayer
        playerturn(player1, player2, turn)
#Body to run during cplayer's turn
def playerturn(cplayer, nplayer,turn):
    #Player's main display at the beginning of his/her turn
    cplayer.gold['amount'] = cplayer.gold['amount'] + 100
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
    while True:
        cplayer_choice = input("> ").upper()
        #Player Attack Option
        if cplayer_choice == "1" or cplayer_choice == "A":
            cplayer_attack_strength = cplayer.soldier['attack'] * cplayer.soldier['num'] + cplayer.warrior['attack'] * cplayer.warrior['num'] + cplayer.knight['attack'] * cplayer.knight['num']
            print("Preparing Forces...") #Simulate loading time to calculate total attack strength
            time.sleep(2)
            print("Attack Strength: %r" % cplayer_attack_strength)
            print("Launching Attack...")
            time.sleep(5)
            luck = random.randint(1,10)
            if luck < 8:
                nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] - cplayer_attack_strength
                if nplayer.castle_health['castle_health'] < 0:
                    nplayer.castle_health['castle_health'] = 0
                s_luck = random.randint(0, cplayer.soldier['num']//4) #Randomly give casualty to the attacker
                w_luck = random.randint(0, cplayer.warrior['num']//6)
                k_luck = random.randint(0, cplayer.knight['num']//8)
                g_luck = random.randint(100,200) #Randomly loot gold
                cplayer.soldier['num'] = cplayer.soldier['num'] - s_luck #Subtract casualty from initial amount
                cplayer.warrior['num'] = cplayer.warrior['num'] - w_luck 
                cplayer.knight['num'] = cplayer.knight['num'] - k_luck 
                cplayer.gold['amount'] = cplayer.gold['amount'] + g_luck
                nplayer.gold['amount'] = nplayer.gold['amount'] - g_luck
                if nplayer.gold['amount'] < 0: #Checks for gold quantity before plundering and returns if gold hits -ve value
                    disparity = -(nplayer.gold['amount'])
                    nplayer.gold['amount'] = 0
                    cplayer.gold['amount'] = cplayer.gold['amount'] - disparity
                    print("The attack was a success! You plundered all their gold!")
                if nplayer.gold['amount'] > 0: #Checks for gold quantity before plundering
                    print("The attack was a success! You plundered %r gold!" % g_luck)
                print("%r Castle took %r damage!" % (nplayer.name, cplayer_attack_strength))
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                if nplayer.castle_health['castle_health'] == 0: #End game if player castle health hits 0
                    end(cplayer, nplayer, turn)
                    break
                elif turn == 0: #Run AI's code if turn == 0 (AI Mode)
                    computerturn(turn)
                else:
                    return playerturn(nplayer, cplayer, turn)
                break
            else:
                s_luck = random.randint(0, cplayer.soldier['num']//3) #Randomly give casualty to the attacker (Higher casualty rate than successful attack)
                w_luck = random.randint(0, cplayer.warrior['num']//4)
                k_luck = random.randint(0, cplayer.knight['num']//6)
                cplayer.soldier['num'] = cplayer.soldier['num'] - s_luck #Subtract casualty from initial amount
                cplayer.warrior['num'] = cplayer.warrior['num'] - w_luck
                cplayer.knight['num'] = cplayer.knight['num'] - k_luck
                print("The attack was repelled!")
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                if turn == 0: #Run AI's code if turn == 0 (AI Mode)
                    computerturn(turn)
                else:
                    return playerturn(nplayer, cplayer, turn)
                break
        #Player Repair Option
        elif (cplayer_choice == "2" or cplayer_choice == "R") and cplayer.gold['amount'] >= 100: #Check for enough gold for minimal repair
            while True:
                #Straightforward option to repair castle health
                print("How much do you wish to repair?\n1. 100 Health (Cost 100 Gold)\n2. 200 Health (Cost 200 Gold)\n3. 300 Health (Cost 300 Gold)")
                cplayer_repair = input("> ")
                if (cplayer_repair == "1" or cplayer_repair == "100") and cplayer.gold['amount'] >= 100:
                    repair = 100
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 100
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 100
                    break
                elif (cplayer_repair == "2" or cplayer_repair == "200") and cplayer.gold['amount'] >= 200:
                    repair = 200
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 200
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 200
                    break
                elif (cplayer_repair == "3" or cplayer_repair == "300") and cplayer.gold['amount'] >= 300:
                    repair = 300
                    cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] + 300
                    cplayer.gold['amount'] = cplayer.gold['amount'] - 300
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            if cplayer.castle_health['castle_health'] > 2000: #Checks if castle health is more than 2000 and refunds extra gold and health
                gold_refund = cplayer.castle_health['castle_health'] - 2000
                cplayer.castle_health['castle_health'] = 2000
                cplayer.gold['amount'] = cplayer.gold['amount'] + gold_refund
                print("%r Castle already at full health! Extra %r gold returned!" % (cplayer.name, gold_refund))
            elif cplayer.castle_health['castle_health'] <= 2000:
                print("Repairing Castle...")
                time.sleep(5)
                print("The Egyptian Castle has repaired %r health!" % repair)
            if turn == 0: #Run AI's code if turn == 0 (AI Mode)
                computerturn(turn)
                break
            else:
                return playerturn(nplayer, cplayer, turn)
                break
        #Player Repair Option but not enough Gold
        elif (cplayer_choice == "2" or cplayer_choice == "R") and cplayer.gold['amount'] < 100: #Reject if not enough gold for repair
            print("Not enough gold to repair! Choose another option!")
        #Player Hire Option
        elif (cplayer_choice == "3" or cplayer_choice == "H") and cplayer.gold['amount'] >= cplayer.soldier['price']: #Check for enough gold for minimal hire
            while True:
                print("Which unit do you wish to hire?")
                print("1. Soldier - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.soldier['price'], cplayer.soldier['attack'], cplayer.soldier['armor'], cplayer.soldier['desc']))
                print("2. Warrior - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.warrior['price'], cplayer.warrior['attack'], cplayer.warrior['armor'], cplayer.warrior['desc']))
                print("3. Knight - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (cplayer.knight['price'], cplayer.knight['attack'], cplayer.knight['armor'], cplayer.knight['desc']))
                cplayer_hire = input("> ")
                if (cplayer_hire == "1" or cplayer_hire == "S") and cplayer.gold['amount'] >= cplayer.soldier['price']:
                    while True:
                        print("How many Soldiers do you want to hire?")
                        s_hire = input("> ")
                        if s_hire.isdigit() and int(s_hire) > 0 and int(s_hire)*cplayer.soldier['price'] <= cplayer.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.soldier['num'] = cplayer.soldier['num'] + int(s_hire)
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(s_hire)*cplayer.soldier['price']
                    print("Hiring Soldiers...")
                    time.sleep(5)
                    print("%r Soldiers hired!" % int(s_hire))
                    break
                elif (cplayer_hire == "2" or cplayer_hire == "W") and cplayer.gold['amount'] >= cplayer.warrior['price']:
                    while True:
                        print("How many Warriors do you want to hire?")
                        w_hire = input("> ")
                        if w_hire.isdigit() and int(w_hire) > 0 and int(w_hire)*cplayer.warrior['price'] <= cplayer.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.warrior['num'] = cplayer.warrior['num'] + int(w_hire)
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(w_hire)*cplayer.warrior['price']
                    print("Hiring Warriors...")
                    time.sleep(5)
                    print("%r Warriors hired!" % int(w_hire))
                    break
                elif (cplayer_hire == "3" or cplayer_hire == "300") and cplayer.gold['amount'] >= cplayer.knight['price']:
                    while True:
                        print("How many Knights do you want to hire?")
                        k_hire = input("> ")
                        if k_hire.isdigit() and int(k_hire) > 0 and int(k_hire)*cplayer.knight['price'] <= cplayer.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    cplayer.knight['num'] = cplayer.knight['num'] + int(k_hire)
                    cplayer.gold['amount'] = cplayer.gold['amount'] - int(k_hire)*cplayer.knight['price']
                    print("Hiring Knights...")
                    time.sleep(5)
                    print("%r Knights hired!" % int(k_hire))
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            if turn == 0: #Run AI's code if turn == 0 (AI Mode)
                computerturn(turn)
                break
            else:
                return playerturn(nplayer, cplayer, turn)
                break
        #Player Hire Option but not enough Gold
        elif cplayer_choice == "3" or cplayer_choice == "H" and cplayer.gold < 20: #Reject if not enough gold for hire
            print("Not enough gold to hire! Choose another option!")
        else:
            print("Please choose a valid option!")
#Body to run during an AI's turn (if applicable)
def computerturn(turn):
    #Player's main display at the beginning of AI's turn
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
    nplayer.gold['amount'] = nplayer.gold['amount'] + 100
    print("The Greeks are considering their move...")
    time.sleep(3)
    while True:
        #Strength and health use to give the AI some "intelligence". If health below a certain amount, chances of AI repairing is higher. If attack strength under a certain amount, chance of AI hiring is higher.
        if nplayer.soldier['attack'] * nplayer.soldier['num'] + nplayer.warrior['attack'] * nplayer.warrior['num'] + nplayer.knight['attack'] * nplayer.knight['num'] > 320:
            strength = 4
        else:
            strength = 5
        if nplayer.castle_health['castle_health'] > 650:
            health = 1
        else:
            health = 0
        nplayer_choice = random.randint(health,strength)
        #Computer Attack Option
        if nplayer_choice == 2 or nplayer_choice == 3:
            nplayer_attack_strength = nplayer.soldier['attack'] * nplayer.soldier['num'] + nplayer.warrior['attack'] * nplayer.warrior['num'] + nplayer.knight['attack'] * nplayer.knight['num']
            print("The Greeks decided to launch an attack!")
            print("Greek Attack Strength: %r" % nplayer_attack_strength)
            print("Greeks launching Attack...")
            time.sleep(5)
            luck = random.randint(1,10)
            if luck < 8:
                cplayer.castle_health['castle_health'] = cplayer.castle_health['castle_health'] - nplayer_attack_strength
                if cplayer.castle_health['castle_health'] < 0:
                    cplayer.castle_health['castle_health'] = 0
                s_luck = random.randint(0, nplayer.soldier['num']//4) #Same as player, randomizing casualty
                w_luck = random.randint(0, nplayer.warrior['num']//6)
                k_luck = random.randint(0, nplayer.knight['num']//8)
                g_luck = random.randint(100,200)
                nplayer.soldier['num'] = nplayer.soldier['num'] - s_luck #Subtracting casualty from initial amount
                nplayer.warrior['num'] = nplayer.warrior['num'] - w_luck
                nplayer.knight['num'] = nplayer.knight['num'] - k_luck
                cplayer.gold['amount'] = cplayer.gold['amount'] - g_luck #Plundering gold, same as player
                nplayer.gold['amount'] = nplayer.gold['amount'] + g_luck
                if cplayer.gold['amount'] < 0: #Checking for gold amount to make sure gold will not hit -ve
                    disparity = -(cplayer.gold['amount'])
                    cplayer.gold['amount'] = 0
                    nplayer.gold['amount'] = nplayer.gold['amount'] - disparity
                    print("The Greek attack was a success! They plundered all the gold!")
                if cplayer.gold['amount'] > 0:
                    print("The Greek attack was a success! They plundered %r gold!" % g_luck)
                print("Egyptian Castle took %r damage!" % nplayer_attack_strength)
                if cplayer.castle_health['castle_health'] == 0: #Checks for winning condition
                    end(cplayer, nplayer, turn)
                    break
                elif cplayer.castle_health['castle_health'] > 0:
                    playerturn(cplayer, nplayer, turn)
            else:
                s_luck = random.randint(0, nplayer.soldier['num']//3) #Higher casualty rate for failed attack
                w_luck = random.randint(0, nplayer.warrior['num']//4)
                k_luck = random.randint(0, nplayer.knight['num']//6)
                nplayer.soldier['num'] = nplayer.soldier['num'] - s_luck #Subtract casualty from initial amount
                nplayer.warrior['num'] = nplayer.warrior['num'] - w_luck
                nplayer.knight['num'] = nplayer.knight['num'] - k_luck
                print("The attack was repelled!")
                playerturn(cplayer, nplayer, turn)
        #Computer Repair Option
        #Checks for sufficient gold for minimal repair
        elif (nplayer_choice == 1 and nplayer.gold['amount'] >= 100 and nplayer.castle_health['castle_health'] < 2000) or (nplayer_choice == 0 and nplayer.gold['amount'] >= 100 and nplayer.castle_health['castle_health'] < 2000):
                while True:
                    nplayer_repair = random.randint(1,3)
                    if nplayer_repair == 1 and nplayer.gold['amount'] >= 100:
                        repair = 100
                        nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 100
                        nplayer.gold['amount'] = nplayer.gold['amount'] - 100
                        break
                    elif nplayer_repair == 2 and nplayer.gold['amount'] >= 200:
                        repair = 200
                        nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 200
                        nplayer.gold['amount'] = nplayer.gold['amount'] - 200
                        break
                    elif nplayer_repair == 3 and nplayer.gold['amount'] >= 300:
                        repair = 300
                        nplayer.castle_health['castle_health'] = nplayer.castle_health['castle_health'] + 300
                        nplayer.gold['amount'] = nplayer.gold['amount'] - 300
                        break
                    else:
                        continue
                if nplayer.castle_health['castle_health'] > 2000:
                    gold_refund = nplayer.castle_health['castle_health'] - 2000
                    nplayer.castle_health['castle_health'] = 2000
                    nplayer.gold['amount'] = nplayer.gold['amount'] + gold_refund
                    print("Greek Castle already at full health! Extra %r gold returned!" % gold_refund)
                elif nplayer.castle_health['castle_health'] <= 2000:
                    print("Greeks repairing Castle...")
                    time.sleep(5)
                    print("The Greek Castle has repaired %r health!" % repair)
                playerturn(cplayer, nplayer, turn)
        #Computer Hire Option
        #Checks for sufficient gold for minimal hire of 100 gold worth of soldiers (purposely to make AI hire more)
        elif (nplayer_choice == 4 and nplayer.gold['amount'] >= 100) or (nplayer_choice == 5 and nplayer.gold['amount'] >= 100) :
            while True:
                nplayer_hire = random.randint(1,3)
                if nplayer_hire == 1 and nplayer.gold['amount'] >= nplayer.soldier['price']:
                    while True:
                        s_hire = random.randint(5,20)
                        if int(s_hire)*nplayer.soldier['price'] <= nplayer.gold['amount']:
                            break
                        else:
                            continue
                    nplayer.soldier['num'] = nplayer.soldier['num'] + int(s_hire)
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(s_hire)*nplayer.soldier['price']
                    break
                if nplayer_hire == 2 and nplayer.gold['amount'] >= nplayer.warrior['price']:
                    while True:
                        w_hire = random.randint(2,8)
                        if int(w_hire)*nplayer.warrior['price'] <= nplayer.gold['amount']:
                            break
                        else:
                            continue
                    nplayer.warrior['num'] = nplayer.warrior['num'] + int(w_hire)
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(w_hire)*nplayer.warrior['price']
                    break
                if nplayer_hire == 3 and nplayer.gold['amount'] >= nplayer.knight['price']:
                    while True:
                        k_hire = random.randint(1,4)
                        if int(k_hire)*nplayer.knight['price'] <= nplayer.gold['amount']:
                            break
                        else:
                            continue
                    nplayer.knight['num'] = nplayer.knight['num'] + int(k_hire)
                    nplayer.gold['amount'] = nplayer.gold['amount'] - int(k_hire)*nplayer.knight['price']
                    break
                else:
                    continue
            print("Greeks hiring units...")
            time.sleep(5)
            print("The Greeks have hired more units!")
            playerturn(cplayer, nplayer, turn)
        else:
            continue
#Introduction (Ask user for name)
print("\t\t\tWelcome to Age of Empire!\nIn this game, The Egyptians and Greeks are having an all out war!\nFor a start, may we know your name?")
cplayer = Empire("Egyptians")
nplayer = Empire("Greeks")
valid_name = False
while valid_name == False:
    cplayername = (input("> "))
    if len(str(cplayername)) == 0: #Checks for valid name
        print("Please enter a valid name!")
    else:
        valid_name = True
#Ask for gamemode choice before starting
def start():
    print("Welcome %s! Your army awaits! Which gamemode would you like to choose?\n1. Player VS Player \n2. Player VS AI" % cplayername)
    while True:
        gamemode_choice = input("> ")
        if gamemode_choice == "1":
            print("Play as an Egyptian against your Greek friend!\nLoading...")
            time.sleep(2)
            turn = 1
            player1 = cplayer
            player2 = nplayer
            playerturn(player1, player2, turn)
            break
        elif gamemode_choice == "2":
            print("Play as an Egyptian against the Greek AI!\nLoading...")
            time.sleep(5)
            turn = 0
            player1 = cplayer
            computer = nplayer
            playerturn(player1, computer, turn)
            break
        else:
            print("Please enter a valid input!")
start()

