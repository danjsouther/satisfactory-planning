from ..component import Component
from ..machine import Constructor
from .ingot import Steel

class SteelBeam(Component):
	production = Constructor(
		inputs = [
			Steel(3)
		],
		output = 1,
		rate = 10
	)
