import json

class Golds():
	def __init__(self, golds, wantFood):
		print golds
		self.golds = golds
		self.want = wantFood

	def distanceToGold(self, snake):
		golds = []
		head = snake.head
		for gold in self.golds:
			x =  head[0] - gold[0]
			y =  head[1] - gold[1]
			golds.append(abs(x) + abs(y))
		return golds


	def amClosest(self, snakes, mySnake):
		myDistance = self.distanceToGold(mySnake)
		for snake in snakes:
			snakeDistance = self.distanceToGold(snake)

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
		goldWeight = 10
		head = mySnake.head
		for x in xrange(0, len(self.golds)):
			if closest[x] >= 0:
				print "i am closest to " + str(closest[x])
				gold = self.golds[x]

				nsdiff = gold[1] - head[1]

				ewdiff = gold[0] - head[0]

				if nsdiff < 0:
					direction.north *= (1 + goldWeight/closest[x])
				elif nsdiff > 0:
					direction.south *= (1 + goldWeight/closest[x])

				if ewdiff > 0:
					direction.east *= (1 + goldWeight/closest[x])
				elif ewdiff < 0:
					direction.west *= (1 + goldWeight/closest[x])
		return direction













