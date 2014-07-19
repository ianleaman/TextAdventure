#Game Configuration Dictionaries.
#This is where you tell the parser

#have an active item variable.
'''
Global configuration can be overiden locally
'''
class Config:
	def __init__(self, game, grid):
		self.game = game
		self.grid = grid

		self.globalActionMap = {
			"sudo":{
				"ls":"",
				"rm":"",
				"system":"",
			},
			"exit":"",
		}

		moveConfig = {
				"north":self.grid.incrementXPosUp,  #x-up
				"south":self.grid.incrementXPosDown, #x-down
				"east":self.grid.incrementYPosUp,     #y-up
				"west":self.grid.incrementYPosDown,  #y-down
				"up":self.grid.incrementZPosUp,      #z-up
				"down":self.grid.incrementZPosDown,   #z-down
				}

		self.mainActionMap ={
			"move":moveConfig,
			"go":moveConfig,
			"travel":moveConfig,
			"describe":{
				"location":self.grid.describeLocation,
			}
		}

		self.fightCommandDict = {
			

		}

"""
Endings:
Congradulations youve won the game.---
But you lose your self respect.
But at what cost?
Who knew winning could be that easy.
But whats the point.
Why did so much time playing this game.
But are you really happy.

"""
