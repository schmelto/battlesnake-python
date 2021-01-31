class Directions:
    def __init__(self):
        self.up = 100
        self.down = 100
        self.right = 100
        self.left = 100

    def bestDirection(self):
        bestDir = "up"
        bestVal = 0

        if self.up > bestVal:
            bestVal = self.up
            bestDir = "up"

        if self.down > bestVal:
            bestVal = self.down
            bestDir = "down"

        if self.right > bestVal:
            bestVal = self.right
            bestDir = "right"

        if self.left > bestVal:
            bestVal = self.left
            bestDir = "left"
        
        print("up ", self.up)
        print("down ", self.down)
        print("left ", self.left)
        print("right ", self.right)

        return bestDir