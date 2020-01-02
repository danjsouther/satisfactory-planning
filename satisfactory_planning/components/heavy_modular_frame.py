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
			ModularFrameAlt(5),
			SteelPipe(15),
			EncasedIndustrialBeamAlt(5),
			ScrewAlt(90)
		],
		output = 1,
		rate = 2
	)

class HeavyModularFrameAlt(Component):
	production = Manufacturer(
		inputs = [
			ModularFrameAlt(8),
			SteelPipe(36),
			EncasedIndustrialBeamAlt(10),
			Concrete(25)
		],
		output = 3,
		rate = 2.812
	)
