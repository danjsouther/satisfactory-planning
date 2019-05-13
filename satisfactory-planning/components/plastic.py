from ..component import Component
from ..machine import OilRefinery

class Plastic(Component):
	production = OilRefinery(output=3, rate=22.5)
