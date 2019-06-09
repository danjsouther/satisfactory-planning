from ..component import Component
from ..machine import OilRefinery

class Rubber(Component):
	production = OilRefinery(output=4, rate=30)
