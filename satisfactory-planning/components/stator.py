from ..component import Component
from ..machine import Assembler
from .steelpipe import SteelPipe
from .wire import Wire

class Stator(Component):
	production = Assembler(
		inputs = [
			SteelPipe(3),
			Wire(10)
		],
		output = 1,
		rate = 6
	)