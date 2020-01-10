from heroes import Heroes
from monsters import Monsters
from os import system

def getUserName():
    username = input()
    return username

#Program starting point "Welcome"
print("Please Enter your name: ")
playersUsername = getUserName()
system('clear')
print("Welcome to the awesome battle text game")
print(" ")
print("Hello " + playersUsername)
print(" ")

def determineHeroAttack():
    print("Attack the monster. Enter 1 = Melee | 2 = Ranged")
    attackType = input()
    return attackType

def main():
    #Setup monter and hero
    hero = Heroes(playersUsername)
    monster = Monsters()
    
    #Both the hero and monster start with 100 health point
    monsterStartingHealthPoints = monster.healthPoints
    heroStartingHealthPoints = hero.healthPoints
    print("Players Health: " + str(heroStartingHealthPoints))
    print("Monters Health " + str(monsterStartingHealthPoints))

    #Battle Logic
    heroAttackType = determineHeroAttack()
    if heroAttackType == "1":
        heroAttacKDamage = hero.meleeAttack()
        monsterAttackDamage = monster.attack()
        print("Hero HIts for: " + str(heroAttacKDamage))
        print("Monster Hits for: " + str(monsterAttackDamage))
        
    
    elif heroAttackType == "2":
        heroAttacKDamage = hero.rangedAttack()
        monsterAttackDamage = monster.attack()
        print("Hero HIts for: " + str(heroAttacKDamage))
        print("Monster Hits for: " + str(monsterAttackDamage))
   
    heroTotalHealthPoints = heroStartingHealthPoints - monsterAttackDamage
    monsterTotalHealthPoints = monsterStartingHealthPoints - heroAttacKDamage
    print ("Heros remaining health: " + str(heroTotalHealthPoints))
    print ("Monsters remaining health: " + str(monsterTotalHealthPoints))

main()