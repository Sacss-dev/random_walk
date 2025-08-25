from random import choice 


class RandomWalk: 
    """A class that generates random walks"""

    def __init__(self, num_points = 10000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # Each walk starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self) : 
        """Calculate all the points in the walk"""


        # Keep taking steps until the number of points desired is reached 
        while len(self.x_values) < self.num_points : 

            # Decide which direction to go and how far to go in that direction 
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0 : 
                continue 

            # Calculate the new position 
            x_new = self.x_values[-1] + x_step 
            y_new = self.y_values[-1] + y_step 

            self.x_values.append(x_new)
            self.y_values.append(y_new)


        