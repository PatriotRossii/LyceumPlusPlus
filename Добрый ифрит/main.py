class GoodIfrit:
    def __adjust_goodness(self):
        if self.goodness < 0:
            self.goodness = 0

    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = goodness

        self.__adjust_goodness()

    def change_goodness(self, value):
        self.goodness += value
        self.__adjust_goodness()

    def __add__(self, value):
        return GoodIfrit(self.height + value, self.name, self.goodness)

    def __call__(self, value):
        return value * self.goodness // self.height

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, \
goodness {self.goodness}"

    def __lt__(self, other):
        return (self.goodness, self.height, self.name) <\
                (other.goodness, other.height, other.name)

    def __le__(self, other):
        return (self.goodness, self.height, self.name) <=\
                (other.goodness, other.height, other.name)

    def __gt__(self, other):
        return (self.goodness, self.height, self.name) >\
                (other.goodness, other.height, other.name)

    def __ge__(self, other):
        return (self.goodness, self.height, self.name) >=\
                (other.goodness, other.height, other.name)

    def __eq__(self, other):
        return (self.goodness, self.height, self.name) ==\
                (other.goodness, other.height, other.name)

    def __ne__(self, other):
        return (self.goodness, self.height, self.name) !=\
                (other.goodness, other.height, other.name)
