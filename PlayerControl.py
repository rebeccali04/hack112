class Player:
    def __init__(self,top,left):
        self.top = top
        self.left = left
        self.width = 30
        self.height = 60
        self.dx = 1
        self.dy = -1
    
    def moveLeft(self):
        self.left-=self.dx

    def moveRight(self):
        self.left+=self.dx

    def moveUp(self):
        self.top+=self.dy
    
    def moveDown(self):
        self.down-=self.dy

    




