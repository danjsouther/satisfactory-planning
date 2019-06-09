from ..component import Component
from ..machine import Assembler, Constructor
from .wire import Wire
from .rubber import Rubber

class Cable(Component):
	production = Constructor(
		inputs = [
			Wire(2)
		],
		output = 1,
		rate = 37.5
	)
class CableAlt(Component):
	production = Assembler(
		inputs = [
			Wire(3),
			Rubber(2)
		],
		output = 5,
		rate = 37.5
	)