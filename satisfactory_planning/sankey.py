
class Sankey(object):
    def __init__(self):
        self._labels = []
        self.source = []
        self.target = []
        self.values = []
        
    def addLabel(self, index, label):
        self._labels.append({'index': index, 'label': label})
        
    @property
    def labels(self):
        labelMax = max(map(lambda l: l['index'], self._labels))
        labels = ['']*(labelMax+1)
        for item in self._labels:
            # if item['label'] not in labels:
            labels[item['index']] = item['label']
        return labels
        
    def __add__(self, other):
        sankey = Sankey()
        sankey._labels = self._labels + other._labels
        sankey.source = self.source + other.source
        sankey.target = self.target + other.target
        sankey.values = self.values + other.values
        return sankey