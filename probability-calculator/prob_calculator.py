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
            return "This is, indeed, a hat."
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
      
      experiments = []
      # draw balls from hat for num_experiments 
      for _ in range(num_experiments):
            # deep copy hat to avoid removing balls from original and running out of balls for subsequent experiments
            hat_copy = copy.deepcopy(hat)
            drawn = hat_copy.draw(num_balls_drawn)
            experiments.append(drawn)
      
      # convert list of experiment results to list of experiment results as dictionaries with balls counted
      counted_results = []
      for result in experiments:
            counter = {}
            for ball in result:
                  if ball in counter:
                        counter[ball] += 1
                  else:
                        counter[ball] = 1
            counted_results.append(counter)
      
      successful_result = 0
      # compare expected_balls with each dictionary result
      for counted_result in counted_results:
            successful_balls = 0
            # check each expected ball in expected_balls
            for ball, count in expected_balls.items():
                  # check if counted_result is successful for each ball in expected_result
                  # i.e. the ball exists in the counted_result and the number of the ball is >= the expected number for that ball
                  if ball in counted_result and counted_result[ball] >= count:
                        successful_balls += 1
                  
            # if for each ball in expected_balls there is a successful ball, add 1 to successful_result     
            if successful_balls == len(expected_balls.keys()):
                  successful_result += 1
                  
      probability = successful_result / num_experiments        
      
      return probability
                        
      
hat = Hat(red=4, blue=4)     
print(experiment(hat, {"red": 3, "blue": 4}, 7, 5000))