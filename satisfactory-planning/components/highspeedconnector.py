from ..component import Component
from ..machine import Assembler
from .quickwire import Quickwire
from .cable import CableAlt
from .plastic import Plastic

class HighSpeedConnector(Component):
	production = Assembler(
		inputs = [
			Quickwire(40),
			CableAlt(10),
			Plastic(6)
		],
		output = 1,
		rate = 2.5
	)
