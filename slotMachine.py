from random import randint


symbols = ["$", "@", "&", "%", "#"]
coins = 100

def pull():
  return [symbols[randint(0,len(symbols)-1)], symbols[randint(0,len(symbols)-1)], symbols[randint(0,len(symbols)-1)]]


def betDebt(amount):
  global coins
  coins -= amount
  return coins

def draw(pull):
  return " | ".join(pull)
  
  
def count(pull):
  symbols = {
    "dollar": 0,
    "at": 0,
    "andSign":0,
    "percent":0,
    "hashTag":0
  }
  for key in pull:
      symbols[key] += 1
  return [symbols.items()[i][1] for i in range(len(symbols.items()))];


def spin(bet):
  global coins
  startingCoin = coins
  result = pull()
  if bet <= coins and bet > 0:
    countEach = count(result)
    for i in range(len(countEach)):
      if countEach[i] == 2:
        coins += bet*2
      elif countEach[i] == 3:
        coins += bet*10
      for j in range(len(result)):
        if countEach == 3 and result[j] == "$":
          coins += bet*25
  print "__________________________________"        
  print draw(result)
  print "__________________________________"  
  print "you have won " + str(abs(startingCoin - coins)) + "!"
  return coins
          


print "********************************"
print "*******BOnKerS SLoTz************"
print "********************************"
print "********************************"
print "________________________________"    
while coins >= 1:
  betAmount = int(input("$$bet$$:"))
  print "Bank: "+  str(spin(betAmount))
  betDebt(betAmount)
  
  
  
  
  
