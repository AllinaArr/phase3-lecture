# classes are the blueprints
class Rectangle:
    # constructor -- function that build the object
    def __init__(self, width_param, heigth_param):
       self.width=width_param
       self.height=heigth_param
       
    def get_area(self):
        return self.width * self.height
    
    def get_circumfrence(self):
        return (2 * self.width) + (2 * self.height)

# build a reactangle object
r1 = Rectangle(2,3)
r1.width = 99
print(type(r1))