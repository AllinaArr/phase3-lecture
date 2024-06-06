class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'<Pet {self.name} {self.age}>'

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def __repr__(self):
        return f'<Dog {self.name} {self.age}>'
        
class Cat(Pet):
    def __repr__(self):
        return f'<Cat {self.name} {self.age}>'
        
        