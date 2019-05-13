from ..component import Component
from ..machine import Assembler
from .circuitboard import CircuitBoard
from .quickwire import Quickwire
	
class AILimiter(Component):
	production = Assembler(
		inputs = [
			CircuitBoard(1),
			Quickwire(18)
		],
		output = 1,
		rate = 5
	)
