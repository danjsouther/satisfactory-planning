from .sankey import Sankey

class Machine(object):
    _id = -1
    
    def __init__(self, output, rate, inputs=[]):
        self.id = Machine._getId()
        self.output = output
        self.rate = rate
        self.inputs = inputs
       
    @classmethod
    def _getId(cls):
        cls._id += 1
        return cls._id
    
    @property
    def name(self):
        return type(self).__name__

    def _produce(self, unitRate):
        clockSpeed = unitRate / self.rate
        batchRate = unitRate/self.output
        sankey = Sankey()
        for item in self.inputs:
            itemSankey = item._produce(batchRate)
            itemSankey.target.append(self.id)
            sankey += itemSankey
        sankey.source.append(self.id)
        sankey.value.append(clockSpeed)
        return sankey
    
class Smelter(Machine):
    pass

class Constructor(Machine):
    pass

class Assembler(Machine):
    pass

class Foundry(Machine):
    pass

class OilRefinery(Machine):
    pass

class Manufacturer(Machine):
    pass
