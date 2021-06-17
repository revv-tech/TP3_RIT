class AssumptionClass:
    className = ""
    n = 0
    total = 0

    def __init__(self, className):
        self.className = className
        self.n = 0
        self.total = 0

    def average(self):
        if self.n != 0:
            self.total /= self.n
        else:
            self.total = 0
        return

    def addTotal(self, pWeight):
        self.n += 1
        self.total += pWeight
        return
