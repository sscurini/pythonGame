import random

class Heroes:

    def __init__(self, name, healthPoints = 100):
        self.name = name
        self.healthPoints = healthPoints
        
    def rangedAttack(self):
       attackHit = random.randint(20,41)
       return attackHit
    
    def meleeAttack(self):
       attackHit = random.randint(1,11)
       return attackHit