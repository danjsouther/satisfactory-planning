from ..component import Component
from ..machine import Assembler
from .reinforced_iron_plate import ReinforcedIronPlateAlt, ReinforcedIronPlate
from .iron_rod import IronRod
from .steel_pipe import SteelPipe

class ModularFrame(Component):
	production = Assembler(
		inputs = [
			ReinforcedIronPlate(3),
			IronRod(6)
		],
		output = 1,
		rate = 4
	)

class ModularFrameAlt(Component):
	production = Assembler(
		inputs = [
			ReinforcedIronPlate(6),
			SteelPipe(6)
		],
		output = 3,
		rate = 6
	)
