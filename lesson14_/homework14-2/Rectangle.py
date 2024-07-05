
class Rectangle():

    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width


    def square(self):
        return self.width * self.lenth

    @staticmethod
    def sizes(a,sq):
        for i in range(a,sq):
            if sq % i ==0:
                return i
        return 1

    @staticmethod
    def new_rect(a,sq):
        new_lenth = self.sizes(self.lenth + self.width, new_square)
        new_width = new_square / new_lenth
        new = Rectangle(new_lenth, new_width)


    def __add__(self,other):
        new_square = self.square()+other.square()
        new_lenth = self.sizes(self.lenth + self.width, new_square)
        new_width = new_square/new_lenth
        new = Rectangle(new_lenth,new_width)
        return new

    def __mul__(self, number: int):
        new_square = self.square()*number
        new_lenth = self.sizes(self.lenth + self.width, new_square)
        new_width = new_square / new_lenth
        new = Rectangle(new_lenth, new_width)


    def __gt__(self,other):
        if self.square() > other.Rectangle():
            return True
        return False

    def __lt__(self,other):
        if self.square() < other.Rectangle():
            return True
        return False

    def __eq__(self,other):
        if self.square() == other.Rectangle():
            return True
        return False

    def __ne__(self,other):
        if self.square() != other.Rectangle():
            return True
        return False

    def __str__(self):
        return f'rectangle with:\nlenth {self.lenth}\nwidth {self.width}\nSquare {self.square()}\n'
