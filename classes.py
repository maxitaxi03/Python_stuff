#classes

class Point():
    def __init__ (self, x, y): #this is a magic method that is automatically called every time we try to make a new Point. All methods that operate on objexts themselves will take the first agrument "self"
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)