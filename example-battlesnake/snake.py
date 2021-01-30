from utility import *

class Snake():
	
    def __init__(self, snake):
        self.id = snake['id'] 
        self.age = snake['age']
        self.health = snake['health']
        self.status = snake['status']
        self.coordinates = snake['coords']
        self.head = self.coordinates[0]
        self.length = len(self.coordinates)
        
    def shouldAttack(self, enemySnake):
        if self.length <= enemySnake.length:
            return False
	    
        if distanceBetweenTwoPoints(self.head, enemySnake.head) < 3:
            return True
	        
    def attackDirection(self, enemySnake):
        head = enemySnake.head
        nsdiff = head[1] - self.head[1]
        ewdiff = head[0] - self.head[0]

        if nsdiff < 0: return 'north'
        elif nsdiff > 0: return 'south'

        if ewdiff > 0: return 'east'
        elif ewdiff < 0: return 'west'

	
    def attack(self, directions, snakes):
        for snake in snakes:
            if snake.id == self.id: continue
            
            direction = self.attackDirection(snake)
            if self.shouldAttack(snake):  
                if (direction == 'north'): directions.north *= 2
                elif (direction == 'south'): directions.south *= 2
                elif (direction == 'east'): directions.east *= 2
                elif (direction == 'west'): directions.west *= 2
            
            else:
                if self.length <= snake.length and distanceBetweenTwoPoints(self.head, snake.head) < 3:
                   if (direction == 'north'): directions.north *= .1
                   elif (direction == 'south'): directions.south *= .1
                   elif (direction == 'east'): directions.east *= .1
                   elif (direction == 'west'): directions.west *= .1 
                    
        return directions
        