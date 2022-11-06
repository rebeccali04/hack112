from cmu_cs3_graphics import *
from Collider import *

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

def BackToMenu(app):
    app.screen = None

def Level():
    Collider.DrawColliders()

def MakeLevel(app):
    Platform(app.blockWidth,app.blockWidth, app.width-2*app.blockWidth, app.blockWidth)
    Platform(app.blockWidth,app.blockWidth, app.blockWidth, app.height-2*app.blockWidth)
    Platform(app.width-3*app.blockWidth,app.blockWidth, 
            2*app.blockWidth, app.height-2*app.blockWidth)
    Platform(app.blockWidth,app.height-2*app.blockWidth,
            app.width-2*app.blockWidth, app.blockWidth)
    Platform(app.blockWidth,app.height-2*app.blockWidth,
            app.width-2*app.blockWidth, app.blockWidth, )
    Platform(2*app.blockWidth+1.5*app.spacing,2*app.blockWidth+app.spacing,
            app.width-3*app.blockWidth-1.5*app.spacing, app.spacing, )
    Platform(app.blockWidth,2*app.blockWidth+3*app.spacing, 
            app.width-3*app.blockWidth-1.5*app.spacing, app.spacing, )
    Platform(app.width-4*app.blockWidth,app.height-3*app.blockWidth,
            3*app.blockWidth, app.blockWidth, )
    Platform(app.width-4*app.blockWidth,app.height-3*app.blockWidth,
            3*app.blockWidth, app.blockWidth, )
    Platform(app.width-5*app.blockWidth,app.height-4*app.blockWidth,
            app.blockWidth, 3, )
    Platform(app.width-4*app.blockWidth,app.height-5*app.blockWidth,
            app.blockWidth, 3, )
    Platform(2*app.blockWidth,2*app.blockWidth+2*app.spacing,
            app.blockWidth, 3, )
    Platform(2*app.blockWidth+app.spacing,2*app.blockWidth+1.5*app.spacing,
            app.blockWidth, 3, )

    Spike(app.width//2,app.height-2.5*app.blockWidth, 
            app.blockWidth//2, app.blockWidth//2,'up')
    Spike(app.width//2-30,1.5*app.blockWidth+3*app.spacing, 
            app.blockWidth, app.blockWidth//2,'up')
    #downfacing
    Spike(2*app.blockWidth+2*app.spacing,2*app.blockWidth, 
            app.blockWidth//2, app.blockWidth//2,'down')