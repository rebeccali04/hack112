from cmu_cs3_graphics import *
from PlayerControl import Player

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
    pass

def onMousePress(app, mouseX, mouseY):
    pass
    
def main():
    runApp()

main()