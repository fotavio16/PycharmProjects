import math

class Vector2(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
        #return "(%s, %s)" % (format_number(x), format_number(y))

    def __getitem__(self, index):
        """Gets a component as though the vector were a list."""
        try:
            return self._v[index]
        except IndexError:
            raise IndexError("There are 2 values in this object, index should be 0 or 1")

    @classmethod
    def from_points(cls, p1, p2):
        x, y = p1
        xx, yy = p2
        return cls(float(xx-x), float(yy-y))

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):
        magnitude = self.get_magnitude()
        return (self.x / magnitude, self.y / magnitude)

    # rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2( -self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
