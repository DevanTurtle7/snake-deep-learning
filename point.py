class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __eq__(self, other):
    if not isinstance(other, Point):
      return False
    else:
      return other.x == self.x and other.y == self.y
    
  def __repr__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
