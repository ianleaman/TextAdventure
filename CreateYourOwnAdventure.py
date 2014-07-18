

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
	def __init__(self,x,y,z):
		self.currentLocation = {
			"x":x,
			"y":y,
			"z":z,
		}
		
		self.worldBounds = {
			"x-up":None,
			"x-down":0,
			"y-up":None,
			"y-down":0,
			"z-up":0,
			"z-down":0,
		}

		self.grid = {
			0:{   #x
				0:{
					0:None
				}    #y
			}
		}
	def addSpace(self, x,y,z,space):
		self.grid[x][y][z] = space

class Game():
	def __init__(self):

		startSpace = Space("room")
		self.grid = Grid(0,0,0)
		self.grid.addSpace(0,0,0, startSpace)

		self.actionMap = {
			"up":incrementPosUp,
			"down",incrementPosDown, 
			"describe":
		}

	def start(self):
		command = "You find yourself in an empty room, what would you like to do?"
		while True:
			
			command = self.parse(input(command + " "))


	def parse(self, command):
		pass




if __name__ == '__main__':
	main()