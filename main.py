from cmu_cs3_graphics import *
from Collider import *
import Draw

def onAppStart(app):
    app.width = 900
    app.height = 600
    app.screen = None
    app.blockWidth = 30
    app.spacing = ((app.height-2*app.blockWidth)-(2*app.blockWidth))//5
    reset(app)

def reset(app):
    Collider.ClearColliders()
    Draw.MakeLevel(app)
    app.player = Player(200,470,30,60)
    app.gameOver = False

def redrawAll(app):
    if app.screen == None:
        Draw.Menu(app)
    elif app.screen == 1:
        Draw.Menu(app)
        Draw.Manual(app)
    elif app.screen == 0:
        Draw.Level()

def onKeyPress(app, key):
    if key == 'escape':
        Draw.BackToMenu(app)
        reset(app)

def onKeyHold(app,keys):
    if app.screen == 0 and not app.gameOver:
        if 'up' in keys:
            app.player.turnUp()
        if 'left' in keys and 'right' in keys:
            app.player.dx = 0
        elif 'left' in keys:
            app.player.turnLeft()
        elif 'right' in keys:
            app.player.turnRight()

def onKeyRelease(app,key):
    if app.screen == 0 and not app.gameOver:
        app.player.dx = 0

def onMousePress(app, mouseX, mouseY):
    if app.screen == None:
        app.screen = Draw.GetButton(app, mouseX, mouseY)

def onStep(app):
    takeStep(app)

def takeStep(app):
    if app.screen == 0 and not app.gameOver:
        app.player.doMove()
        collisions = app.player.GetCollisions()
        for collider in collisions:
            if isinstance(collider,Platform): app.player.onPlatform = True
            collider.OnCollision(app.player)

def main():
    runApp()

main()