class HP:
    def __init__(self, max):
        self.max = max
        self.get = max
        self.tmp = 0
        self.effects = []
        
class WP:
    def __init__(self, max):
        self.max = max
        self.stage = 0
        self.effects = []