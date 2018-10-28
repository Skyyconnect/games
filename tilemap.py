from processing import *
from random import randint

WIDTH = 401
HEIGHT = 401
keyFlags = {}
tiles = []
rowSize = 20
colSize = 20

def setup():
  size(WIDTH, HEIGHT)
  frameRate(30)
  
class Tile:
  def __init__(self, x, y, color):
    self.x = x;
    self.y = y
    self.width = 20
    self.height = 20
    self.color = color
    
  def draw(self):
    if self.color == "white":
      fill(255,255,255)
    elif self.color == "green":
      fill(0,255,0)
    else:
      fill(0,0,0)
      
    return rect(self.x*rowSize, self.y*colSize, self.width, self.height)
      
      
  def keys(self):
    if ("s" in keyFlags and keyFlags["s"]) and self.y < colSize-1:
      self.y += 1
    elif ("w" in keyFlags and keyFlags["w"]) and self.y > 0:
      self.y -= 1
    elif ("d" in keyFlags and keyFlags["d"]) and self.x < rowSize-1:
      self.x += 1
    elif ("a" in keyFlags and keyFlags["a"]) and self.x > 0:
      self.x -= 1
    
      
def createTileMap(sizeCol, sizeRow):
  for col in range(sizeCol):
    for row in range(sizeRow):
      tiles.append(Tile(col, row, "white"))

def drawAll(items):
  for i in range(len(items)):
    items[i].draw()
    
    

def keyPressed():
  keyFlags[key] = True


def keyReleased():
  keyFlags[key] = False



createTileMap(colSize,rowSize)
player = Tile(0,0, "green")


def update():
  background(100,100,100)
  drawAll(tiles)
  player.draw()
  player.keys()
  
  
draw = update
run()