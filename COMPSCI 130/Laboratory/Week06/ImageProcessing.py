class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0 for col in range(width)] for row in range(height)]

