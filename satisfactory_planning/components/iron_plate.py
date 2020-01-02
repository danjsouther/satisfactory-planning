from ..component import Component
from ..machine import Constructor
from .ingot import Iron

class IronPlate(Component):
	production = Constructor(
		inputs = [Iron(2)],
		output = 1,
		rate = 15
	)
