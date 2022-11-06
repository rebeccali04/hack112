from cmu_cs3_graphics import *

class Collider:
    colliders = set()
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.dx = self.dy = 0
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

class Platform(Collider):
    def DrawCollider(self):
        drawRect(self.x, self.y, self.width, self.height, fill='grey')
    
    def OnCollision(self, other):
        # we assume that other was not colliding with self in the previous frame
        if isinstance(other,Collider):
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
        app.direction = direction

    def DrawSpike(self):
        numOfSpikes = self.width//10 + 1
        for i in range(numOfSpikes):
            pass
            #drawPolygon()

    def OnCollision(self, other):
        if isinstance(other,Player):
            other.respawn()

class Goal(Collider):
    def OnCollision(self, other):
        if isinstance(other,Player):
            self.app.gameOver = True