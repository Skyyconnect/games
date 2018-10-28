from random import randint
import os 

wordList = ["apple", "tree", "house", "bluewhale", "chemistry", "math", "physics", "alphabet", "application", "ghost", "gunner", "gate  "]
bodyParts = 0
correct = []
incorrect = []
blank = []
inGame = True

def pickWord(words):
  return words[randint(0, len(wordList)-1)]
  
  
def hangmanDraw():
  head = "0"
  body = "|"
  armL = "/"
  armR = "\\"
  legL = "/"
  legR = "\\"
  
  
  if bodyParts == 1:
    print "   |-----|"
    print "   "+head+"     |"
    print "         |"
    print "         | "
    print "       --|--"
    
    
  elif bodyParts == 2:
    print "   |-----|"
    print "   "+head+"     |"
    print "  "+armL+body+"     |"
    print "         | "
    print "       --|--"
    
    
  elif bodyParts == 3:
    print "   |-----|"
    print "   "+head+"     |"
    print "  "+armL+body+armR+"    |"
    print "         | "
    print "       --|--"
    
    
  elif bodyParts == 4:
    print "   |-----|"
    print "   "+head+"     |"
    print "  "+armL+body+armR+"    |"
    print "  "+legL+"      |"
    print "       --|--"
    
    
  elif bodyParts == 5:
    print "   |-----|"
    print "   "+head+"     |"
    print "  "+armL+body+armR+"    |"
    print "  "+legL+" "+legR+"    |"
    print "       --|--"
  
  else:
    print "   |-----|"
    print "         |"
    print "         |"
    print "         | "
    print "       --|--"
    
  
def pickWord(words):
  return words[randint(0, len(wordList)-1)]

def blankyBlank(word):
  for i in range(len(word)):
    blank.append("_")
  return blank







word = pickWord(wordList)
blankyBlank(word)

print "-------------"
print "| hangman |"
print "-------------"

while bodyParts <=5 and inGame:
  hangmanDraw()

  print " ".join(blank)
  print "_________________"
  print "incorrect: " + " ".join(incorrect)
  print "_________________"
   
  into = input("guess a letter:")
  
  
  if into == "guess":
    makeGuess(word)
  else:
    
    if len(into) > 1:
      into = into[0]
      
    if into in word and (into not in correct):
      correct.append(into)
    else:
      bodyParts += 1
      incorrect.append(into)
   
  
   
  
  for i in range(len(correct)):
    for j in range(len(word)):
      if correct[i] == word[j]:
        blank[j] = correct[i]
        
  
  if bodyParts > 5:
    print " The word was " + word
    print "you lose. Try again. You need more practice!"
  
  else:
    count = 0
    if inGame:
      for i in range(len(blank)):
        if blank[i] != "_":
            count += 1
            if count == len(word):
              hangmanDraw()
              print "You Win"
              print " The word was " + word
              inGame = False
  if inGame:
    os.system("clear")
          