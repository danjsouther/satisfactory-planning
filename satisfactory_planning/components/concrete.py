from ..component import Component
from ..machine import Constructor

class Concrete(Component):
	production = Constructor(output=1, rate=15)
