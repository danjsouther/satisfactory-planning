from ..component import Component
from ..machine import Constructor
from .ingot import Caterium

class Quickwire(Component):
	production = Constructor(
		inputs = [
			Caterium(1)
		],
		output = 4,
		rate = 60
	)