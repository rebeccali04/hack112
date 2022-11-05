class Collider:
    colliders = []
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        Collider.colliders.append([x,y,width,height])
    
    def HasCollided(self):
        for x, y, width, height in Collider.colliders:
            if Collider.rectanglesOverlap(x, y, width, height): return True
        return False
    
    @staticmethod
    def rectanglesOverlap(left1, top1, width1, height1,
                          left2, top2, width2, height2):
        right1 = left1 + width1
        right2 = left2 + width2
        bottom1 = top1 + height1
        bottom2 = top2 + height2
        if (right1 < left2 or right2 < left1 or
            bottom1 < top2 or bottom2 < top1): return False
        else: return True
