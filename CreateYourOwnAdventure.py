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

class Item:
	def __init__(self, itemType, description = None):
		 self.type = itemType
		 self.description = description

class Mob:
	def __init__(self, mobType, attack = None, defence = None):
		self.type =  mobType
		self.attack = attack
		self.defence = defence
		self.items = []

class Space:
	def __init__(self, spaceType):
		self.type = spaceType
		self.mobs = []
		self.items = []
	def __unicode__(self):
		return "Space object of type "+ self.type

	def addMob(self, mob):
		self.mobs.append(mob)

	def removeMob(self, mob):
		self.mobs.remove(mob)

	def returnMobs(self):
		return self.mobs

	def addItem(self, item):
		self.items.append(item)

	def removeItem(self, item):
		self.items.append(item)

	def returnItems(self):
		return self.items


class Grid:
	def __init__(self,x,y,z):
		self.currentLocation = {
			"x":x,
			"y":y,
			"z":z,
		}
		
		self.worldBounds = {
			"x-up":9999,  
			"x-down":-9999,
			"y-up":9999,
			"y-down":-9999,
			"z-up":0,
			"z-down":0,
		}

		self.grid = {
			0:{   #x
				0:{
					0:Space("filler")
				}    #y
			}
		}

	#Populates the map based on the programers configuration list.
	def loadMap(self, mapConfig):
		
		for space in mapConfig["spaces"]:
			try:
				spaceObject = Space(space["type"])
			except KeyError:
				continue

			for item in space["items"]:
				itemObject = Item(item["type"])
				spaceObject.addItem(itemObject)

			for mob in space["mobs"]:
				mobObject = Mob(mob["type"])
				spaceObject.addMob(mobObject)


			self.ensureGridPossition(x=space["x"] ,y=space["y"],z =space["z"])
			self.createRoom(x=space["x"] ,y=space["y"],z =space["z"] ,
				spaceObject = spaceObject, verbose = False)


	def addSpace(self, x,y,z,space):
		self.insertAtPostition(x = x, y = y, z = z, spaceObject = space)

	def incrementXPosUp(self,param):

			self.currentLocation["x"] += 1
			if not self.checkBounds():
				self.currentLocation["x"] -= 1
				print("Can't move in that direction. Sorry.")
			
			x = self.currentLocation["x"]
			self.insertAtPostition(x = x,
				y = self.currentLocation["y"], z = self.currentLocation["z"])


	def incrementXPosDown(self,param):
		self.currentLocation["x"] -= 1
		if not self.checkBounds():
			self.currentLocation["x"] += 1
			print("Can't move in that direction. Sorry.")

		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"])


	def incrementYPosUp(self,param):
		self.currentLocation["y"] += 1
		if not self.checkBounds():
			self.currentLocation["y"] -= 1
			print("Can't move in that direction. Sorry.")

		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"])

	def incrementYPosDown(self,param):
		self.currentLocation["y"] -= 1
		if not self.checkBounds():
			self.currentLocation["y"] += 1
			print("Can't move in that direction. Sorry.")

		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"])

	def incrementZPosUp(self,param):
		self.currentLocation["z"] += 1
		if not self.checkBounds():
			self.currentLocation["z"] -= 1
			print("Can't move in that direction. Sorry.")

		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"])

	def incrementZPosDown(self,param):
		self.currentLocation["z"] -= 1
		if not self.checkBounds():
			self.currentLocation["z"] += 1
			print("Can't move in that direction. Sorry.")

		self.insertAtPostition(x = self.currentLocation["x"],
			y = self.currentLocation["y"], z = self.currentLocation["z"])

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

	#This only insures cordinants exist within the grid, it does
	#not create a new space.
	def ensureGridPossition(self,x,y,z):
		if x not in self.grid:
			self.grid[x] = {}
		if y not in self.grid[x]:
			self.grid[x][y] = {}
		if z not in self.grid[x][y]:
			self.grid[x][y][z] = None

	def insertAtPostition(self, x, y,z, spaceObject=None):
		if x not in self.grid:
			self.grid[x] = {}
		if y not in self.grid[x]:
			self.grid[x][y] = {}
		if z not in self.grid[x][y]:
			self.createRoom(x,y,z, spaceObject)
		
		# print(self.grid)
	def createRoom(self, x,y,z, spaceObject =None, verbose=True):
		if spaceObject == None:
			spaceObject = Space("mountan")
		
		if verbose:
			print("You have wondered into a brand new space")

		self.grid[x][y][z] = spaceObject

	def getCurrentSpaceObject(self):
		x = self.currentLocation["x"]
		y = self.currentLocation["y"]
		z = self.currentLocation["z"]
		return self.grid[x][y][z]

	def describeLocation(self, param):

		print("At location of type "+ self.getCurrentSpaceObject().type +
				" at coordinants: " + str(self.currentLocation) )
		curSpace = self.getCurrentSpaceObject()
		print("This area has " + str(len(curSpace.items)) +" items and " +str(len(curSpace.mobs)) +
			" creatures")
	def describeItems(self, param):
		curSpace = self.getCurrentSpaceObject()
		print(str(len(curSpace.items)) + " item(s)")
		i = 1
		for item in curSpace.items:
			print("Item #" + str(i)+":")
			print("Item type: " + item.type)
			if item.description:
				print("Item description: ")

			i+=1

	def describeMobs(self, param):
		print("Not today. Im a STUB")

	#Accepts arguments as x:coord, y:coord, or z:coor
	def transport(self, param):
		for opt in param.args:
			opt = opt.split(":")
			self.currentLocation[opt[0]] = opt[1]

		if checkBounds():
			

class Param():
	def __init__(self, args=None):
		self.args = args

class Game():
	def __init__(self):

		startSpace = Space("room")
		self.grid = Grid(0,0,0)
		self.grid.addSpace(0,0,0, startSpace)
		self.config = Config(game=self, grid=self.grid)
		self.grid.loadMap(self.config.game1)
	def start(self):
		print("You find yourself in an empty room, what would you like to do? ")
		loop = True
		while loop:

			loop = self.parse(commandString = input(), commandDict = self.config.mainActionMap )



	def parse(self, commandString, commandDict):
		
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

			if isinstance(commandDict, str):
				print(commandDict)
			if isinstance(commandDict, types.MethodType):
				paramObj = Param(args=commandList[i:]) 
				if commandDict( param = paramObj ) == False:
					return False
				else:
					return True


			i += 1

		if "onFail" in commandDict:
			commandDict = commandDict["onFail"]
			if "message" in commandDict:
				print(commandDict["message"])
			if "function" in commandDict:
				commandDict = commandDict["function"]
				if commandDict:
					paramObj = Param(args = commandList)
					commandDict(param = paramObj)
		else:
			print("No")

		return True

	def exitGame(self, param):
		for option in param.args:
			if option == "f":
				return False
		if input("Are you sure? There is currently no save feature. ")[:1].lower() == "y":
	 		return False
			


if __name__ == '__main__':
	main()