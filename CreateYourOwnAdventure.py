

def main():
	answer = input("Welcome to create your own text adventure. Are you ready to get started? ")
	if answer[:1].lower() == "y":
		import os
		os.system('cls' if os.name == 'nt' else 'clear')
		newGame = Game()
		newGame.start()
	else:
		print("Fine, this game doesnt need you anyway")


class Space:
	def __init__(self, spaceType):
		self.type = spaceType

class Grid:
	def __init__(self):
		self.grid = {
			0:{   #x
				0:{
					0:None
				}    #y
			}
		}
	def addSpace(x,y,z,space):
		self.grid[x][y][z] = space

class Game():
	def __init__(self):

		startSpace = Space("room")
		self.grid = Grid()
		self.grid.addSpace
		self.currentLocation = {
			"x":0
			"y":0
			"z":0
		}
		self.worldBounds = {
			"x-up":None,
			"x-down":0,
			"y-up":None,
			"y-down":0,
			"z-up":0,
			"z-down":0,
		}


	def start(self):
		input("You find yourself in an empty room, what would you like to do?")


	def parse(self, command):



actionMap = {
	"up":incrementPosUp,
	"down",incrementPosDown, 
	"describe":


}
if __name__ == '__main__':
	main()