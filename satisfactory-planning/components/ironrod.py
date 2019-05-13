from ..component import Component
from ..machine import Constructor
from .ingot import Iron

class IronRod(Component):
	production = Constructor(
		inputs = [Iron(1)],
		output = 1,
		rate = 15
	)
