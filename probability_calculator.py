import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            if ball in drawn_balls_dict:
                drawn_balls_dict[ball] += 1
            else:
                drawn_balls_dict[ball] = 1

        success = True
        for color, expected_quantity in expected_balls.items():
            if color not in drawn_balls_dict or drawn_balls_dict[color] < expected_quantity:
                success = False
                break
        if success:
            success_count += 1

    return success_count / num_experiments