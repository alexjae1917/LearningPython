
class Rectangle():

    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width


    def square(self):
        return self.width * self.lenth

    @staticmethod
    def sizes(lenth, sq):
        for i in range(lenth, sq):
            if sq % i == 0:
                return i
        return 1


    def new_rect(self,a,sq):
        new_lenth = self.sizes(a, sq)
        new_width = sq / new_lenth
        new = Rectangle(new_lenth, new_width)
        return new


    def __add__(self,other):
        new_square = self.square()+other.square()
        new_rect = self.new_rect(self.lenth + self.width, new_square)
        return new_rect

    def __mul__(self, number: int):
        new_square = self.square()*number
        new_rect = self.new_rect(self.lenth + number, new_square)
        return new_rect


    def __gt__(self,other):
        return self.square() > other.square()


    def __lt__(self,other):
        return self.square() < other.square()


    def __eq__(self,other):
        return self.square() == other.square()


    def __ne__(self,other):
        return self.square() != other.square()


    def __str__(self):
        return f'rectangle with:\nlenth {self.lenth}\nwidth {self.width}\nSquare {self.square()}\n'
