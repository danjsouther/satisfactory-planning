from ..component import Component
from ..machine import Manufacturer
from .circuitboard import CircuitBoard
from .cable import Cable, CableAlt
from .plastic import Plastic
from .screw import Screw, ScrewAlt

class Computer(Component):
	production = Manufacturer(
		inputs = [
			CircuitBoard(5),
			Cable(12),
			Plastic(18),
			Screw(60)
		],
		output = 1,
		rate = 1.875
	)

class ComputerAlt(Component):
	production = Manufacturer(
		inputs = [
			CircuitBoard(5),
			CableAlt(12),
			Plastic(18),
			ScrewAlt(60)
		],
		output = 1,
		rate = 1.875
	)
