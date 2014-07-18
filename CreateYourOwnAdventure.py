

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
	def __unicode__(self):
		return "Space object of type "+ self.type  

class Grid:
	def __init__(self,x,y,z):
		self.currentLocation = {
			"x":x,
			"y":y,
			"z":z,
		}
		
		self.worldBounds = {
			"x-up":9999,  #Make none in future
			"x-down":0,
			"y-up":9999,
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

	def incrementXPosUp(self):

			self.currentLocation["x"] += 1
			if not self.checkBounds():
				self.currentLocation["x"] -= 1
				print("Can't move in that direction. Sorry.")

			

			spaceObject = Space("mountan")
			self.insertAtPostition(x = self.currentLocation["x"],
				y = self.currentLocation["y"], z = self.currentLocation["z"], 
				spaceObject = spaceObject)



	def incrementXPosDown(self):
		self.currentLocation["x"] -= 1
		if not self.checkBounds():
			self.currentLocation["x"] += 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)


	def incrementYPosUp(self):
		self.currentLocation["y"] += 1
		if not self.checkBounds():
			self.currentLocation["y"] -= 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementYPosDown(self):
		self.currentLocation["y"] -= 1
		if not self.checkBounds():
			self.currentLocation["y"] += 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementZPosUp(self):
		self.currentLocation["z"] += 1
		if not self.checkBounds():
			self.currentLocation["z"] -= 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementZPosDown(self):
		self.currentLocation["z"] -= 1
		if not self.checkBounds():
			self.currentLocation["z"] += 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def checkBounds(self):

		
		if ((self.currentLocation["x"] <= self.worldBounds["x-up"]) and (
			self.currentLocation["x"] >= self.worldBounds["x-down"]) and 
			((self.currentLocation["y"] <= self.worldBounds["y-up"]) and (
			self.currentLocation["y"] >= self.worldBounds["y-down"])) and
			((self.currentLocation["z"] <= self.worldBounds["z-up"]) and (
			self.currentLocation["z"] >= self.worldBounds["z-down"]))):
				return True
		else:
			return False

	def insertAtPostition(self, x, y,z, spaceObject):
		if x not in self.grid:
			self.grid[x] = {}
		if y not in self.grid[x]:
			self.grid[x][y] = {}
		if z not in self.grid[x][y]:
			self.grid[x][y][z] = spaceObject
			print("New Object Created")

	def getCurrentSpaceObject(self):
		x = self.currentLocation["x"]
		y = self.currentLocation["y"]
		z = self.currentLocation["z"]
		return self.grid[x][y][z]

	def describeLocation(self):
		print("At location of type "+ self.getCurrentSpaceObject().type +
				" at coordinants: " + str(self.currentLocation) )


class Game():
	def __init__(self):

		startSpace = Space("room")
		self.grid = Grid(0,0,0)
		self.grid.addSpace(0,0,0, startSpace)

		self.actionMap = {
			"move":{
				"x-up":self.grid.incrementXPosUp,
				"x-down":self.grid.incrementXPosDown,
				"y-up":self.grid.incrementYPosUp,
				"y-down":self.grid.incrementYPosDown,
				"z-up":self.grid.incrementZPosUp,
				"z-down":self.grid.incrementZPosDown,
			},
			"describe":{
				"location":self.grid.describeLocation,
			}
		}

	def start(self):
		command = "You find yourself in an empty room, what would you like to do?"
		loop = True
		while loop:

			loop = self.parse(input(command + " "))


	def parse(self, commandString):
		commandList = commandString.split(" ")

		i = 0
		while i < len(commandList):
			word = commandList[i]

			if word.lower() == "go" or word.lower() == "move" or word.lower() == "travel":
				i += 1
				word = commandList[i].lower()
				if word == "south":
					self.actionMap["move"]["x-up"]()
				elif word == "north":
					self.actionMap["move"]["x-down"]()
				elif word == "east":
					self.actionMap["move"]["y-up"]()
				elif word == "west":
					self.actionMap["move"]["y-down"]()
				elif word == "up":
					self.actionMap["move"]["z-up"]()
				elif word == "down":
					self.actionMap["move"]["z-down"]()
				else:
					print("Go " + word +"? Nah.")

			if word.lower() == "describe":
				i += 1
				# print(i, commandList )
				word = commandList[i].lower()

				if word == "location":
					self.actionMap["describe"]["location"]()


			if word.lower() == "exit()" and len(commandList) == 1:
				if input("Are you sure? There is currently no save feature. ")[:1].lower() == "y":
					return False

			i += 1
		return True







if __name__ == '__main__':
	main()