from ..component import Component
from ..machine import Assembler
from .rotor import Rotor
from .stator import Stator

class Motor(Component):
	production = Assembler(
		inputs = [
			Stator(2),
			Rotor(2)
		],
		output = 1,
		rate = 5
	)