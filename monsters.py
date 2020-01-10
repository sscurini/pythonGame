import random

class Monsters:

    def __init__(self, healthPoints = 100):
        self.healthPoints = healthPoints
    
    def attack(self):
       attackHit = random.randint(10,31)
       return attackHit