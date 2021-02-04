class Walls():

    def wallCollision(self, game_json, direction, mySnake):

        # while the head of the snake is to far away from the wall only return the given direction
        snake_head = mySnake.head
        if len(snake_head) < 2:
            return direction

        # get the parameters of the board
        width = game_json["board"]["width"]
        height = game_json["board"]["height"]

        if snake_head["x"] == 0:  # head on left side, don't go left
            direction.left = 0
            # direction.right -= 1

        if snake_head["x"] == width - 1:  # head on right side, don't go right
            direction.right = 0
            # direction.left -= 1

        if snake_head["y"] == 0:  # head on bottom, dont go down
            direction.down = 0
            # direction.up -= 1

        if snake_head["y"] == height - 1:  # head on top side, don't go up
            direction.up = 0
            # direction.down -= 1

        return direction
    
    def deadEndDetection(self, data, direction, mysnake):

        return direction

    #     head = mySnake["head"]
    #     board = data["board"]

    #     leftOfHead = head["x"] - 1
    #     rightOfHead = head["x"] + 1
    #     aboveHead = head["y"] - 1
    #     belowHead = head["y"] + 1

    #     deadEndDetectedUp = True
    #     deadEndDetectedDown = True
    #     deadEndDetectedLeft = True
    #     deadEndDetectedRight = True

    #     distanceToBlockUp = 0
    #     distanceToBlockDown = 0
    #     distanceToBlockLeft = 0
    #     distanceToBlockRight = 0

    #     # Check dead and top (up)


        
