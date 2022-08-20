"""CS 108 - Final Project

Pictionary Game Test

@author: Ben Elpidius (bee6)
@date: fall, 2021
@Project Used: Simple Draw
"""

import math
from pictionary import File, Leader, Leaderboard, Line, Squiggle, Rectangle, Ellipse

file = File()

# Asserts for reading from easy level file
assert file.easy[0] == 'Book'
assert file.easy[2] == 'Laptop'

# Asserts for reading from medium level file
assert file.medium[0] == 'Bag'
assert file.medium[2] == 'Telephone'

# Asserts for reading from hard level file
assert file.hard[0] == 'Computer Science'
assert file.hard[2] == 'Summer'


check_leaderboard = Leaderboard()

# Asserts for reading from leaderboard file 
assert check_leaderboard.leaderboard[0].user == 'ben'
assert check_leaderboard.leaderboard[1].corrects == 2


# Asserts for the rectangle class. Taken from figure_test.
rectangle = Rectangle(start=(0, 0), dimensions=(10, 10), color='green')
assert abs(rectangle.get_area() - 100.0) < 1e-2


# Asserts for the ellipse class. Taken from figure_test.
ellipse = Ellipse(start=(0, 0), dimensions=(10, 10), color='red', filled=True)
assert abs(ellipse.get_area() - math.pi * 100) < 1e-2


# Asserts for the line class. Taken from figure_test.
line = Line(start=(0, 0), end=(0, 10), color='blue')
assert line.get_length() == 10.0


# Asserts for the squiggle class. Taken from figure_test.
squiggle = Squiggle()
for x in range(1, 11):
    squiggle.add_point((0, x))
assert squiggle.get_length() == 10.0


print('all test passed')