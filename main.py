from cmu_cs3_graphics import *
from Collider import *

def onAppStart(app):
    app.width = 900
    app.height = 600
    Platform(0,350,400,30)
    Spike(50,100,90,10,'down')
    Collectible(150,100,10,10)
    restartApp(app)

def restartApp(app):
    app.characterList = []
    getCharacter(app)

def getCharacter(app):
    newCharacter = Player(200,200,30,60)
    app.characterList.append(newCharacter)

def redrawAll(app):
    Collider.DrawColliders()
    for character in app.characterList:
        drawRect(character.x, character.y, character.width, character.height, fill ='red')

def onKeyHold(app,keys):
    if 'up' in keys:
        app.characterList[0].turnUp()
    if 'left' in keys and 'right' in keys:
        app.characterList[0].dx = 0
    elif 'left' in keys:
        app.characterList[0].turnLeft()
    elif 'right' in keys:
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
        collisions = character.GetCollisions()
        for collider in collisions:
            if isinstance(collider,Platform): character.onPlatform = True
            collider.OnCollision(character)

def main():
    runApp()

main()