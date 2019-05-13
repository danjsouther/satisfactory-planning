from ..component import Component
from ..machine import Smelter
from ..machine import Foundry

class Iron(Component):
	production = Smelter(output=1,rate=30)
	
class Copper(Component):
	production = Smelter(output=1,rate=30)

class Caterium(Component):
	production = Smelter(output=1, rate=30)

class Steel(Component):
	production = Foundry(
		output = 2,
		rate = 30
	)
