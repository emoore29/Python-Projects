class Rectangle:
      def __init__(self, width, height):
            self.width = width
            self.height = height
            
      def set_width(self, width):
            self.width = width
            
      def set_height(self, height):
            self.height = height
            
      def get_area(self):
            return self.width * self.height
            
      def get_perimeter(self):
            return 2 * self.width + 2 * self.height

      def get_diagonal(self):
            return (self.width ** 2 + self.height ** 2) ** 0.5

      def get_picture(self):
            line = "*" * self.width + "\n"
            if self.width > 50 or self.height > 50:
                  return "Too big for picture."
            else:
                  return line * self.height
                  
      def get_amount_inside(self, shape):
            # See how many times width fits
            if shape.width <= self.width and shape.height <= self.height:
                  return (self.width // shape.width) * (self.height // shape.height)
            else: 
                  return 0
      
      def __str__(self):
            return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
      def __init__(self, side):
            self.width = side
            self.height = side
            
      def set_side(self, side):
            self.width = side
            self.height = side
            
      def set_width(self, width):
            self.width = width
            self.height = width
            
      def set_height(self, height):
            self.height = height
            self.width = height
            
      def __str__(self):
            return f"Square(side={self.width})"
      

