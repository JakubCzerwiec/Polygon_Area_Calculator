import math
class Rectangle() :
    def __init__(self, width, height) :
        self.width = width
        self.height = height
    
    def set_width(self, new_width) :
        self.width = new_width
    
    def set_height(self, new_height) :
        self.height = new_height

    def get_area(self) :
        area = self.width * self.height
        return area

    def get_perimeter(self) :
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter
    
    def get_diagonal(self) :
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self) :
        picture = ''
        i = 0
        if self.height >= 50 or self.width >= 50 :
            return 'Too big for picture.'
            quit()

        while i < self.height :
            picture += '*' * self.width + '\n'
            i += 1
        return picture

    def get_amount_inside(self, ob) :
        return self.get_area() // ob.get_area()


    def __str__(self) :
        rect_string = f'Rectangle(width={self.width}, height={self.height})'
        return rect_string

class Square(Rectangle) :
    def __init__(self, side) :

        self.width = side
        self.height = side

    def set_side(self, new_side) :
        self.width = new_side
        self.height = new_side


    def set_width(self, new_width) :
        self.width = new_width
        self.height = new_width
    
    def set_height(self, new_height) :
        self.height = new_height
        self.width = new_height

    def __str__(self) :
        scr_string = f'Square(side={self.width})'
        return scr_string
    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))