import copy
import random

class Hat:
      def __init__(self, **kwargs):
            self.contents = []
            for key, value in kwargs:
                  self.contents.append(key * value)
                  
      def __str__(self):
            print(self.contents)
      
      
hat = Hat(red=2, blue=4)
print(hat)
# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
