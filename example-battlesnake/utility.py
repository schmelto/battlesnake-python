import json
import math
import random

boardTypes = {'Empty': 0, 'Wall': 1, 'Snake_Body': 2, 'Snake_Head': 3, 'Food': 4, 'Gold':5}

def distanceBetweenTwoPoints(point1, point2):
    return  (abs((point2[0] - point1[0])) + abs((point2[1] - point1[1])))


def createBoardObject(data, snakes):
    global boardTypes
    Board = [[0 for x in range(data["height"])] for x in range(data["width"])]

    # Start off as empty
    for i in range(data["height"] - 1):
        for j in range(data["width"] - 1):
            Board[i][j] = boardTypes['Empty']

    # Find Snakes
    for snake in snakes:
        for index, point in enumerate(snake.coordinates, start=0):
            if index == 0:
                Board[point[0]][point[1]] = boardTypes['Snake_Head']
            else:
                if Board[point[0]][point[1]] != boardTypes['Snake_Head']:
                    Board[point[0]][point[1]] = boardTypes['Snake_Body']
    # Find Food
    for apple in data["food"]:
        print apple
        Board[apple[0]][apple[1]] = boardTypes['Food']

    # Find Walls
    if "walls" in data:
        for wall in data["walls"]:
            print wall
            Board[wall[0]][wall[1]] = boardTypes['Wall']
    else:
        print "No Walls object, must be a classic games"

    # Find Walls
    if "gold" in data:
        for gold in data["gold"]:
            print gold
            Board[gold[0]][gold[1]] = boardTypes['Gold']
    else:
        print "No Walls object, must be a classic games"

    return Board

def getTaunt():
    bieberqoutes = ['I make mistakes growing up. I\'m not perfect; I\'m not a robot. -Justin Bieber', 'I\'m crazy, I\'m nuts. Just the way my brain works. I\'m not normal. I think differently. -Justin Bieber', 'Friends are the best to turn to when you\'re having a rough day. -Justin Bieber', 'I leave the hip thrusts to Michael Jackson. -Justin Bieber', 'It\'s cool when fans spend so much time making things for me. It means a lot. -Justin Bieber', 'No one can stop me. -Justin Bieber']
    
    return random.choice(bieberqoutes)

def whichSnake(point, snakes):
    for snake in snakes:
        for snakePoint in snake.coordinates:
            if point == snakePoint:
                return snake.id
                
def getSelf(snakes, snakeId):
    for snake in snakes:
        if snake.id == snakeId:
            return snake

    return False