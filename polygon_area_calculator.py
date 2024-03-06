class Rectangle:
    def __init__(self, width, height):
        # Initialize width and height attributes
        self.width = width
        self.height = height
    
    def __str__(self):
        # String representation of Rectangle
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        # Set width
        self.width = width

    def set_height(self, height):
        # Set height
        self.height = height

    def get_area(self):
        # Calculate area
        return self.width * self.height

    def get_perimeter(self):
        # Calculate perimeter
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Calculate diagonal
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        # Draw rectangle as picture
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for _ in range(self.height):
                picture += "*" * self.width + "\n"
            
            return picture

    def get_amount_inside(self, shape):
        # Calculate how many shapes can fit inside the rectangle
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height

        return horizontal_fit * vertical_fit


class Square(Rectangle):
    def __init__(self, side):
        # Initialize square with side length
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        # Set side length
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, width):
        # Set width (overriding Rectangle's set_width)
        self.set_side(width)
        self.side = width

    def set_height(self, height):
        # Set height (overriding Rectangle's set_height)
        self.set_side(height)
        self.side = height

    def __str__(self):
        # String representation of Square
        return f"Square(side={self.side})"
