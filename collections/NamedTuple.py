# Named Tuple collection
from collections import namedtuple

# Create a named tuple collection named point and contains the fields x,y with its values stored in the pt var
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)