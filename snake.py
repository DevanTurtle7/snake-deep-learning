from point import Point
import random

UP_DIR = 'UP'
RIGHT_DIR = 'RIGHT'
LEFT_DIR = 'LEFT'

class SnakeGame:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__snake = [Point(width // 2, height // 2)];
        self.__food = generateFood()
    
    def move(self, dir):
        pass
    
    def generateFood(self):
        found = False
        
        while not found:
            x = random.randrange(self.__width)
            y = random.randrange(self.__height)
