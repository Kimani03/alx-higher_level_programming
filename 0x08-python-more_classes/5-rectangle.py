#!/usr/bin/python3
""" Rectangle Module """

class Rectangle:
    """ Rectangle Class"""
    def __init__(self, width=0, height=0:)
        """ Initialize Rectangle """
        self.height = height
        self.widht = width
    
    @property
    def width(self):
        """ getter function for the private instance attribute widht"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """ setter function for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter function for the private instance attribute height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """ setter function for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height
    
    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect
    
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height) 
    
    def __del__(self):
        """Print text on deletionn of an instance of the rectangle class"""
        print("Bye rectangle...")
