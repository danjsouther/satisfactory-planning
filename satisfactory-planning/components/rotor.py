from ..component import Component
from ..machine import Assembler
from .ironrod import IronRod
from .screw import Screw, ScrewAlt

class Rotor(Component):
	production = Assembler(
		inputs = [
			IronRod(3),
			Screw(22)
		],
		output = 1,
		rate = 6
	)
