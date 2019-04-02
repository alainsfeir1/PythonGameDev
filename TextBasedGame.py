#Program name: version1.py
#Developer: Alain Sfeir
#Date: 2/16/2018
#Description: Version 1 of the game!
import random
import time
Gold=''
backpack=[]
backpack_1=[]
backpack_2=[]
final_backpack=[]
goalSword=[]
goalShield=[]
health_user=0
health_monster=0
hp=0
user_stats={}#stats for the user
monster_stats={}#stats for the monster

####
def verificationBig(choice):#involves verification that number chosen is valid and returns choice
    while choice!='1' and choice!='2' and choice!='3' and choice!='4' and choice!='5' and choice!='6' and choice!='7':
        print('Pick a Number!')
        choice=input()
    return choice
def verificationSmall(choice):#involves verification that number chosen is valid and returns choice this involves only 1 2 3 choices.
    while choice!='1' and choice!='2' and choice!='3':
        print('Pick a Number!')
        choice=input()
    return choice
####
#This is the function for the town where the trading happens
def town(backpack,Gold):
    Gold=1000
    backpack=['Gold','Flashlight','water']
    while True:#keeps looping until 7 is chosen so player leaves town
        
        print('1.visit blacksmith sector')
        print('2.Visit gambling section')
        print('4.Visit alchemist section')#this option hasnt yet been impelemented into the code
        print('5.Open backpack')
        print("6.Sorcerer's isles")
        print('7.Start Quest')
        visit=input()
        visit=verificationBig(visit)#assign verification to visit
        if visit=='5':#prints things in backpack
            print()
            print('Gold='+str(Gold))
            print(backpack)
        #here the action is at the smith shop.Conditionals check if u can buy or not
        if visit=='1':
            if Gold==0:
                print('Sorry you dont have enough gold')
            if Gold==2050:
                print('Smith:Welcome my friends.How can i help you')
                print('Translator:You now can buy armor and sword')
                print('YOU JUST BOUGHT SWORD AND ARMOR!!!')
                Gold=Gold - 2000
                backpack.append('Steel armor')
                backpack.append('Steel sword')
            if Gold ==2000:
                print('Smith:Welcome my friends.How can i help you')
                print('Translator:You now can buy armor and sword')
                print('YOU JUST BOUGHT SWORD AND ARMOR!!!')
                Gold=Gold - 50
            
                backpack.append('Steel armor')
                backpack.append('Steel sword')
            if Gold==1000:
                print('Welcome to my shop young lad what can i forge for you')
                print('''
    Would you like:
    1.Armor(1000 gold)
    2.Sword(1000 gold)
    3.Leave shop
    ''')
                choiceBS=input()
                choiceBS=verificationSmall(choiceBS)#verify using verificationSmall
                if choiceBS=='2':
                  Gold=Gold-1000
                  print('Thnx for the thousand gold, see you next time')
                  backpack.append('Steel sword')

                elif choiceBS=='1':
                  Gold=Gold-1000
                  print('Thnx for the thousand gold, see you next time')
                  backpack.append('Steel armor')
                else:
                    print('Okey maybe next time')
            
            
        if visit=='2':#gambler's place
            if Gold>1000:
                print('Sorry we are closed today')
            elif Gold<1000:
                print('Sorry you dont have enough gold')
            elif Gold==50:
                print('we are closed today')
            elif Gold==1000:
                #intro to gambler's place
                print('''
    Gambler:HHAHAHA Hello my friend, Would you like to enter in the game.
    Its 1000 gold to join. if u guess 1 of the 6 number that show after
    we throw 3 dice your gold will be doubled with 50 gold extra.
    if you lose all is lost.''')

                
                print('''
    Translator: it is a risk u wont be able to buy weapons if you lose.
                but if we win we can buy weapon plus potions from alchemists''')
               
                print('''
    Time to start you want to join ?(1 to join)
                                    (2 to return to town center)''')
                gamble=input()
                gamble=verificationSmall(gamble)
                if gamble=='1':
                    print('okey, pick your number')
                    pickedNumber=input()
                    pickedNumber=verificationBig(pickedNumber)
                    #Three dice are thrown each gives a number
                    dice1=random.randint(1,6)
                    dice2=random.randint(1,6)
                    dice3=random.randint(1,6)
                    
                    
                    if pickedNumber==str(dice1) or pickedNumber==str(dice2) or pickedNumber==str(dice3):#if ur choice of number is equal to either one of the dices thrown
                        print('Gambler:You won!!!!')
                        print('Translator:Good Job you now have 2050 gold')
                        Gold=2050
                    else:
                        print('Gambler:Sorry hard luckk')
                        print('Translator:Guess we will have to go into the temple without weapons')
                        Gold=0
                        
        
        #section for the seer which is just question and answers
        if visit=='6':
            print('Seer:It is you warriors.I have been expecting you for so long')
            print('Translator:This is the mighty seer. The all knowing future teller')
            while True:
                print('''
    Ask seer:1.How do I go back to realiy?
             2.Can i defeat the monster?
             3.Is there anything i should know before heading out?
             4.Leave Isle''')
                
                seerQues=input()
                seerQues=verificationBig(seerQues)
                
                if seerQues=='1':
                     print('Seer:The hand of god will grant you one wish. Use it...')
                     print()
                elif seerQues=='2':
                     print('Seer:Depends on your choices wise warrior')
                     print()
                elif seerQues=='3':
                    print('Seer: Yess!! Here in the land of Valisiya, you get 4 spells:Land,water,air,and fire')
                    print('')
                    print('Seer: you can use 2 only each day for it requires immense enegry')
                    print('')
                    print('Translator:Maybe this will come in handy later...')
                else:
                    print('Enough questions for now')
                    print('')
                    break
        if visit=='4':
            if Gold>0:
                print('Alchemist:Hello , i got a good shrinking potion for you for 50 gold only')
                time.sleep(2)
                print()
                print('Translator:Shrinking potion allows you to make things smaller for a specific time to make more space later on')
                print('press 1 to buy potion ')
                print('press 2 to return to main town')
                shrink=input()
                verificationSmall(shrink)
                if shrink=='1':
                    backpack.append('shrinking potion')
                    Gold=Gold-50
                    
                else:
                    print('okey maybe next time')
            
            
            elif Gold<=0:
                print('Sorry .We are closed')
                
        if visit=='7':
            print()
            print('Of we go.The quest at the temple awaits us ')
            break
        
    return backpack#returns backpack with the final gold value u got
################################################################################################
#this is stage 1 in the path to the cave
def stage1(backpack):
    print(backpack)
    print('''
Translator:We have reached the entrance of the temple.
           Hieroglyphs say that there are two paths to reach the isle.
           The 'Path of the Arrows' and 'Path of the Deadly Waters'
    ''')
    print('which would you like '+'name'+' path 1 or 2?')#change name to user input name
    print('''
1.Path of the Arrows
2.Path of the deadly waters
''')
    path=input()
    path=verificationSmall(path)
    if path=='1':
        print('Path of arrow it is then...')
        print('30 min later!!!')
        print('Reaper:Beware my friends.The road across is set by trap tiles.!')
        print('       One wrong step you get an arrow in your head')
        steps=0
        for steps in range(2):
            print('Pick a tile:1.Right tile')
            print('            2.Left tile')
            print('            3.Center tile')
            badStep=random.randint(1,3)
            move= input()
            
            if move!=str(badStep):
                print('We passed this tile lets go')
                
            if steps==1:
                print('We passed this trap , Good job')
                print('Looks like we found a key for the door of the isle')
                backpack.append('KEY')
                break
                return backpack
              
            elif move==str(badStep):
                print('''


              oops
         0  /                 <----<<< 
       \/|\__             <----<<<   <----<<<
         |                   <----<<<   <----<<<
   _____/ \________
   
   ''')
            
                
                print('''
                                                           
 .-----.---.-.--------.-----.   .-----.--.--.-----.----.   
 |  _  |  _  |        |  -__|   |  _  |  |  |  -__|   _|   
 |___  |___._|__|__|__|_____|   |_____|\___/|_____|__|     
 |_____|                                                   
                                                           
                                                           
                                                           ''')
                break
        return backpack
            
    if path=='2':
        #intro to path2 
        print('Translator:Jump into the boat!!')
        time.sleep(2)
        print('20 minutes later')
        print('Translator:Do you see that in the water?!')
        time.sleep(2)
        print('Translator: We are followed by a the megatooth an ancient animal')
        print('            said to be extinct...')
        time.sleep(3)
        print('Objective:steer the boat to dodge the attacks(BOAT CAN SUSTAIN 3 HITS)')
        print('Steer:1.Right /2.Left')
        hit=0
        miss=0
        for sharkAttacks in range(6):#loops for 6 times which we wont reach since either full hits or full misses will be achieved
            
            attack=random.randint(1,2)
            dodgeDirection=input()
            if dodgeDirection==str(attack):
                print('Dodged that attack')
                miss=miss+1#adds 1 to miss

            if dodgeDirection!=str(attack):
                print('We are hit!!!!')
                hit=hit+1#adds 1 to hit
            if miss==3:#when hit reaches 2 wins
                print('we made it!!')
                print('Looks like we found a key for the door of the isle')
                backpack.append('KEY')
                break
            if hit==3:#when hit reaches 3 loses
                print('game over')
                break
        return backpack
########################################################################################################################################     
def isle(backpack):
    goalSword=('Steel sword','Gold handle','Dragon glass')
    goalShield=('Steel shield','Diamond plate','Pixie dust')
    print('This is the isle where you will craft the weapon')
    print('We need to find material to start crafting')
    print('-------------------------------------------------')
    print('To craft Ultimate sword: ')
    print(goalSword)
    print('-------------------------------------------------')
    print('To craft ultimate shield: ')
    print(goalShield)
    print('-------------------------------------------------')
    print(backpack)
    print('-------------------------------------------------')
    print('''
There are two rooms to search:1.Loot land
                              2.King's tomb
                              3.Crafting isle
''')
    return backpack
########################################################################
#function for room 1 
def room1(backpack):
        print('We found a chest')
        print('opens chest...')
        while True:# keeps looping until it is broken
            print('''
    +---------------------+
    |loot:1.Gold handle   |
    |     2.Diamond plate |
    |     3.Gold coins    |
    +---------------------+
PICK AN ITEM:
         ''')
            choice1=input()
            if choice1=='1':
                backpack.append('Gold handle')#add gold handle to backpack
                break
            if choice1=='2':
                backpack.append('Diamond plate')#add plate to backpack
                break
            if choice1=='3':
                backpack.append('Gold coins')#add coins to backpack
                break
            else:
                print('chose an item 1 ,2 , 3')
        
        return(backpack)
##############################################################################
def room2(backpack):
          print('open the coffin to see if there is any item inside')
          while True:
            print('''
        +----------------------+
        |loot:1.Dragon Glass   |
        |     2.Pixie Dust     |
        |     3.big bow        |
        +----------------------+
        PICK AN ITEM:''')
            choice2=input()
            if choice2=='1':
                backpack.append('Dragon glass')
                break
            if choice2=='2':
                 backpack.append('Pixie dust')
                 break
            if choice2=='3':
                 backpack.append('big bow')
                 break
            else:
                print('pick 1,2, or 3')
          return(backpack)
######################;######################################################
def crafting(backpack):
    while True:
        print('pick room!!')
        room=input()
        if room=='1':
          final_backpack=room1(backpack)
          print(backpack)

        if room=='2':
          final_backpack=room2(backpack)
          print(backpack)
        if 'shrinking potion' in backpack:#u can craft more items
            if len(backpack)>11:#if number of items greater than 11 
                print('MAX 11 items in backpack')
                print(backpack)
                print('Remove item:(type exact name of item)')
                x=input()
                if x not in backpack:
                    print('no such item')
                else:
                    backpack.remove(x)#remove item from list
                    print(backpack)
            
        if 'shrinking potion' not in backpack:
            if len(backpack)>7:#if number of items in backpack bigger than 4
                print('MAX 7 items in backpack')
                print(backpack)
                print('Remove item:(type exact name of item)')
                x=input()
                while x not in backpack:
                    print('no such item')
                    print('Backpack:',backpack)
                    print('what item you want to remove')
                    x=input()
                backpack.remove(x)#remove item from list
                print(backpack)
        if room=='3':
            break

############################################################################
def room3(backpack):
    print('This is the isle')
    print(backpack)
    if 'Diamond plate' in backpack and 'Pixie dust' in backpack and 'Steel armor' and 'Gold handle' in backpack and 'Dragon glass' in backpack and 'Steel sword' in backpack:
        print('you can craft both shield and sword')
        backpack[3:13]=['////SHIELD OF AGES\\\\','////DRAGONSLAYER SWORD\\\\']
    elif 'Gold handle' in backpack and 'Dragon glass' in backpack and 'Steel sword' in backpack:#check if item in backpack
        print('you can craft sword')
        backpack[3:8]=['////DRAGONSLAYER SWORD\\\\']#SUBS items looted with dragonslaye
        print(backpack)
    elif 'Diamond plate' in backpack and 'Pixie dust' in backpack and 'Steel armor':#check if items in backpack
        print('you can craft shield')
        backpack[3:8]=['////SHIELD OF AGES\\\\']#sub shield  of ages with indexes 1 to 4 
        print(backpack)
    
    else:#if material is missing
        print('you dont have the write material')
        
    
    return backpack
                
###########################################################################
def spellsBattle(backpack):
    spellset=['1.blackhole','2.air tornado','3.ground wall(good vs liquid units)','4.water shockwave','5.fire ball','6.Sun\'s light','7.rock shield(good vs luminous units)']
    print('''
    there is a beast up ahead....
    Beast to face:
    1.groundbeast
    2.Firebeast
    3.waterbeast
    4.lightbeast''')
    print('Spells: ',spellset)
    beast1=random.randint(1,4)
    print()
    print('you are going to face beast: '+str(beast1))
    print()
    spell_1=input('Pick first spell:')
    spell_2=input('Pick second spell:')
    if beast1==1:
        if spell_1=='4' and spell_2=='5' or spell_1=='5' and spell_2=='4':
            print('you have slain the beast')
            backpack.append('3 hp pots')
            print('Look they dropped two health potions')
            print(backpack)
        else:
            print('you have been wrecked')
    elif beast1==2:
        if spell_1=='4' and spell_2=='2' or spell_1=='2' and spell_2=='4':
            print('you have slain the beast')
            backpack.append('3 hp pots')
            print('Look they dropped two health potions')
            print(backpack)
            print('you have slain the beast')
        else:
            print('you have been wrecked')
    elif beast1==3:
        if spell_1=='6' and spell_2=='3' or spell_1=='3' and spell_2=='6' :
            print('you have slain the beast')
            print('you have slain the beast')
            backpack.append('3 hp pots')
            print('Look they dropped two health potions')
            print(backpack)
        else:
            print('you have been wrecked')
    elif beast1==4:
        if spell_1=='1' and spell_2=='7' or spell_1=='7' and spell_2=='1':
            print('you have slain the beast')
            print('you have slain the beast')
            backpack.append('3 hp pots')
            print('Look they dropped two health potions')
            print(backpack)
        else:
            print('you have been wrecked')
    return backpack
##################################################
def boss_battle(backpack,user_stats,monster_stats,health_user,health_monster,hp):
    print(backpack)
    health_user=0
    health_monster=0
    hp=0
    user_stats={'Health':health_user,'health pod':hp}#stats for the user
    monster_stats={'Health':health_monster}#stats for the monster
    if '////SHIELD OF AGES\\\\' in backpack and '////DRAGONSLAYER SWORD\\\\'in backpack:
            print('ULTRA UPGRADE')
            health_monster=health_monster+160
            health_user=health_user+160
            hp=3
            
        
    elif '////SHIELD OF AGES\\\\' in backpack:
            print('upgrade stats')
            health_monster=health_monster+200
            health_user=160
            hp=3
            
    elif'////DRAGONSLAYER SWORD\\\\'in backpack:
            print('upgrade stats!!')
            health_monster=160
            health_user=health_user+120
            hp=3
            
            
    else:
            health_user=health_user+100
            health_monster=health_monster+200
            hp=3
            
    print('Monster:',health_monster)
    print('Health:',health_user)
    print('''
    Hit the monster on : 1.Head
                     2.Torso
                     3.Back
                     
                     4.heal up(20hp)''')
  

    while True:#boss battle
        
        monsterHits=random.randint(1,3)
        userHits=int(input())
        if userHits==4:
            if hp==0:
                print('no more potions')
            else:
                print('healing up!!(blocking all damage recieved)')
                hp=hp-1
                health_user=health_user+40
        if health_monster==0:#wins when health is zero
            print('you won!!!')
            user_stats.update({'reward':'Hand of God'})#add item to dictionary
            print(user_stats)
            break
        if health_user==0:#loses when health is zero
            print('you lost!!')
            break
        elif userHits==monsterHits:
            print('blocked')
            health_user=health_user-20#loses 20 health if hit
            print('Health:',health_user)
            print('Monster:',health_monster)
        elif userHits!=monsterHits:
            print('critical strike')
            health_monster=health_monster-20#loses 20 health if hit
            print('Health:',health_user)
            print('Monster:',health_monster)
    

########################################################################################################################################
def main():
    playAgain = 'yes'
    #here should be an intro for the game as a whole with options lore ....
    while playAgain == 'yes' or playAgain == 'y':
        backpack_1=town(backpack,Gold)
        backpack_2=stage1(backpack_1)
        print(backpack_2)
        if 'KEY' in backpack_2:
            final_backpack=isle(backpack_2)
            crafting(final_backpack)

            boss_backpack=room3(final_backpack)#final_bsckpack is returned and stored in boss backpack
            new_boss_backpack=spellsBattle(boss_backpack)
            print('Backpack;',new_boss_backpack)
            if '3 hp pots' in new_boss_backpack:
                boss_battle(new_boss_backpack,user_stats,monster_stats,health_user,health_monster,hp)
                print('Do you want to play again? (yes or no)')
                playAgain = input()
            
                

        else:
            print('Do you want to play again? (yes or no)')
            playAgain = input()
main()
