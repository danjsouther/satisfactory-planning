from ..component import Component
from ..machine import Assembler
from .iron_plate import IronPlate
from .wire import Wire
from .screw import Screw

class ReinforcedIronPlate(Component):
	production = Assembler(
		inputs = [
			IronPlate(4),
			Screw(24)
		],
		output = 1,
		rate = 5
	)

class ReinforcedIronPlateAlt(Component):
	production = Assembler(
		inputs = [
			IronPlate(6),
			Wire(30)
		],
		output = 3,
		rate = 7.5
	)