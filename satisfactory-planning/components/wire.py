from ..component import Component
from ..machine import Constructor
from .ingot import Copper

class Wire(Component):
	production = Constructor(
		inputs = [Copper(1)],
		output = 3,
		rate = 45
	)
