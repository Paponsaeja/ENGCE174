
# รูปแบบที่ 1
def one(height) :
    left = ""    # for string 
    for i in range(1, height + 1):
        left += '*' * i+ "\n" 
    return left

# รูปแบบที่ 2
def two(height) :
    leftupsidedown = ""
    for i in range(height, 0, -1):
        leftupsidedown += '*' * i + '\n'
    return leftupsidedown


# รูปแบบที่ 3
def three(height):
    tree_lines = []  # Initialize an empty list to store each line of the tree
    max_width = height * 2 - 1  # Calculate the maximum width of the tree

    for i in range(height):
        # Create the line with asterisks and spaces
        line = "* " * (i + 1)
        # Strip the trailing space and center the line
        centered_line = line.rstrip().center(max_width)
        # Append the centered line to the list
        tree_lines.append(centered_line)
    
    return "\n".join(tree_lines)  # Join all lines with newline characters


# รูปแบบที่ 4
def four(height): 
    tree_lines = []
    max_width = height * 2 - 1 
    for i in range(height, 0, -1):
        line = "* " * i
        centered_line = line.rstrip().center(max_width)
        tree_lines.append(centered_line)
    return "\n".join(tree_lines)


# รูปแบบที่ 5
def five(height):
    treelast = ""
    for i in range(height):
        for j in range(height - i - 1):
            treelast += " "
        for k in range(i+1):
            treelast += "*"
        treelast += "\n"
    return treelast





def all_tree(height):
    pattern1 = one(height)
    pattern2 = two(height)
    pattern3 = three(height)
    pattern4 = four(height)
    pattern5 = five(height)
    return pattern1, pattern2, pattern3, pattern4, pattern5 

height = int(input("Enter the number of stars: "))
result1 , result2 , result3 , result4 , result5 = all_tree(height)

# Define a list of results to iterate over
results = [result1, result2, result3, result4, result5]
patterns_names = ['Pattern 1', 'Pattern 2', 'Pattern 3', 'Pattern 4', 'Pattern 5']

# Use a for loop to print each pattern with its corresponding name
for name, pattern in zip(patterns_names, results):
    print(f"\n{name}:\n{pattern}")
