from ..component import Component
from ..machine import Constructor
from .ironrod import IronRod
from .ingot import Iron

class Screw(Component):
	production = Constructor(
		inputs = [
			IronRod(1)
		],
		output = 6,
		rate = 90
	)

class ScrewAlt(Component):
	production = Constructor(
		inputs = [
			Iron(2)
		],
		output = 12,
		rate = 90
	)
