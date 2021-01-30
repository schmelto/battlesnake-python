class Directions:
    def __init__(self):
        self.north = 100
        self.south = 100
        self.east = 100
        self.west = 100

    def toString(self):
        return 'N:'+str(self.north) + 'S:'+str(self.south) + 'E:'+str(self.east) + 'W:'+str(self.west)

    def bestDirection(self):
        bestDir = "north"
        bestVal = 0

        if self.north > bestVal:
            bestVal = self.north
            bestDir = "north"

        if self.south > bestVal:
            bestVal = self.south
            bestDir = "south"

        if self.east > bestVal:
            bestVal = self.east
            bestDir = "east"

        if self.west > bestVal:
            bestVal = self.west
            bestDir = "west"

        return bestDir