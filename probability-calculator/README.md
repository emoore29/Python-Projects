# Probability Calculator

This is a FCC project. The full instructions can be found [here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator), but I've written my own summary below.

The **Hat** class takes a variable number of arguments that specify the number of balls of each colour that are in a hat. These are stored in a contents instance variable, which is a list of strings. For example, two red balls and one blue ball will result in a contents instance variable of ["red", "red", "blue"].

The Hat class contains a **draw** method that accepts a number that indicates how many balls to draw from the hat. The balls do not go back into the hat during the draw. If the number drawn is greater than the number inside the hat, return all the balls.

There is also an **experiment** function that accepts the following:

- **hat** an object containing the balls
- **expected balls** an object indicating the group of balls that we are attempting to draw from the hat, e.g., {"blue": 2, "red": 1}
- **num_balls_drawn** the number of balls to draw from the hat in each experiment
- **num_experiments** the number of experiments to perform. _The more experiments performed, the more accurate the approximate probability will be_

It should return a probability.

## Example

Calculate the probability of drawing two red balls and one green ball when five balls are drawn from a hat containing six black, four red, adn three green balls:

![hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)](image.png)
