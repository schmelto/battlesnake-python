from past.builtins import xrange

class Food():

    def __init__(self, food, wantFood):
        self.food = food
        self.want = wantFood

    def distanceToFood(self, snake):
        food = []
        head = snake.head
        for food in self.food:
            x =  head["x"] - food["x"]
            y =  head["y"] - food["y"]
            food.append(abs(x), abs(y))
        return food


    def amClosest(self, snakes, mySnake):
        myDistance = self.distanceToFood(mySnake)
        for snake in snakes:
            snakeDistance = self.distanceToFood(snake)

            for x in xrange(0,len(snakeDistance)):
                if myDistance[x] > snakeDistance[x]:
                    myDistance[x] = 100

                if myDistance[x] == snakeDistance[x]:
                    if len(snake.coordinates) > mySnake.length:
                        myDistance[x] = 100

        closest = []
        for distance in myDistance:
            if distance < 100:
                closest.append(distance)
            else:
                closest.append(-1)

        return closest

    def goTowards(self, closest, direction, mySnake):
        foodWeight = 10
        head = mySnake.head
        for x in xrange(0, len(self.food)):
            if closest[x] >= 0:
                #print "i am closest to " + str(closest[x])
                food = self.food[x]

                nsdiff = food["y"] - head["y"]

                ewdiff = food["x"] - head["x"]

                if nsdiff < 0:
                    direction.north *= (1 + foodWeight/closest[x])
                elif nsdiff > 0:
                    direction.south *= (1 + foodWeight/closest[x])
                
                if ewdiff > 0:
                    direction.east *= (1 + foodWeight/closest[x])
                elif ewdiff < 0:
                    direction.west *= (1 + foodWeight/closest[x])
        return direction