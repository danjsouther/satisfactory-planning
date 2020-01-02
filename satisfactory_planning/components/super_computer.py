from ..component import Component
from ..machine import Manufacturer
from .computer import Computer
from .ai_limiter import AILimiter
from .high_speed_connector import HighSpeedConnector
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