#!/usr/bin/python3
"""

Module comprises class that defines Rectangle


"""


class Rectangle:
    """ Class defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method initializes instance

        Args:
            width: rectangle width
            height: rectangle height


        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ method returns value of width

        Returns:
            rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method defines width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method returns value of height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method defines height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method calculates Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ Method calculates Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method  the Rectangle #

        Returns:
            str of the rectangle


        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method returns string represantion of instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method prints message when instance is deleted


        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
