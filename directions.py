class Directions:
    def __init__(self):
        self.up = 100
        self.down = 100
        self.right = 100
        self.left = 100

    def checkForOwnBody(self, data, directions, mySnake):

        snake_head = mySnake.head
        snake_body = mySnake.body

        for pointInBody in snake_body:

            if snake_head["x"] == pointInBody["x"] - 1 and snake_head["y"] == pointInBody["y"]:
                directions.right = 0
            if snake_head["x"] == pointInBody["x"] + 1 and snake_head["y"] == pointInBody["y"]:
                directions.left = 0
            if snake_head["y"] == pointInBody["y"] - 1 and snake_head["x"] == pointInBody["x"]:
                directions.up = 0
            if snake_head["y"] == pointInBody["y"] + 1 and snake_head["x"] == pointInBody["x"]:
                directions.down = 0

        print("up ", self.up)
        print("down ", self.down)
        print("left ", self.left)
        print("right ", self.right)
        return directions

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