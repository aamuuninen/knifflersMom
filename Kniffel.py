from random import randint


# This class rolls a dice and outputs a Number between 1 and 6
class Dice():
    def __init__(self):
        self.result = None

    def roll(self):
        self.result = randint(1, 6)
        return self.result


# This class stores all the data on the game that is currently
# ongoing.
class Scorecard():
    def __init__(self):
        # Which round of the game are we in?
        self.round = 0
        # Store the last dice roll result
        self.latestRoll = [0] * 5
        # Scores are kept in these variables
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.bonus = 0
        self.threeok = 0
        self.fourok = 0
        self.fullhouse = 0
        self.smallstreet = 0
        self.largestreet = 0
        self.kniffel = 0
        self.chance = 0

    def playTurn(self):
        dice = Dice()
        for i in range(5):
            self.latestRoll[i] = dice.roll()
        print 'Result of roll was: ' + str(self.latestRoll)


test = Scorecard()
test.playTurn()
