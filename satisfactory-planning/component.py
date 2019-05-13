
class Component(object):

	def __init__(self, amount=1):
		self.amount = amount
		
	@property
	def name(self):
		return type(self).__name__
	
	def produce(self, rate):
		sankey = self._produce(rate)
		sankey.target.append(self.production.id+1)
		sankey.addLabel(self.production.id+1, self.name)
		return sankey
	
	def _produce(self, batchRate):
		unitRate = batchRate*self.amount
		sankey = self.production._produce(unitRate)
		sankey.addLabel(self.production.id, "{}-{}".format(self.production.name,self.name))
		return sankey
