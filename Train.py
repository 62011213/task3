from Transportation import Transportation
class train(Transportation):
    def __init__(self, s, e, d, stop):
        super().__init__(s, e, d)
        self.stop = stop
    def find_cost(self):
        return self.stop * 5