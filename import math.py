import math
import random

def multiply_pi():
    return random.randint(1,10) * math.pi

for i in range(5):
    print(multiply_pi())