from ..component import Component
from ..machine import Assembler
from .steel_beam import SteelBeam
from .steel_pipe import SteelPipe
from .concrete import Concrete


class EncasedIndustrialBeam(Component):
	production = Assembler(
		inputs = [
			SteelBeam(4),
			Concrete(5)
		],
		output = 1,
		rate = 4
	)
	
class EncasedIndustrialBeamAlt(Component):
	production = Assembler(
		inputs = [
			SteelPipe(18),
			Concrete(10)
		],
		output = 3,
		rate = 6
	)
