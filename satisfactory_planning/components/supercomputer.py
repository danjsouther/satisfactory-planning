from ..component import Component
from ..machine import Manufacturer
from .computer import Computer
from .ailimiter import AILimiter
from .highspeedconnector import HighSpeedConnector
from .plastic import Plastic

class SuperComputer(Component):
	production = Manufacturer(
		inputs = [
			Computer(2),
			AILimiter(2),
			HighSpeedConnector(3),
			Plastic(21)
		],
		output = 1,
		rate = 1.875
	)