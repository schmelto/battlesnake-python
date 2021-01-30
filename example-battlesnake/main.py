import bottle
from utility import *
from walls import *
from utility import *
from snake import *
from food import *
from gold import *
from directions import *

snakeId = "72ad0c75-244b-4e30-9169-4584cf4fee28"
boardTypes = {'Empty': 0, 'Wall': 1, 'Snake_Body': 2, 'Snake_Head': 3, 'Food': 4}

wantFood = 1
wantGold = 5

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/rbm-head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    # TODO: Do things with data

    return {
        'taunt': 'RBM is gong to win ' + str(data['game'])
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    snakes = []
    for snake in data["snakes"]:
        snakes.append(Snake(snake))
    
    mySnake = getSelf(snakes, snakeId)
    directions = Directions()
    foods = Foods(data['food'], wantFood)
    board = createBoardObject(data, snakes)

    directions = foods.goTowards(foods.amClosest(snakes, mySnake), directions, mySnake)

    if 'gold' in data:
        golds = Foods(data['gold'], wantGold)
        directions = golds.goTowards(golds.amClosest(snakes, mySnake), directions, mySnake)

    # Check for collision
    walls = Walls()
    directions = walls.wallCollision(data, directions, mySnake, snakes)
    directions = walls.snakeCollision(data, board, directions, mySnake)
    #Check for dead ends
    directions = walls.deadEndDetection(board, mySnake, directions)

    ## Check for attack opportunities
    directions = mySnake.attack(directions, snakes)




    print "Direction = " + directions.toString()

    move = directions.bestDirection()
    print "Move =" + move
    return {
        'move': move,
        'taunt': str(getTaunt())
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    print bottle.request
    # TODO: Do things with data

    return {
        'taunt': str(getTaunt())
    }





# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host='127.0.0.1', port=8080, debug=True, reloader=True)
