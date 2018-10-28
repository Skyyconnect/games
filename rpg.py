from random import randint 
from time import sleep

inGame = True
shopItems = ["Health Potion", "Wooden Sword", "Full Heal", "Bronze Sword"]
prices = [15,25,50,100]

story = [
  "There was once a dark Castle. A dark mage lived there. You wondered into the castle one day.",
  "You awake from a deep slumber, only to hear sounds coming from the hallway...",
  "You open the door and see a monster standing outside!",
  "It tries to eat you but you dodge it and run past it.",
  "You run down the hall with the monster close behind. Don't slow down!"
  "You keep running, but you still hear the monster growling behind you."
  "You see a doorway up ahead, but when you get there, you find another monster!"
  "The monster chasing you falls behind, and you can slow down for a bit."
  "You hear spooky noises coming from down the hallway."
  
  ]


class Monster:
  def __init__(self, typeOf, hp, attack):
    self.typeOf = typeOf
    self.hp = hp 
    self.attack = attack
    self.isFaster = False
    self.level = 1
    self.speed = randint(1,10)
    self.gold = randint(1,10)
    
  def takeDamage(self,amount):
    self.hp -= amount
    return self.hp
  
  def stats(self):
    print "#####################"
    print "Type: " + self.typeOf
    print "Level: "+ str(self.level)
    print "HP: " + str(self.hp)
    print "Attack: " + str(self.attack)
    print "#####################"
    
class Player:
  def __init__(self, name, hp, attack, classification):
    self.name = name 
    self.hp = hp 
    self.attack = attack
    self.classification = classification
    self.level = 1
    self.isFaster = False
    self.speed = randint(1,10)
    self.gold = 10
    self.inventory = []
    self.monstersKilled = 0
  
  def takeDamage(self, amount):
    self.hp -= amount
    return self.hp
  
  def stats(self):
    print "@@@@@@@@@@@@@@@@@@@@"
    print "Name: " + self.name
    print "Class: " + self.classification
    print "HP: " +  str(self.hp)
    print "Attack: " + str(self.attack)
    print "Level: " + str(self.level)
    print "Gold: " + str(self.gold)
    print "@@@@@@@@@@@@@@@@@@@@"
    
    
  def levelUp(self):
    if self.monstersKilled % 4 ==0:
      self.level += 1
      self.attack += self.level
      self.speed += 1
      print "You have leveled up!"
    else:
      print "You have killed "+ str(self.monstersKilled)+ " monsters"

player = Player("John", 100, 5, "Warrior")
monsterType = ["Goblin", "Snake-Monster","Zombie","Ghost"]

def createMonster():
  return Monster(monsterType[randint(0, len(monsterType)-1)],randint(3, 10)*player.level, randint(1,5)*player.level)


def combat(a,b):
  while a.hp >=1 and b.hp >=1:
    if a.speed > b.speed:
      a.isFaster = True
    else:
      b.isFaster = True
    
    if a.isFaster:
      b.takeDamage(a.attack)
      a.takeDamage(b.attack)
    else:
      a.takeDamage(b.attack)
      b.takeDamage(a.attack)
      
    a.stats()
    b.stats()
    sleep(1)
    
    if a.hp < 1:
      print "You Died"
      inGame = False
      break
    if b.hp <1:
      print b.typeOf+ " has died"
      player.monstersKilled += 1
      a.gold += b.gold
      print "You recieved " + str(b.gold) + " Gold!"
      break
  a.levelUp()


def shop():
  print "Welcome to Shop. You have " + str(player.gold)+ " Gold"
  for i in range(len(shopItems)):
    print str(i+1) + ")" + shopItems[i] + "  $"+ str(prices[i])
  
  item = int(input("what do you want to buy(pick a number)?"))
  for j in range(len(shopItems)):
    if item == j+1:
      if player.gold >= prices[j]:
        player.gold -= prices[j]
        player.inventory.append(shopItems[j])
        print "You bought a " + shopItems[j] 
      else:
        print "you do not have enough Gold!"
        break
        
def use():
  item = input("what item do you want to use?")
  if item in player.inventory:
    
    if item == "Health Potion":
      health = randint(10,20)
      player.hp += health
      player.inventory.remove("Health Potion")
      print "you have been healed: " + str(health)
      
    elif item == "Mystery Potion":
      chance = randint(1,2)
      if chance == 1:
        player.hp += 10
        print "you gained 10 health"
      else:
        player.hp -= 10
        print "you lost 10 health"
      player.inventory.remove("Mystery Potion")
    
    elif item == "Full Heal":
      player.hp = 100
      print "You have been fully healed"
      player.inventory.remove("Full Heal")
      
    elif item == "Wooden Sword":
      atk = randint(1,3)
      player.attack += atk
      print "your attacked increased by " + str(atk)
      player.inventory.remove("Wooden Sword")
    
 
def search():
  chance = randint(1,100)
  if chance < 5:
    print "you have found a [Health Potion]"
    player.inventory.append("Health Potion")
  
  elif chance < 25:
    gold = randint(1,15)
    player.gold += gold
    print "You found " + str(gold) + " gold"
  
  elif chance < 35:
    print "you have found a [Mystery Potion]"
    player.inventory.append("Mystery Potion")
  
  else:
    print "You found Nothing! "
  



enemyVoice = ["You have been attacked", "You have been ambush"]      
print "Welcome to |Peter in the Castle|"
name = input("Choose your name:")
player.name = name
print "Welcome " + player.name


print story[0]

while player.hp >0 and inGame:
  if player.hp > 100:
    player.hp = 100
  chance = randint(1,10)
  into = input("##>")
  if chance <= 2:
    print enemyVoice[randint(0, len(enemyVoice)-1)]
    sleep(2)
    monster = createMonster()
    monster.level = player.level
    combat(player, monster)
  if chance <= 5 and chance > 2:
    print story[randint(1,len(story)-1)]
  if into == "stats":
    player.stats()
    print "Inventory: " + str(player.inventory)
  
  if into == "search":
    search()
  
  if into == "shop":
    shop()
    print "Inventory: " + str(player.inventory)
  
  if into == "stop":
    inGame = False
    print "You ended the adventure!"
    break
  
  if into == "use":
    use()
  
  
    
  

      
  
  
  
  
  
  
  
  
  
  
  
  
  
  