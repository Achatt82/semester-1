# Worksheet 1.5: Rectangle Class

from cmath import rect

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """

        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Both parameters must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Both parameters must be greater than 0")

        self.width = width
        self.height = height

    def is_square(self):
        """
        Checks if the rectangles width is equal to its height.
        If they are equal, the rectangle is square and returns True. Otherwise,
        it returns false.
        """

        return self.width == self.height

    def area(self):
        """
        Calculates and returns the area of the rectangle by multiplying its width
        by its height.
        """

        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle by adding
        its width and height togetyher and multiplying by 2.
        """

        return (self.width + self.height) * 2
