from cmu_cs3_graphics import *
from Player import Player

def onAppStart(app):
    restartApp(app)

def restartApp(app):
    app.characterList = []
    getCharacter(app)

def getCharacter(app):
    newCharacter = Player(100,100)
    app.characterList.append(newCharacter)

def redrawAll(app):
    for character in app.characterList:
        drawRect(character.left, character.top, character.width, character.height, fill ='red')

def onKeyPress(app, key):
    if key =='up':
        app.characterList[0].turnUp()
        
    elif key =='left':
        app.characterList[0].turnLeft()
        

    elif key =='right':
       
        app.characterList[0].turnRight()

def onKeyRelease(app,key):
    app.characterList[0].dx = 0

def onMousePress(app, mouseX, mouseY):
    pass

def onStep(app):
    takeStep(app)

def takeStep(app):
    for character in app.characterList:
        character.doMove()

def main():
    runApp()

main()