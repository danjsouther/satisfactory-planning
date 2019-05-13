from ..component import Component
from ..machine import Assembler
from .wire import Wire
from .plastic import Plastic

class CircuitBoard(Component):
	production = Assembler(
		inputs = [Wire(12), Plastic(6)],
		output = 1,
		rate = 5
	)
