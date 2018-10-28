from processing import * 
from random import randint, shuffle 
from time import sleep





WIDTH = 400
HEIGHT = 400
deck = []
suit = ['hearts', 'spades', 'clubs', 'diamonds']



def setup():
  frameRate(25)
  size(WIDTH,HEIGHT)



class Game:
  def __init__(self, deck):
    self.computerValue = 0
    self.playerValue = 0
    self.player = []
    self.computer = []
    self.maxValue = 21
    self.deck = deck
    self.playerStay = False 
    self.computerStay = False
    
  
  def shuffle(self):
    shuffle(self.deck)
  
   
  def giveCard(self, person):
    person.append(self.deck[len(self.deck)-1])
    self.deck.pop(len(self.deck)-1)
    
    
 
  def deal(self):
    for i in xrange(2):
      self.giveCard(self.player)
      self.giveCard(self.computer)
  
  def score(self):
    self.playerValue = 0
    for i in range(len(self.player)-1):
      self.playerValue += self.player[i].value
    self.computerValue = 0
    for j in range(len(self.computer)-1):
      self.computerValue += self.computer[i].value
    print self.playerValue
    
    
game = Game(deck)    
    
      
  
 
class Button:
  def __init__(self, x,y, width, height, text):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.isClicked = False
    
    
  def draw(self):
    fill(147, 86, 175)
    return rect(self.x, self.y, self.width, self.height)
  
  def buttonText(self):
    return addText(self.text, self.x+(self.width/3), self.y+(self.height/2),16, 255,255,255)
    
  def mouseEvent(self, mouse):
    if mouseCollision(self, mouse,0):
      if text == 'HIT':
        game.givecard(game.player)
      elif text == 'STAY':
        game.playerStay = True
        
      self.isClicked = True
      return self.isClicked
    else:
      self.isClicked = False
      return self.isClicked
    
    
class Card:
  def __init__(self, x,y, suit, value):
    self.x = x 
    self.y = y
    self.width = 50
    self.height = 68
    self.suit = suit 
    self.value = value
    self.isFlipped = False 
    

  def draw(self, shape):
    if self.isFlipped:
      fill(255,255,255)
    else:
      fill(255,0,0)
    if shape == 'rect':
      return rect(self.x,self.y, 50,68)
    if shape == 'circle':
      return ellipse(self.x, self.y, 50,50)
      
  def addText(self):
    textSize(10)
    if self.suit == 'Club' or self.suit == 'Spade':
      fill(0,0,0)
      return text(str(self.value)+ " of "+ self.suit,self.x,self.y+(self.height/2))
    else:
      fill(255,0,0)
      return text(str(self.value)+ " of "+ self.suit,self.x,self.y+(self.height/2))
      

cards = {
  2: { "hearts": Card(0,0, "Heart", 2),
  "spades": Card(0,0, "Spade", 2),
  "diamonds": Card(0,0, "Diamond", 2),
  "clubs": Card(0,0, "Club", 2),
    
  },
  
  3: { "hearts": Card(0,0, "Heart", 3),
  "spades": Card(0,0, "Spade", 3),
  "diamonds": Card(0,0, "Diamond", 3),
  "clubs": Card(0,0, "Club", 3),
    
  },
   4: { "hearts": Card(0,0, "Heart", 4),
  "spades": Card(0,0, "Spade", 4),
  "diamonds": Card(0,0, "Diamond", 4),
  "clubs": Card(0,0, "Club", 4),
    
  },
  5: { "hearts": Card(0,0, "Heart", 5),
  "spades": Card(0,0, "Spade", 5),
  "diamonds": Card(0,0, "Diamond", 5),
  "clubs": Card(0,0, "Club", 5),
    
  },
  
  6: { "hearts": Card(0,0, "Heart", 6),
  "spades": Card(0,0, "Spade", 6),
  "diamonds": Card(0,0, "Diamond", 6),
  "clubs": Card(0,0, "Club", 6),
    
  },
  7: { "hearts": Card(0,0, "Heart", 7),
  "spades": Card(0,0, "Spade", 7),
  "diamonds": Card(0,0, "Diamond", 7),
  "clubs": Card(0,0, "Club", 7),
    
  },
  8: { "hearts": Card(0,0, "Heart", 8),
  "spades": Card(0,0, "Spade", 8),
  "diamonds": Card(0,0, "Diamond", 8),
  "clubs": Card(0,0, "Club", 8),
    
  },
  9: { "hearts": Card(0,0, "Heart", 9),
  "spades": Card(0,0, "Spade", 9),
  "diamonds": Card(0,0, "Diamond", 9),
  "clubs": Card(0,0, "Club", 9),
    
  },
  10: { "hearts": Card(0,0, "Heart", 10),
  "spades": Card(0,0, "Spade", 10),
  "diamonds": Card(0,0, "Diamond", 10),
  "clubs": Card(0,0, "Club", 10),
    
  },
  11: { "hearts": Card(0,0, "Heart", 10),
  "spades": Card(0,0, "Spade", 10),
  "diamonds": Card(0,0, "Diamond", 10),
  "clubs": Card(0,0, "Club", 10),
    
  },
  12: { "hearts": Card(0,0, "Heart", 10),
  "spades": Card(0,0, "Spade", 10),
  "diamonds": Card(0,0, "Diamond", 10),
  "clubs": Card(0,0, "Club", 10),
    
  },
  13: { "hearts": Card(0,0, "Heart", 10),
  "spades": Card(0,0, "Spade", 10),
  "diamonds": Card(0,0, "Diamond", 10),
  "clubs": Card(0,0, "Club", 10),
    
  },
   14: { "hearts": Card(0,0, "Heart", [11,1]),
  "spades": Card(0,0, "Spade", [11,1]),
  "diamonds": Card(0,0, "Diamond", [11,1]),
  "clubs": Card(0,0, "Club", [11,1]),
    
  },
  

  
  
}


def addText(string, x, y, size,r,g,b):
  textSize(size)
  fill(r,g,b)
  return text(string,x,y)
  
  

def drawAll(items, shape):
  for i in xrange(len(items)):
    items[i].draw(shape)
  
def mouseCollision(a, b, radius):
  if a.x < b.x+radius+a.width and a.x+a.width > b.x+a.width and a.y < b.y+radius and a.height+ a.y> b.y:
    return True
  else:
    return False

def showDeck(items):
   for i in range(len(items)):
    items[i].x = i*4
  

def drawPlayer(items, shape, x, y, isPlayer):
  for i in xrange(len(items)):
    items[i].draw(shape)
    items[i].x = i*x/5
    items[i].y = y
    if isPlayer:
      items[i].isFlipped = True
      items[i].addText()
    

def button(x,y, width, height, text):
  addText(text,x+(width/2), y+(height/2), 16, 255,255,255)
  fill(147, 86, 175)
  return rect(x,y, width, height)
    

def mouseClicked():
  stay.mouseEvent(mouse)
  for i in xrange(len(deck)):
    if mouseCollision(deck[i], mouse, 0):
      deck[i].isFlipped = True
      deck[i].y = 100
      return
      


def createDeck(items):
  for i in xrange(2,14):
    for j in xrange(4):
      items.append(cards[i][suit[j]])
  return items

def label():
  for i in range(len(deck)):
    if deck[i].isFlipped:
      deck[i].addText()




hit = Button(200,200, 100,50, "HIT")
stay = Button(200, 300, 100,50, "STAY")





createDeck(deck)
game.shuffle()
game.deal()
game.score()
def update():
  background(9, 155, 31)
  stay.draw()
  hit.draw()
  stay.buttonText()
  hit.buttonText()
  showDeck(deck)
  drawAll(deck, 'rect')
  drawPlayer(game.player, "rect", 250,250, True)
  drawPlayer(game.computer, "rect", 100,100, False)
  label()
  addText("Blackjack", 275,275, 25, 255,255,255)

 
  


draw = update
run()