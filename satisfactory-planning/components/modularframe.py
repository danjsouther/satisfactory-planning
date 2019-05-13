from ..component import Component
from ..machine import Assembler
from .reinforcedironplate import ReinforcedIronPlateAlt
from .ironrod import IronRod
from .steelpipe import SteelPipe

class ModularFrame(Component):
	production = Assembler(
		inputs = [
			ReinforcedIronPlateAlt(3),
			IronRod(6)
		],
		output = 1,
		rate = 4
	)

class ModularFrameAlt(Component):
	production = Assembler(
		inputs = [
			ReinforcedIronPlateAlt(6),
			SteelPipe(6)
		],
		output = 3,
		rate = 6
	)
