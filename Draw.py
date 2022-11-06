from cmu_cs3_graphics import *

def onAppStart(app):
    app.blockWidth = 30
    app.width = 900
    app.height = 600
    app.screen = None

def Menu(app):
    drawLabel('OH Dash!', app.width/2, 125,
              align='center', fill='blue', size=60)
    drawLabel('A Hack112 Game', app.width/2, 175,
              align='center', fill='blue', size=20)

    drawRect(app.blockWidth, app.blockWidth, app.width-2*app.blockWidth,
            app.height-2*app.blockWidth, fill=None, border='blue')
    
    for i in range(2):
        label = GetButtonLabel(i)
        drawRect(app.width/2+4, 274+75*i, 175, 60,
                fill='turquoise', border=None, align='center')
        drawRect(app.width/2, 270+75*i, 175, 60,
                fill=None, border='blue',align='center', dashes=True)
        drawLabel(label,app.width/2, 271+75*i,
                align='center', fill='blue', size=25)

def GetButtonLabel(i):
    if i == 0:
        return 'Play'
    elif i == 1:
        return 'Manual'
    elif i == 2:
        return 'Settings'

def GetButton(app, mouseX, mouseY):
    if app.width/2+4-175/2<mouseX<app.width/2+4+175/2:
        for i in range(2):
            if 274+75*i-30/2<mouseY<274+75*i+30/2:
                return i
    return None

def Manual(app):
    drawRect(app.width/2, app.height/2+50, 350, 220,
             fill='lightblue', border='blue', align='center', dashes=True)
    drawLabel('Press left/right arrow to move', app.width/2, app.height/2,
              fill='blue', size=20)
    drawLabel('Press up arrow to jump', app.width/2, app.height/2+40,
              fill='blue', size=20)
    drawLabel('Press Esc to go back to menu', app.width/2, app.height/2+80,
              fill='blue', size=20)

def Reset(app):
    app.screen = None

def onMousePress(app, mouseX, mouseY):
    if app.screen == None:
        app.screen = GetButton(app, mouseX, mouseY)

def onKeyPress(app, key):
    if key == 'escape':
        Reset(app)

def redrawAll(app):
    if app.screen == None:
        Menu(app)
    elif app.screen == 1:
        Menu(app)
        Manual(app)
    elif app.screen == 0:
        Level(app)
    
def Level(app):
    pass

def main():
    runApp()

main()