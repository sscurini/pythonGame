from heroes import Heroes
from monsters import Monsters

def getUserName():
    username = input()
    return username

#Program starting point "Welcome"
print("Please Enter your name: ")
playersUsername = getUserName()
print(" ")
print("Welcome to the super awesome monster battle text based game")
print(" ")
print("Hello " + playersUsername)
print(" ")

def determineHeroAttack():
    print("Attack the monster. Enter 1 = Melee | 2 = Ranged")
    attackType = input()
    return attackType

def calculateDamage(attacKDamage,totalDamage,totalHealthPoints):
    totalDamage += attacKDamage
    totalHealthPoints = totalHealthPoints - totalDamage
    return totalHealthPoints

def printRemaininghealth(playersUsername,heroTotalHealthPoints,monsterTotalHealthPoints):
    print (playersUsername + "'s" + " remaining health: " + str(heroTotalHealthPoints))
    print ("Monster's remaining health: " + str(monsterTotalHealthPoints))

def battle():
    #Setup monter and hero
    hero = Heroes(playersUsername)
    monster = Monsters()
    
    #Both the hero and monster start with 100 health point
    monsterTotalHealthPoints = monster.healthPoints
    heroTotalHealthPoints = hero.healthPoints
    print(hero.name + "'s" + " Health: " + str(heroTotalHealthPoints))
    print("Monter's Health " + str(monsterTotalHealthPoints))

    #Battle Logic
    heroTotalDamage = 0
    monsterTotaldamage = 0
    while (heroTotalHealthPoints > 0) & (monsterTotalHealthPoints > 0):
        heroAttackType = determineHeroAttack()
        monsterAttackDamage = monster.attack()
        if heroAttackType == "1":
            heroAttacKDamage = hero.meleeAttack()
            print(hero.name + " Hits for: " + str(heroAttacKDamage))
            print("Monster Hits for: " + str(monsterAttackDamage))
            heroTotalHealthPoints    = calculateDamage(monsterAttackDamage,monsterTotaldamage,heroTotalHealthPoints)
            monsterTotalHealthPoints = calculateDamage(heroAttacKDamage,heroTotalDamage,monsterTotalHealthPoints)
            printRemaininghealth(hero.name,heroTotalHealthPoints,monsterTotalHealthPoints)

        elif heroAttackType == "2":
            heroAttacKDamage = hero.rangedAttack()
            print(hero.name + " Hits for: " + str(heroAttacKDamage))
            print("Monster Hits for: " + str(monsterAttackDamage))
            heroTotalHealthPoints    = calculateDamage(monsterAttackDamage,monsterTotaldamage,heroTotalHealthPoints)
            monsterTotalHealthPoints = calculateDamage(heroAttacKDamage,heroTotalDamage,monsterTotalHealthPoints)
            printRemaininghealth(hero.name,heroTotalHealthPoints,monsterTotalHealthPoints)
        else:
            print("Please enter a valid attack")

    if (monsterTotalHealthPoints <= 0) & (heroTotalHealthPoints <= 0):
        print(hero.name + ", you killed the monster but also died. Nice Try. Game Over")
    elif monsterTotalHealthPoints <= 0:
        print("Congratulations " + hero.name + ". You killed the monster. You win")
    elif heroTotalHealthPoints <= 0 :         
        print("You Died. Game Over")
battle()
