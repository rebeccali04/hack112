from cmu_cs3_graphics import *

class Collider:
    colliders = set()
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        Collider.colliders.add(self)
    
    def __repr__(self):
        return f'Collider({self.x}, {self.y}, {self.width}, {self.height})'
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        return (isinstance(other,Collider) and
                (self.x, self.y, self.width, self.height) ==
                (other.x, other.y, other.width, other.height))

    def GetCollisions(self): #this should only be called by moveable colliders
        collisions = set()
        for other in Collider.colliders:
            if other == self: continue
            if self.RectanglesOverlap(other):
                collisions.add(other)
        return collisions

    @staticmethod
    def DrawColliders():
        for collider in Collider.colliders:
            collider.DrawCollider()

    @staticmethod
    def ClearColliders():
        Collider.colliders = set()

    def OnCollision(self, other):
        pass

    def DrawCollider(self):
        pass

    def RectanglesOverlap(self, other):
        left1, top1, width1, height1 = self.x, self.y, self.width, self.height
        left2, top2, width2, height2 = other.x, other.y, other.width, other.height
        right1 = left1 + width1
        right2 = left2 + width2
        bottom1 = top1 + height1
        bottom2 = top2 + height2
        if (right1 < left2 or right2 < left1 or
            bottom1 < top2 or bottom2 < top1): return False
        else: return True


class Player(Collider):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 0
        self.dy = 1 #change back to 1
        self.jumpMax = 30
        self.jumpVal = 0
        self.defaultDy = 1#this is moving down
        self.isJumping = False
        self.points = 0
        self.onPlatform = True
        self.spawnX = x
        self.spawnY = y
    
    def DrawCollider(self):
        drawRect(self.x, self.y, self.width, self.height, fill='red')

    def respawn(self):
        self.x = self.spawnX
        self.y = self.spawnY
        self.points = 0
    
    def turnLeft(self):
        self.dx = -2

    def turnRight(self):
        self.dx = 2

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
            self.dy = -1 #jump speed 
    
    def doMove(self):
        if self.jumpVal>0:
            self.doJump()
        else:
            self.dy = self.defaultDy #not jumping? always same dy
        
        self.x+=self.dx
        self.y+=self.dy


class Platform(Collider):
    def DrawCollider(self):
        drawRect(self.x, self.y, self.width, self.height, fill='grey')
    
    def OnCollision(self, other):
        # we assume that other was not colliding with self in the previous frame
        if isinstance(other,Player):
            other.y -= other.dy
            if self.RectanglesOverlap(other):
                other.y += other.dy
                other.x -= other.dx


class Collectible(Collider):
    def DrawCollider(self):
        cx, cy = self.x + .5*self.width, self.y + .5*self.height
        r = 1.5 * max(self.width, self.height)
        drawStar(cx, cy, r, 5, fill='blanchedalmond', border='black', roundness=60)
    
    def OnCollision(self, other):
        if isinstance(other,Player):
            other.points += 1
            Collider.colliders.discard(self)


class Spike(Collider):
    def __init__(self,x,y,width,height,direction):
        super().__init__(x,y,width,height)
        self.direction = direction

    def DrawCollider(self):
        if self.direction == 'up' or self.direction == 'down':
            numOfSpikes = self.width//10 + 1
            x = self.x - (10 * numOfSpikes - self.width)/2
            if self.direction == 'up':
                for i in range(numOfSpikes):
                    drawPolygon(x+10*i, self.y+self.height,
                                x+10*i+5, self.y,
                                x+10*(i+1), self.y+self.height,
                                fill='white', border='black')
            else:
                for i in range(numOfSpikes):
                    drawPolygon(x+10*i, self.y,
                                x+10*i+5, self.y+self.height,
                                x+10*(i+1), self.y,
                                fill='white', border='black')
        elif self.direction == 'left' or self.direction == 'right':
            numOfSpikes = self.height//10 + 1
            y = self.y - (10 * numOfSpikes - self.height)/2
            if self.direction == 'left':
                for i in range(numOfSpikes):
                    drawPolygon(self.x+self.width, y+10*i,
                                self.x, y+10*i+5,
                                self.x+self.width, y+10*(i+1),
                                fill='white',border='black')
            else:
                for i in range(numOfSpikes):
                    drawPolygon(self.x, y+10*i,
                                self.x+self.width, y+10*i+5,
                                self.x, y+10*(i+1),
                                fill='white',border='black')

    def OnCollision(self, other):
        if isinstance(other,Player):
            other.respawn()


class Goal(Collider):
    def __init__(self,app,x,y,width,height):
        super().__init__(x,y,width,height)
        self.app = app
    
    def DrawCollider(self):
        cx, cy = self.x + .5*self.width, self.y + .5*self.height
        r = 1.5 * max(self.width, self.height)
        drawCircle(cx, cy, r, fill='orange')

    def OnCollision(self, other):
        if isinstance(other,Player):
            self.app.gameOver = True