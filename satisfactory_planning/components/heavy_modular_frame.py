from ..component import Component
from ..machine import Manufacturer
from .modular_frame import ModularFrame, ModularFrameAlt
from .concrete import Concrete
from .steel_pipe import SteelPipe
from .encased_industrial_beam import EncasedIndustrialBeam, EncasedIndustrialBeamAlt
from .screw import Screw, ScrewAlt

class HeavyModularFrame(Component):
	production = Manufacturer(
		inputs = [
			ModularFrame(5),
			SteelPipe(15),
			EncasedIndustrialBeam(5),
			Screw(90)
		],
		output = 1,
		rate = 2
	)

class HeavyModularFrameAlt(Component):
	production = Manufacturer(
		inputs = [
			ModularFrame(8),
			SteelPipe(36),
			EncasedIndustrialBeam(10),
			Concrete(25)
		],
		output = 3,
		rate = 2.812
	)
