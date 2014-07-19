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



		describeConfig = {
				"location":self.grid.describeLocation,  #Either describes the location or changes location description
				"items":self.grid.describeItems,
				"mobs":self.grid.describeMobs,
				"onFail":{    #In this case onFail is acting as the default function to run
					"function":self.grid.describeLocation,
				},
			}

		moveConfig = {
				"north":self.grid.incrementXPosUp,  #x-up
				"south":self.grid.incrementXPosDown, #x-down
				"east":self.grid.incrementYPosUp,     #y-up
				"west":self.grid.incrementYPosDown,  #y-down
				"up":self.grid.incrementZPosUp,      #z-up
				"down":self.grid.incrementZPosDown,   #z-down
				"help":"Wll this is an unhelful help message",
				"onFail":{
					"message":"You cant move in that direction",
				},
			}

		self.globalActionMap = {
			"sudo":{
				"ls":"",
				"rm":"",
				"system":"",
				"teleport":self.grid.transport #More descrption in function
			},
			"ls":describeConfig,
			"exit":self.game.exitGame,
		}

	

		self.mainActionMap ={
			"move":moveConfig,
			"go":moveConfig,
			"travel":moveConfig,
			"describe":describeConfig,
			"onFail":{
				"message":"No I Will Not", 
				"function":None,
			}
		}

		self.fightCommandDict = {
			

		}

		self.game1 = {
			"spaces":[
				{
					"x":0,
					"y":0,
					"z":0,
					"type":"room",
					"description":"Your base of operations",
					"items":[
					{
						"type":"sword",
						"attack":9,
						"defence":0
					}
					],
					"mobs":[],
				},
				{
					"x":1,
					"y":2,
					"z":0,
					"type":"room",
					"description":"An empty room",
					"items":[
					{
						"type":"sword",
						"attack":4,
						"defence":0
					}
					],
					"mobs":[
					{
						"type":"mouse",
						"attack":0,
						"health":0
					},
					{
						"type":"mouse",
						"attack":0,
						"health":0
					},
					{
						"type":"mouse",
						"attack":0,
						"health":0
					},
					],
				},
				{
					"x":4,
					"y":2,
					"z":0,
					"type":"room",
					"description":"The boss",
					"items":[
					{
						"type":"rock",
						"attack":1,
						"defence":2,
					}
					],
					"mobs":[
					{
						"type":"Minor Boss",
						"attack":10,
						"health":10,
						"description":("All those tremble when looking upon this "
							"bosses midlevel power")
					},
					],
				},
				],
			"mobTypes":[],
			"itemTypes":[],
		}


"""
Plan for different endings:
Congradulations youve won the game.---
But in the process you lost your self respect.
But at what cost?
Who knew winning could be that easy.
But whats the point.
Why did you spend so much time playing this game.
But are you really happy about it.

"""
