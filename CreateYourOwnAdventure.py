'''
Instructions:

The game runs based on the configuration dictionaries defined bellow. Each 
configuration dictionary defines a function to perform in the game. The configuration
dictionaries are interpreted by the parser which then runs their corisponding function. 

The world is event based, so if you can call a function that has its own command loop.
'''

'''
Each configuration dictionary can contain synonyms, for example move, go, travel.
'''

import types

from config import Config


# experimentDict = {
# 	"synonyms":{
# 		"describe":experimentDict["actions"]["describe"],
# 		"narrate":experimentDict["actions"]["describe"],
# 	},
# 	"actions":{
# 		"describe":{
# 			"location":self.grid.describeLocation,
# 		},
# 	},
# }

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
		self.populateMap()

	#Populates the map based on the programers configuration list.
	def populateMap(self):
		print("STUB")

	def addSpace(self, x,y,z,space):
		self.insertAtPostition(x = x, y = y, z = z, spaceObject = space)

	def incrementXPosUp(self,param):

			self.currentLocation["x"] += 1
			if not self.checkBounds():
				self.currentLocation["x"] -= 1
				print("Can't move in that direction. Sorry.")

			

			spaceObject = Space("mountan")
			self.insertAtPostition(x = self.currentLocation["x"],
				y = self.currentLocation["y"], z = self.currentLocation["z"], 
				spaceObject = spaceObject)



	def incrementXPosDown(self,param):
		self.currentLocation["x"] -= 1
		if not self.checkBounds():
			self.currentLocation["x"] += 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)


	def incrementYPosUp(self,param):
		self.currentLocation["y"] += 1
		if not self.checkBounds():
			self.currentLocation["y"] -= 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementYPosDown(self,param):
		self.currentLocation["y"] -= 1
		if not self.checkBounds():
			self.currentLocation["y"] += 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementZPosUp(self,param):
		self.currentLocation["z"] += 1
		if not self.checkBounds():
			self.currentLocation["z"] -= 1
			print("Can't move in that direction. Sorry.")

		spaceObject = Space("mountan")
		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"], 
			spaceObject = spaceObject)

	def incrementZPosDown(self,param):
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

	def describeLocation(self, param):
		print("At location of type "+ self.getCurrentSpaceObject().type +
				" at coordinants: " + str(self.currentLocation) )


class Param():
	def __init__(self, args=None):
		self.args = args

class Game():
	def __init__(self):

		startSpace = Space("room")
		self.grid = Grid(0,0,0)
		self.grid.addSpace(0,0,0, startSpace)
		self.config = Config(game=self, grid=self.grid)


	def start(self):
		print("You find yourself in an empty room, what would you like to do? ")
		loop = True
		while loop:

			loop = self.parseExperimental(commandString = input(), commandDict = self.config.mainActionMap )



	def parseExperimental(self, commandString, commandDict):
		
		#Add the local options to the globaly available options
		commandDictTemp = self.config.globalActionMap.copy()
		commandDictTemp.update(commandDict)
		commandDict = commandDictTemp


		commandList = commandString.split(" ")

		i = 0
		while i < len(commandList):
			word = commandList[i].lower()
			
			if word in commandDict:
				commandDict = commandDict[word]

			if isinstance(commandDict, types.MethodType):
				paramObj = Param(args=commandList[i:]) 
				commandDict( param = paramObj )
				break


			i += 1

		return True


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