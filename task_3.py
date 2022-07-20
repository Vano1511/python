class Cell:

    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size

    def __mul__(self, other):
        return self.size * other.size

    def __truediv__(self, other):
        return round(self.size / other.size)

    def make_order(self, step):
        if self.size > step:
            full = self.size // step
            part = (self.size % step) * '*'
            self.step = step * '*'
            list = [self.step for i in range(full)]
            list.append(part)
        else:
            list = [self.size * '*']
        str = '\п'.join(list)
        return str




cell1 = Cell(15)
cell2 = Cell(6)
cell3 = Cell(cell2 + cell1)
print(cell3.make_order(6))