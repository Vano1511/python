class Clothes:

     def __init__(self, size):
         self.size = size

class Coat(Clothes):
    @property
    def consuption(self):
        return self.size/6.5 + 0.5
class Suit(Clothes):

    @property
    def consuption(self):
        return self.size*2 + 0.3

size = int(input('введите размер пальто '))
high = float(input('введите рост костюма в метрах '))
coat1 = Coat(size)
suit1 = Suit(high)
print(f'общий расход равен {round(coat1.consuption+suit1.consuption, 3)} м ткани')
