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

rec = Rectangle(8, 5)
print(rec.get_area())