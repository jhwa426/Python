class Point:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y
        
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


