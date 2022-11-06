
######################
class Player(Collider):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 1 #change back to 1
        self.jumpMax = 10
        self.jumpVal = 0
        self.defaultDy = 1 #this is moving down
        self.isJumping = False
        self.point =0
        self.onPlatform = True
    
    def turnLeft(self):
        self.dx = -1

    def turnRight(self):
        self.dx = 1

    #called by key press up 
    def turnUp(self):
        #if not already in jump motion, jump 
        if self.onPlatform:
            self.jumpVal = self.jumpMax
            self.onPlatform = False
        
        
    def doJump(self):
        
        #we know we're jumping rn, jump val starts at 10
        self.jumpVal-=1
        if self.jumpVal >0:
            self.dy = -1 
        
            
    
    def doMove(self):
        if self.jumpVal>0:
            self.doJump()
        else:
            self.dy = self.defaultDy #not jumping? always same dy
        
        self.x+=self.dx
        self.y+=self.dy 



    




