from cmu_cs3_graphics import *
from Collider import *
def onAppStart(app):
    Platform(0,350,400,30)
    Spike(50,100,90,10,'down')
    Collectible(150,100,10,10)
    restartApp(app)
    resetBoardModel(app)


def resetBoardModel(app):
    app.width = 900
    app.height = 600
    app.blockWidth = 30
    app.spacing = ((app.height-2*app.blockWidth)-(2*app.blockWidth))//5
    app.level1Model = []
    makeLevel1(app)


def makeLevel1(app):
    app.level1Model+=[
    Platform(app.blockWidth,app.blockWidth, app.width-2*app.blockWidth, app.blockWidth),
    Platform(app.blockWidth,app.blockWidth, app.blockWidth, app.height-2*app.blockWidth),
    Platform(app.width-3*app.blockWidth,app.blockWidth, 
            2*app.blockWidth, app.height-2*app.blockWidth),
    Platform(app.blockWidth,app.height-2*app.blockWidth,
            app.width-2*app.blockWidth, app.blockWidth),
    Platform(app.blockWidth,app.height-2*app.blockWidth,
            app.width-2*app.blockWidth, app.blockWidth, ),
    Platform(2*app.blockWidth+1.5*app.spacing,2*app.blockWidth+app.spacing,
            app.width-3*app.blockWidth-1.5*app.spacing, app.spacing, ),
    Platform(app.blockWidth,2*app.blockWidth+3*app.spacing, 
            app.width-3*app.blockWidth-1.5*app.spacing, app.spacing, ),
    Platform(app.width-4*app.blockWidth,app.height-3*app.blockWidth,
            3*app.blockWidth, app.blockWidth, ),
    Platform(app.width-4*app.blockWidth,app.height-3*app.blockWidth,
            3*app.blockWidth, app.blockWidth, ),
    Platform(app.width-5*app.blockWidth,app.height-4*app.blockWidth,
            app.blockWidth, 3, ),
    Platform(app.width-4*app.blockWidth,app.height-5*app.blockWidth,
            app.blockWidth, 3, ),
    Platform(2*app.blockWidth,2*app.blockWidth+2*app.spacing,
            app.blockWidth, 3, ),
    Platform(2*app.blockWidth+app.spacing,2*app.blockWidth+1.5*app.spacing,
            app.blockWidth, 3, ),

    Spike(app.width//2,app.height-2.5*app.blockWidth, 
            app.blockWidth//2, app.blockWidth//2,'up'),
    Spike(app.width//2-30,1.5*app.blockWidth+3*app.spacing, 
            app.blockWidth, app.blockWidth//2,'up'),
    #downfacing
    Spike(2*app.blockWidth+2*app.spacing,2*app.blockWidth, 
            app.blockWidth//2, app.blockWidth//2,'down'),

    ]
    
    
#level 1
def drawLevel1(app):
    for collider in app.level1Model:
        if isinstance(collider, Collider):
            collider.DrawCollider()

def restartApp(app):
    app.characterList = []
    getCharacter(app)

def getCharacter(app):
    newCharacter = Player(700,400,30,60)
    app.characterList.append(newCharacter)

def redrawAll(app):
    drawLevel1(app)
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



