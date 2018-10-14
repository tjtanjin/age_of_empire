"""
Create a Turn Based Strategy Game "Age of Empire". Players play as Egyptians against the Greeks.
Each round, they are given 3 options explained below:
Attack: Sum up attack of all available units and attack the castle, might fail or succeed.
        If the attack is successful, some gold will be plundered and enemy castle will lose health. There may or may not be allied casualties.
        If the attack is unsuccessful, there is a higher rate of allied casualties.
Repair: 3 options to repair castle at 100 gold, 200 gold and 300 gold.
Hire: Hire more units to increase attack strength. Knight has lower death rate than warrior and warrior has lower death rate than soldier.
Egyptians and Greeks will take turns until one of their castle health hits 0. Have fun!
"""
#Import random and time library
import random
import time
#Defining Player class and attributes
class Empire():
    def __init__(self, name):
        self.name = name
        self.castle_health = {'castle_health': 2000}
        self.gold = {'amount': 900}
        self.soldier = {'price': 20, 'num': 30, 'attack': 5, 'armor': 5, 'desc': "A light infantry unit with weak attack"}
        self.warrior = {'price': 50, 'num': 15, 'attack': 10, 'armor': 7, 'desc': "A toughened soldier with moderate attack"}
        self.knight = {'price': 100, 'num': 5, 'attack': 20, 'armor': 10, 'desc': "A heavily armored unit with strong attack"}
def end():
    while True:
        try_again = input("Would you like to try again? ").upper()
        if try_again == "YES" or try_again == "Y":
            player.castle_health['castle_health'] = 2000
            player.gold['amount'] = 900
            player.soldier['num'] = 30
            player.warrior['num'] = 10
            player.knight['num'] = 5
            computer.castle_health['castle_health'] = 2000
            computer.gold['amount'] = 900
            computer.soldier['num'] = 30
            computer.warrior['num'] = 10
            computer.knight['num'] = 5
            playerturn()
            break
        elif try_again == "NO" or try_again == "N":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input!")       
#Body to run during player's turn
def playerturn():
    player.gold['amount'] = player.gold['amount'] + 100
    print("-----------Castle-----------")
    print("Egyptian Castle Health: %r" % player.castle_health['castle_health'])
    print("Greek Castle Health: %r" % computer.castle_health['castle_health'])
    print("-----------Income-----------")
    print("Gold: %r | +100 Every Turn" % player.gold['amount'])
    print("-----------Units------------")
    print("Soldier(s): %r" % player.soldier['num'])
    print("Warrior(s): %r" % player.warrior['num'])
    print("Knight(s): %r" % player.knight['num'])
    print("----------------------------")
    print("What are your orders?\n1. Attack\n2. Repair\n3. Hire Troops")
    while True:
        player_choice = input("> ").upper()
        #Player Attack Option
        if player_choice == "1" or player_choice == "A":
            player_attack_strength = player.soldier['attack'] * player.soldier['num'] + player.warrior['attack'] * player.warrior['num'] + player.knight['attack'] * player.knight['num']
            print("Preparing Forces...")
            time.sleep(2)
            print("Attack Strength: %r" % player_attack_strength)
            print("Launching Attack...")
            time.sleep(5)
            luck = random.randint(1,10)
            if luck < 8:
                computer.castle_health['castle_health'] = computer.castle_health['castle_health'] - player_attack_strength
                if computer.castle_health['castle_health'] < 0:
                    computer.castle_health['castle_health'] = 0
                s_luck = random.randint(0, player.soldier['num']//4)
                w_luck = random.randint(0, player.warrior['num']//6)
                k_luck = random.randint(0, player.knight['num']//8)
                g_luck = random.randint(100,200)
                player.soldier['num'] = player.soldier['num'] - s_luck
                player.warrior['num'] = player.warrior['num'] - w_luck
                player.knight['num'] = player.knight['num'] - k_luck
                player.gold['amount'] = player.gold['amount'] + g_luck
                computer.gold['amount'] = computer.gold['amount'] - g_luck
                if computer.gold['amount'] < 0:
                    disparity = -(computer.gold['amount'])
                    computer.gold['amount'] = 0
                    player.gold['amount'] = player.gold['amount'] - disparity
                    print("The attack was a success! You plundered all their gold!")
                if computer.gold['amount'] > 0:
                    print("The attack was a success! You plundered %r gold!" % g_luck)
                print("Greek Castle took %r damage!" % player_attack_strength)
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                if computer.castle_health['castle_health'] == 0:
                    print("The Egyptians are Victorious!")
                    end()
                    break
                computerturn()
                break
            else:
                s_luck = random.randint(0, player.soldier['num']//3)
                w_luck = random.randint(0, player.warrior['num']//4)
                k_luck = random.randint(0, player.knight['num']//6)
                player.soldier['num'] = player.soldier['num'] - s_luck
                player.warrior['num'] = player.warrior['num'] - w_luck
                player.knight['num'] = player.knight['num'] - k_luck
                print("The attack was repelled!")
                print("%r soldiers, %r warriors and %r knights were lost!" % (s_luck, w_luck, k_luck))
                computerturn()
                break
        #Player Repair Option
        elif (player_choice == "2" or player_choice == "R") and player.gold['amount'] >= 100:
            while True:
                print("How much do you wish to repair?\n1. 100 Health (Cost 100 Gold)\n2. 200 Health (Cost 200 Gold)\n3. 300 Health (Cost 300 Gold)")
                player_repair = input("> ")
                if (player_repair == "1" or player_repair == "100") and player.gold['amount'] >= 100:
                    repair = 100
                    player.castle_health['castle_health'] = player.castle_health['castle_health'] + 100
                    player.gold['amount'] = player.gold['amount'] - 100
                    break
                elif (player_repair == "2" or player_repair == "200") and player.gold['amount'] >= 200:
                    repair = 200
                    player.castle_health['castle_health'] = player.castle_health['castle_health'] + 200
                    player.gold['amount'] = player.gold['amount'] - 200
                    break
                elif (player_repair == "3" or player_repair == "300") and player.gold['amount'] >= 300:
                    repair = 300
                    player.castle_health['castle_health'] = player.castle_health['castle_health'] + 300
                    player.gold['amount'] = player.gold['amount'] - 300
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            if player.castle_health['castle_health'] > 2000:
                gold_refund = player.castle_health['castle_health'] - 2000
                player.castle_health['castle_health'] = 2000
                player.gold['amount'] = player.gold['amount'] + gold_refund
                print("Egyptian Castle already at full health! Extra %r gold returned!" % gold_refund)
            if player.castle_health['castle_health'] <= 2000:
                print("Repairing Castle...")
                time.sleep(5)
                print("The Egyptian Castle has repaired %r health!" % repair)
            computerturn()
        #Player Repair Option but not enough Gold
        elif (player_choice == "2" or player_choice == "R") and player.gold['amount'] < 100:
            print("Not enough gold to repair! Choose another option!")
        #Player Hire Option
        elif (player_choice == "3" or player_choice == "H") and player.gold['amount'] >= player.soldier['price']:
            while True:
                print("Which unit do you wish to hire?")
                print("1. Soldier - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (player.soldier['price'], player.soldier['attack'], player.soldier['armor'], player.soldier['desc']))
                print("2. Warrior - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (player.warrior['price'], player.warrior['attack'], player.warrior['armor'], player.warrior['desc']))
                print("3. Knight - Cost: %r Gold | Attack: %r | Armor: %r | Description: %r" % (player.knight['price'], player.knight['attack'], player.knight['armor'], player.knight['desc']))
                player_hire = input("> ")
                if (player_hire == "1" or player_hire == "S") and player.gold['amount'] >= player.soldier['price']:
                    while True:
                        print("How many Soldiers do you want to hire?")
                        s_hire = input("> ")
                        if s_hire.isdigit() and int(s_hire) > 0 and int(s_hire)*player.soldier['price'] <= player.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    player.soldier['num'] = player.soldier['num'] + int(s_hire)
                    player.gold['amount'] = player.gold['amount'] - int(s_hire)*player.soldier['price']
                    print("Hiring Soldiers...")
                    time.sleep(5)
                    print("%r Soldiers hired!" % int(s_hire))
                    break
                elif (player_hire == "2" or player_hire == "W") and player.gold['amount'] >= player.warrior['price']:
                    while True:
                        print("How many Warriors do you want to hire?")
                        w_hire = input("> ")
                        if w_hire.isdigit() and int(w_hire) > 0 and int(w_hire)*player.warrior['price'] <= player.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    player.warrior['num'] = player.warrior['num'] + int(w_hire)
                    player.gold['amount'] = player.gold['amount'] - int(w_hire)*player.warrior['price']
                    print("Hiring Warriors...")
                    time.sleep(5)
                    print("%r Warriors hired!" % int(w_hire))
                    break
                elif (player_hire == "3" or player_hire == "300") and player.gold['amount'] >= player.knight['price']:
                    while True:
                        print("How many Knights do you want to hire?")
                        k_hire = input("> ")
                        if k_hire.isdigit() and int(k_hire) > 0 and int(k_hire)*player.knight['price'] <= player.gold['amount']:
                            break
                        else:
                            print("Invalid Option or Insufficient Gold! Please choose again!")
                    player.knight['num'] = player.knight['num'] + int(k_hire)
                    player.gold['amount'] = player.gold['amount'] - int(k_hire)*player.knight['price']
                    print("Hiring Knights...")
                    time.sleep(5)
                    print("%r Knights hired!" % int(k_hire))
                    break
                else:
                    print("Invalid Option or Insufficient Gold! Please choose again!")
            computerturn()
        #Player Hire Option but not enough Gold
        elif player_choice == "3" or player_choice == "H" and player.gold < 20:
            print("Not enough gold to hire! Choose another option!")
        else:
            print("Please choose a valid option!")
#Body to run during computer's turn
def computerturn():
    print("-----------Castle-----------")
    print("Egyptian Castle Health: %r" % player.castle_health['castle_health'])
    print("Greek Castle Health: %r" % computer.castle_health['castle_health'])
    print("-----------Income-----------")
    print("Gold: %r | +100 Every Turn" % player.gold['amount'])
    print("-----------Units------------")
    print("Soldier(s): %r" % player.soldier['num'])
    print("Warrior(s): %r" % player.warrior['num'])
    print("Knight(s): %r" % player.knight['num'])
    print("----------------------------")
    computer.gold['amount'] = computer.gold['amount'] + 100
    print("The Greeks are considering their move...")
    time.sleep(3)
    while True:
        if computer.soldier['attack'] * computer.soldier['num'] + computer.warrior['attack'] * computer.warrior['num'] + computer.knight['attack'] * computer.knight['num'] > 320:
            strength = 4
        else:
            strength = 5
        if computer.castle_health['castle_health'] > 650:
            health = 1
        else:
            health = 0
        computer_choice = random.randint(health,strength)
        #Computer Attack Option
        if computer_choice == 2 or computer_choice == 3:
            computer_attack_strength = computer.soldier['attack'] * computer.soldier['num'] + computer.warrior['attack'] * computer.warrior['num'] + computer.knight['attack'] * computer.knight['num']
            print("The Greeks decided to launch an attack!")
            print("Greek Attack Strength: %r" % computer_attack_strength)
            print("Greeks launching Attack...")
            time.sleep(5)
            luck = random.randint(1,10)
            if luck < 8:
                player.castle_health['castle_health'] = player.castle_health['castle_health'] - computer_attack_strength
                if player.castle_health['castle_health'] < 0:
                    player.castle_health['castle_health'] = 0
                s_luck = random.randint(0, computer.soldier['num']//4)
                w_luck = random.randint(0, computer.warrior['num']//6)
                k_luck = random.randint(0, computer.knight['num']//8)
                g_luck = random.randint(100,200)
                computer.soldier['num'] = computer.soldier['num'] - s_luck
                computer.warrior['num'] = computer.warrior['num'] - w_luck
                computer.knight['num'] = computer.knight['num'] - k_luck
                player.gold['amount'] = player.gold['amount'] - g_luck
                computer.gold['amount'] = computer.gold['amount'] + g_luck
                if player.gold['amount'] < 0:
                    disparity = -(player.gold['amount'])
                    player.gold['amount'] = 0
                    computer.gold['amount'] = computer.gold['amount'] - disparity
                    print("The Greek attack was a success! They plundered all the gold!")
                if player.gold['amount'] > 0:
                    print("The Greek attack was a success! They plundered %r gold!" % g_luck)
                print("Egyptian Castle took %r damage!" % computer_attack_strength)
                if player.castle_health['castle_health'] == 0:
                    print("The Greeks are Victorious!")
                    end()
                playerturn()
            else:
                s_luck = random.randint(0, computer.soldier['num']//3)
                w_luck = random.randint(0, computer.warrior['num']//4)
                k_luck = random.randint(0, computer.knight['num']//6)
                computer.soldier['num'] = computer.soldier['num'] - s_luck
                computer.warrior['num'] = computer.warrior['num'] - w_luck
                computer.knight['num'] = computer.knight['num'] - k_luck
                print("The attack was repelled!")
                playerturn()
        #Computer Repair Option
        elif (computer_choice == 1 and computer.gold['amount'] >= 100 and computer.castle_health['castle_health'] < 2000) or (computer_choice == 0 and computer.gold['amount'] >= 100 and computer.castle_health['castle_health'] < 2000):
                while True:
                    computer_repair = random.randint(1,3)
                    if computer_repair == 1 and computer.gold['amount'] >= 100:
                        repair = 100
                        computer.castle_health['castle_health'] = computer.castle_health['castle_health'] + 100
                        computer.gold['amount'] = computer.gold['amount'] - 100
                        break
                    elif computer_repair == 2 and computer.gold['amount'] >= 200:
                        repair = 200
                        computer.castle_health['castle_health'] = computer.castle_health['castle_health'] + 200
                        computer.gold['amount'] = computer.gold['amount'] - 200
                        break
                    elif computer_repair == 3 and computer.gold['amount'] >= 300:
                        repair = 300
                        computer.castle_health['castle_health'] = computer.castle_health['castle_health'] + 300
                        computer.gold['amount'] = computer.gold['amount'] - 300
                        break
                    else:
                        continue
                if computer.castle_health['castle_health'] > 2000:
                    gold_refund = computer.castle_health['castle_health'] - 2000
                    computer.castle_health['castle_health'] = 2000
                    computer.gold['amount'] = computer.gold['amount'] + gold_refund
                    print("Greek Castle already at full health! Extra %r gold returned!" % gold_refund)
                if computer.castle_health['castle_health'] <= 2000:
                    print("Greeks repairing Castle...")
                    time.sleep(5)
                    print("The Greek Castle has repaired %r health!" % repair)
                playerturn()
        #Computer Hire Option
        elif (computer_choice == 4 and computer.gold['amount'] >= 100) or (computer_choice == 5 and computer.gold['amount'] >= 100) :
            while True:
                computer_hire = random.randint(1,3)
                if computer_hire == 1 and computer.gold['amount'] >= computer.soldier['price']:
                    while True:
                        s_hire = random.randint(5,20)
                        if int(s_hire)*computer.soldier['price'] <= computer.gold['amount']:
                            break
                        else:
                            continue
                    computer.soldier['num'] = computer.soldier['num'] + int(s_hire)
                    computer.gold['amount'] = computer.gold['amount'] - int(s_hire)*computer.soldier['price']
                    break
                if computer_hire == 2 and computer.gold['amount'] >= computer.warrior['price']:
                    while True:
                        w_hire = random.randint(2,8)
                        if int(w_hire)*computer.warrior['price'] <= computer.gold['amount']:
                            break
                        else:
                            continue
                    computer.warrior['num'] = computer.warrior['num'] + int(w_hire)
                    computer.gold['amount'] = computer.gold['amount'] - int(w_hire)*computer.warrior['price']
                    break
                if computer_hire == 3 and computer.gold['amount'] >= computer.knight['price']:
                    while True:
                        k_hire = random.randint(1,4)
                        if int(k_hire)*computer.knight['price'] <= computer.gold['amount']:
                            break
                        else:
                            continue
                    computer.knight['num'] = computer.knight['num'] + int(k_hire)
                    computer.gold['amount'] = computer.gold['amount'] - int(k_hire)*computer.knight['price']
                    break
                else:
                    continue
            print("Greeks hiring units...")
            time.sleep(5)
            print("The Greeks have hired more units!")
            playerturn()
        else:
            continue
#Starting Body
print("\t\t\tWelcome to Age of Empire!\nIn this game, play as the Egyptian Empire and triumph against the Greeks!\nFor a start, may we know your name?")
valid_name = False
while valid_name == False:
    playername = (input("> "))
    if len(str(playername)) == 0:
        print("Please enter a valid name!")
    else:
        valid_name = True
print("Welcome %s! Your army awaits!" % playername)
player = Empire(playername)
computer = Empire("Greek")
playerturn()