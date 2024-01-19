from typing import Any, List, Optional

class Point():
  """Represents a point on a Cartesian coordinate plane."""
  def __init__(self, x: int, y: int) -> None:
    """Creates a point with coordinates x and y."""
    self.x = x
    self.y = y
  
  def __eq__(self, other: object) -> bool:
    """Returns whether the two points are the same."""
    if isinstance(other, Point):
      return (
        self.x == other.x
        and self.y == other.y
      )
    else:
      return False

  def __repr__(self) -> str:
    """Returns a string representation of the point."""
    return "Point({!r}, {!r})".format(self.x, self.y)

