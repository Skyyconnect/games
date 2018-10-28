from randfrom random import randint
from processing import *

#PLUMMET 
height = 400
width = 400
inGame = True
#sprites is used to store sprites and draw them all.
sprites = []
platforms = []
smallPlatforms = []
score = 0


  
# Entity (player and plaform sprites)
class Entity:
  def __init__(self, x , y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    
  def draw(self, shape):
    if shape == "circle":
      return ellipse(self.x, self.y, self.width, self.width)
    else:
      return rect(self.x, self.y, self.width, self.height)
    
  def color(self, r, g, b):
    return fill(r, g, b)
 
# defines player  
player = Entity(50, 50, 20, 20)
sprites.append(player)  

# generates an entity
def platform(x, y):
  return Entity(x, y, 300,30)

# platforms on the left side
def insertPlatforms(x,y,w,h,n):
  for i in range(n):
    smallPlatforms.append(Entity(x,y,w,h))
    

# makes the platforms
def genPlatforms(x,y,n):
  for i in range(n):
    platforms.append(platform(x,y))
    x+= randint(-80,80)
    y+= randint(60,90)

def collision(a,b):
  if a.x < b.x + b.width and a.x + a.width > b.x and a.y < b.y + b.height and a.height + a.y > b.y:
    return True
  else:
    return False
# randomly moves square after touching it 
def moveSmallPlatforms(item,obj):
  chance = randint(0,1)
  for i in range(len(item)):
    item[i].y -= 3
    if item[i].y <= 0:
      item[i].y = height
    if collision(item[i],obj):
      if chance == 1:
        item[i].x -= 10
      else:
        item[i].x += 10
      obj.y = (item[i].y-obj.width)




# move and randomize the platform. Add score too 
def movePlatforms(item,obj):
  global score
  for i in range(len(item)):
    item[i].y -= 2
    if item[i].y <= 0:
      score+=1
      item[i].x = randint(0,200)
      item[i].y = height
    if collision(item[i],obj):
      
      obj.y = (item[i].y-obj.width)+8
    
# creates the screen and sets framerate   
def setup():
  frameRate(60)
  size(width, height)

# add red text
def addText(string, x, y, size):
  textSize(size)
  fill(255,0,0)
  return text(string, x,y)



#changes the level speed and toughness based on score. 
def level():
  if score >=25 and score <50 : 
    return 2
  if score >= 50 and score <75:
    return 3
  if score > 75:
    return 4
  else:
    return 1
 
# movement for player  
def move(speed):
  global inGame
  key = keyboard.keyCode
  player.y += 5
  
  if key == 68 or key == 39 :
    player.x += speed
  if key == 65 or key == 37:
    player.x -= speed
    

 # stops ball from coming off screen   
  if player.x >= width:
    player.x = width
  if player.x <= 0:
    player.x = 0
  if player.y >= height:
    player.y = height
  if player.y <= 0:
    inGame = False
    player.y = 0

# draws all the sprite-lists  
def drawSprites(item,shape):
  for i in xrange(len(item)):
    item[i].draw(shape)
    
# make platforms  
insertPlatforms(0,0,50,50,5)   
genPlatforms(50,height,5)   

 # game engine
def engine():
  global player, sprites, inGame, score
  if inGame:
    background(0)
    fill(76, 238, 247)
    drawSprites(sprites, "circle")
    drawSprites(platforms,"rect")
    drawSprites(smallPlatforms,"rect")
    movePlatforms(platforms,player)# collision is in here
    moveSmallPlatforms(smallPlatforms,player)
    move(7)
    addText("Score: "+str(score),20,30,25)
  else:
    addText("Game Over",width/10,height/2, 50)
   
    
    
# processing call
draw = engine
run()
