#SNAKE LUDO

import random

class Player():
    def __init__ (self, name):
        self.name = name
        self.currentPosition = 0 
        
    def move (self):
         #ROLLING THE DICE
         input("Press Enter key to roll the dice, " + self.name)
         value = random.randint(1,6)
         print ("The dice rolled " + str(value))
         
         #ROLLING A ONE TO START THE GAME
         if (self.currentPosition == 0 and value!=1):
             print ("Sorry, you need to roll a 1 to start the game.")
         elif (value + self.currentPosition > 100):
             print ("Sorry, this is an invalid move.")
         else:
             self.position(value)
    
    def position (self, increment):
        
        #NORMAL MOVES
        self.currentPosition += increment 
        print ("Your current position is " + str(self.currentPosition))
               
        #LADDERS
        if (self.currentPosition == 6):
            print ("Congratulations! You have reached a ladder!")
            self.currentPosition = self.currentPosition + 10
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 8):
            print ("Congratulations! You have reached a ladder!")
            self.currentPosition = self.currentPosition + 33
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 26):
            print ("Congratulations! You have reached a ladder!")
            self.currentPosition = self.currentPosition + 3
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 50):
            print ("Congratulations! You have reached a ladder!")
            self.currentPosition = self.currentPosition  + 43
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 59):
            print ("Congratulations! You have reached a ladder!")
            self.currentPosition = self.currentPosition + 25
            print ("Your current position is " + str(self.currentPosition))
            
        #SNAKES
        if (self.currentPosition == 32):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 20
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 60):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 22
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 63):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 60
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 70):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 45
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 73):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 26
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 82):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 39
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 89):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 36
            print ("Your current position is " + str(self.currentPosition))
        elif (self.currentPosition == 97):
            print ("Oh no! You have reached a snake!")
            self.currentPosition = self.currentPosition - 85
            print ("Your current position is " + str(self.currentPosition))
         
#==========================================================

print ("Welcome to Snake Ludo!")

#INPUTTING THE NUMBER OF PLAYERS
count = 0
while (count >= 0):
    try:
        num_of_players = int(input("Please enter the number of players: "))
        if (num_of_players == 2):
            print ("Let's start!")
            break
        else: 
            print ("You need two players to start the game!")
            continue
    except:
        print ("Please enter a valid number.")

#TAKING NAMES
names = []
count = 0
while (count >= 0 and count < num_of_players):
    names.append (Player(input("Please enter the name of the player " + str(count+1) + ": ")))
    print ("Hello! " + names[count].name)
    count += 1

#FINAL CONDITIONS
winCondition = False
while True:
    for count in names:
        count.move()
        if (count.currentPosition == 100):
            print ("You have won the game, " + count.name)
            winCondition = True
            break        
    if winCondition:
        break