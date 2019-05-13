from ..component import Component
from ..machine import Constructor
from .ingot import Steel

class SteelPipe(Component):
	production = Constructor(
		inputs = [
			Steel(1)
		],
		output = 1,
		rate = 15
	)
