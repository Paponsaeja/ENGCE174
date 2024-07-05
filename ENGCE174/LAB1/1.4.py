numbers = [1,2,3,4,5]

# accessing elements
print("Fisrt element:", numbers[0]) # 1
print("Last element:", numbers[-1]) # 5

#slicing 
print("sliced elements:", numbers[2:4]) # [3,4]

# appending and extending 
numbers.append(6)
print( "After append:", numbers) # [1,2,3,4,5,6]

#remving element
numbers.remove(3)
print( "after remival:", numbers) # [1,2,4,5,6]