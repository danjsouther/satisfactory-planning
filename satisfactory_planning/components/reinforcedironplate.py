from ..component import Component
from ..machine import Assembler
from .ironplate import IronPlate
from .wire import Wire

class ReinforcedIronPlateAlt(Component):
	production = Assembler(
		inputs = [
			IronPlate(6),
			Wire(30)
		],
		output = 3,
		rate = 7.5
	)