#class Player:
    def __init__(self,gender,health,name,defaultWeapon,credits):
        self.gender=gender
        self.health=health
        self.name = name
        self.defaultWeapon = defaultWeapon
        self.credits=credits 
        print("Player Object Created",self.gender,self.health)

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)
    
    def isDead(self):
        if self.health<=0:
            return True
        else:
            return False

def healthstring(self):
   if health >= 80 return "Healthy"
    elif health >=70 and <80 return "Stable"
    elif health >=60 and <70 return "Weak"
    elif health >0 and <60 return "Critical"
    elif health <=0 return "Dead"

def attack(self,target):
    outcome=random.randint(1,2)
    if outcome==1:
        damage=random.randint(5,20)
        target.playerHurt(damage)
        print(self.name, "attacked", target name,
              "attack succedded with damage",damage)
    


p1=Player("F",110, "Carla:, "axe',40)
p2=Player("M",100, "Maya", "sword",70)
p3.=Player(20, Carlos, "knife", 80)
players=(p1,p2,p3) + list of three players
combantants=random.sample(players,2)
attacker=combatants[0]
target=combatants[1]
attacker.attack(target)
for x in players:
#    print(x.name, x.health, x.healthstring())

      
