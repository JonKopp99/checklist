# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import turtle
import random
from turtle import *
import tkSimpleDialog
t = turtle.Pen() #Graphics!
turns = 0 #Global user turns var
guesses = [] #List of user guesses!

#Start scene
screen = turtle.Screen()
screen.setup(600, 600)
image = '7.gif'
screen.addshape(image)
turtle.shape(image)

'''
    createSecretWord = Creates the secret word for user to guess. Picks from all english words in the dict
    @return returns a random word in the english dictionary
'''
def createSecretWord():
    ogword = [line.strip() for line in open('/usr/share/dict/words')]
    theword = random.choice(ogword)
    #print(theword)
    return theword

'''
    dGraphics = draws the graphics for the entire space man game
    @param theTurns = how many turns the user has used
    @param tword = the secret word!
    @post = Draw everything that needs to be drawn!
'''
def dGraphics(theTurns,tword):

    screen.reset()

    image = (str(theTurns)+".gif")
    screen.addshape(image)
    turtle.shape(image)
    screen.bgpic(image)
    turtle.color('blue')
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.setpos(-50.0,-200.0)
    turtle.write(guesses, font=("Arial", 16, "normal"))
    turtle.backward(60)
    turtle.write("Strikes: "+str(theTurns), font=("Arial", 12, "normal"))
    turtle.forward(60)
    wordToDisplay = ""
    for char in tword:
        if char in guesses:
            wordToDisplay+=char
        else:
            wordToDisplay+=" _ "
    turtle.backward(240)
    turtle.write(str(wordToDisplay), font=("Arial", 16, "normal"))
    turtle.forward(300)


'''
    winner = Gives prompt saying you win and restarts with a new game
'''
def winner():
    win = tkSimpleDialog.askstring("YOU WON!!!", "Press OK to continue!")
    if(win != ""):
        startGame()

'''
    looser = Gives prompt saying you took an L and restarts with a new game
    @param theword = the secret word
'''
def loser(theword):
    l = tkSimpleDialog.askstring("YOU LOST:((()))", "Word was: " + theword)
    if(l != ""):
        startGame()
'''
    testInput = Checks for valid input
    @param theInp = what we are checking to see is valid or nah
    @return return true/false based on valid or nah
'''
def testInput(theInp):
    try:
        theInp.decode('ascii')
    except UnicodeDecodeError:
        return False
    if (len(theInp)!=1):
        return False
    elif(theInp.isdigit()):
        return False
    elif(theInp in guesses):
        return False
    else:
        return True
'''
    theguess() = prompts user for input then adds it to the guesses list.
    @return returns the user input!
'''
def theguess():
    guess = tkSimpleDialog.askstring("Press ESC to exit.", "Enter a letter!")
    while(testInput(guess)==False):
        guess = tkSimpleDialog.askstring("Press ESC to exit.", "Enter a letter!")

    guesses.append(guess)
    return guess



'''
    startGame = Main method. Checks to see if user input is inside secret word
                updates f based on right/wrong input. If turns = 0 U LOOSE!

'''
def startGame():
    turns = 7
    word = createSecretWord()
    while turns >= 0:
        fail = 0
        for char in word:
            dGraphics(turns,word)
            if char in guesses:
                print
            else:
                fail += 1

        if fail == 0:
            winner()
            word = createSecretWord()
            del guesses[:]
            fail = 0
            turns = 7
            dGraphics(turns,word)

        guess=theguess()
        dGraphics(turns,word)
        if guess not in word:
            turns -= 1
            if turns < 0:
                del guesses[:]
                loser(word)
                word = createSecretWord()
                fail = 0
                turns = 7
                dGraphics(turns,word)

startGame()
