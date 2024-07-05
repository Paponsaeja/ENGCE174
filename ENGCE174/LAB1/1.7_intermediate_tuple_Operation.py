coordinates = (3, 5)

# unpacking tuples 
x, y = coordinates
print( "x-coordinate:", x) # 3
print( "y-coordinate:", y) # 5

# tuple as keys in dictionary 
location = {(3, 5 ): "home", (10, 20): "office"}
print("Location at (3, 5):", location[(3, 5 )]) # home 