class Bird:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 0
        self.tickCount = 0
        self.flapHeight = 0

    def flap(self):
        self.velocity = -6.5
        self.tickCount = 0
        self.flapHeight = self.y

    def move(self):
        self.tickCount += 1
        d = (self.velocity * self.tickCount) + (0.9 * (self.tickCount ** 2))
    
        if d >= 16:
            d = 16
        if d < 0:
            d -= 1.5

        self.y += d

    def death(self):
        pass


