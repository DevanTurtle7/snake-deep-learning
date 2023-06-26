from point import Point
import random
import numpy as np

UP_DIR = 'UP'
RIGHT_DIR = 'RIGHT'
LEFT_DIR = 'LEFT'
DOWN_DIR = 'DOWN'
DEFAULT_DIR = 'DEFAULT'

class SnakeGame:
  def __init__(self, width, height):
    self.__width = width
    self.__height = height
    self.__snake = [Point(width // 2, height // 2)];
    self.__food = None
    self.__direction = Point(0, 1) # Point used as vector
    self.generate_food()

  def move(self, dir):
    newHead = None
    currentX = self.__snake[0].x
    currentY = self.__snake[0].y
    opposite_dir = Point(self.__direction.x * -1, self.__direction.y * -1)
    new_dir = None

    if (dir == UP_DIR):
      new_dir = Point(0, 1)
    elif (dir == DOWN_DIR):
      new_dir = Point(0, -1)
    elif (dir == LEFT_DIR):
      new_dir = Point(-1, 0)
    elif (dir == RIGHT_DIR):
      new_dir = Point(1, 0)
    else:
      new_dir = self.__direction
    
    if opposite_dir != new_dir:
      self.__direction = new_dir

    newHead = Point(currentX + self.__direction.x, currentY + self.__direction.y)
    self.__snake.pop()
    self.__snake.insert(0, newHead)

    if newHead.x < 0 or newHead.y < 0 or newHead.x >= self.__width or newHead.y >= self.__width:
      print('Game over: out of bounds')
      return False
    
    for i in range(1, len(self.__snake)):
      if self.__snake[i] == newHead:
        print('Game over: Ran into your tail')
        return False
    
    if (newHead.x == self.__food.x and newHead.y == self.__food.y):
      self.eat()
    
    return True

    
  def generate_food(self):
    found = False
        
    while not found:
      overlap = False
      x = random.randrange(self.__width)
      y = random.randrange(self.__height)
      current = Point(x, y)
            
      for point in self.__snake:
        if point == current:
          overlap = True
          break
          
      if not overlap:
        found = True
        self.__food = current
  
  def print_display(self):
    print('\n')
    grid = []

    for y in range(0, self.__height):
      row = ''
      for x in range(0, self.__width):
        row += '.'
      
      grid.append(row)
    
    for point in self.__snake:
      chars = list(grid[(self.__height - 1) - point.y])
      chars[point.x] = '#'
      grid[(self.__height - 1) - point.y] = ''.join(chars)

    chars = list(grid[(self.__height - 1)- self.__food.y ])
    chars[self.__food.x] = 'X'
    grid[(self.__height - 1) - self.__food.y] = ''.join(chars)
    
    for row in grid:
      print(row)
  
  def eat(self):
    last = self.__snake[-1]
    self.__snake.append(Point(last.x, last.y))
    self.generate_food()

  def get_score(self):
    return len(self.__snake) - 1
  

def main():
  continue_game = True
  game = SnakeGame(10, 10)
  game.eat()
  game.eat()
  game.move(UP_DIR)
  game.move(UP_DIR)

  while continue_game:
    game.print_display()
    key = input('Use WASD to control >> ').upper()
    if key == 'W':
      continue_game = game.move(UP_DIR)
    elif key == 'S':
      continue_game = game.move(DOWN_DIR)
    elif key == 'A':
      continue_game = game.move(LEFT_DIR)
    elif key == 'D':
      continue_game = game.move(RIGHT_DIR)
    else:
      continue_game = game.move(DEFAULT_DIR)

if __name__ == '__main__':
  main()