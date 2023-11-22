import copy
import random

class Hat:
      def __init__(self, **kwargs):
            self.contents = []
            for key, value in kwargs.items():
                  for _ in range(value):
                        self.contents.append(key)
                        
      def draw(self, x):
            # check whether x exceeds the number of balls in self.contents
            if x > len(self.contents):
                  return self.contents
            else:
                  drawn = []
                  # draw X number of balls
                  for _ in range(x):
                        # generate random index to draw from based on length of self.contents
                        random_number = random.randint(0, len(self.contents) - 1)
                        
                        # identify ball based on random index
                        ball_drawn = self.contents[random_number]
                        
                        # remove ball from self.contents
                        self.contents.pop(random_number)
                        
                        # append ball to drawn list
                        drawn.append(ball_drawn)
            
                  return drawn      
                  
      def __str__(self):
            print(self.contents)
      
      
hat = Hat(red=6, blue=4, green=2)

print(hat.draw(2))

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
      
      # draw balls from hat
      hat.draw(num_balls_drawn)
      