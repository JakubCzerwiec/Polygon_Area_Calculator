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
        if self.height > 50 or self.width > 50 :
            print('Too big for picture.')
            quit()

        while i < self.height :
            picture += '*' * self.width + '\n'
            i += 1
        return picture

    def get_amount_inside(self, shape_width, shape_height) :
        if self.width < shape_width or self.height < shape_height :
            return 0
        else :
            number_of_items = int(math.floor(self.width / shape_width)) * int(math.floor(self.height / shape_height))
            return number_of_items

    def __str__(self) :
        rect_string = f'Rectangle(width={self.width}, height={self.height})'
        return rect_string


rec = Rectangle(2, 3)
rec.set_height(7)
rec.set_width(10)
print(rec.get_area())

print(rec.get_picture())
print(rec.get_amount_inside(3,2))
print(rec)