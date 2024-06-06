import math

class ShapeValueError(Exception):
    pass

def is_number(value):
    """Return true if value is a number"""
    return isinstance(value, int) or isinstance(value, float)
    

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        if is_number(new_x):
            self._x = new_x
        else:
            raise ShapeValueError('x must be a number')
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        if is_number(new_y):
            self._y = new_y
        else:
            raise ShapeValueError('y must be a number')
    
    def get_area(self):
        pass
    
    def get_perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        
    @property    
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if is_number(new_radius) and new_radius>0:
            self._radius = new_radius
        else:
            raise ShapeValueError("radius must be a positive")
        
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f"<Circle {self.x} {self.y} {self.radius}>"
    
c = Circle(1, 4, 100)
print(c)