from collections import namedtuple

#define a named tuple
Point = namedtuple('point', ['x','y'])

# creat instances of the named tuple

p1 = Point(3,5)
p2 = Point(-1,2)

# Access element by name 
print( "Coordinates of p1:", p1.x, p1.y ) # 3 5 