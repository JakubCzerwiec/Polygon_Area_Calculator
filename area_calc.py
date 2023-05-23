class Rectangle() :
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def set_width(self) :
        return self.width
    
    def set_height(self) :
        return self.height
    
    def get_area(self) :
        area = self.set_width() * self.set_height()
        return area

    def get_perimeter(self) :
        perimeter = (2 * self.set_width() + 2 * self.set_height())
        return perimeter
    
    def get_diagonal(self) :
        diagonal = ((self.set_width() ** 2 + self.set_height() ** 2) ** .5)
        return diagonal

    def get_picture(self) :
        picture = ''
        i = 0
        if self.set_height() > 50 or self.set_width() > 50 :
            print('Too big for picture.')
            quit()

        while i < self.set_height() :
            picture += '*' * self.set_width() + '\n'
            i += 1
        return picture

rec = Rectangle(2, 3)
print(rec.get_picture())