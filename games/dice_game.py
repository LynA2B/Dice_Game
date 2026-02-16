import random

class DiceGame: # contains all rules and logic for dice game
    def __init__(self): 
        self.turn = 1 # game starts on turn 1
        self.point = None # point is only set after the first roll
        self.finished = False # becomes true when game ends
        self.result = "" # describes what happens after each roll 
    
    def roll_dice(self):
        return random.randint(2 ,12) # roll a random number between 2 and 12
    
    def is_valid_roll(self, roll):
        return 2 <= roll <= 12 # check if roll is between 2 and 12
    
    def play_turn(self, roll):
        if self.finished: # if game is over, do nothing
            self.result = "The game is already finished"
            return
        
        if not self.is_valid_roll(roll): # check if roll is valid
            self.result = "Error: Roll must be between 2 and 12."
            return
        
        # first turn rules
        if self.turn == 1: # losing rolls on turn 1 
            if roll in (2, 3, 12):
                self.result = f"Roll {roll}: You lose!"
                self.finished = True

            elif roll in (7, 11): # winning rolls on turn 1
                self.result = f"Roll {roll}: You win!"
                self.finished = True

            else: # any other roll becomes a point
                self.point = roll
                self.result = f"Roll {roll}: Point is now {self.point}."
                self.turn += 1 # move to next turn

            return # end of first turn logic
        
        #rules for turn 2 and so fourth
        if roll == 7: #rolling a 7 after the first turn means you lose
            self.result = f"Roll {roll}: You lose!"
            self.finished = True

        elif roll == self.point: # rolling your point means you win 
            self.result = f"Roll {roll}: You win!"
            self.finished = True

        else: # any other roll means the game continues
            self.result = f"Roll {roll}: No win  or loss. Keep going."
            self.turn += 1
        
        


