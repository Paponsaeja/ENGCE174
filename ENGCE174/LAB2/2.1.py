height = int(input("Enter the number of stars: "))

# รูปแบบที่ 1
for i in range(1, height + 1):
    print('*' * i)

print("-------------------------------------------------")

# รูปแบบที่ 2
for i in range(height, 0, -1):
    print('*' * i)

print("-------------------------------------------------")

# รูปแบบที่ 3
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()  # ขึ้นบรรทัดใหม่

print("-------------------------------------------------")

# รูปแบบที่ 4
for i in range(height, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()  # ขึ้นบรรทัดใหม่

print("-------------------------------------------------")

# รูปแบบที่ 5
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()  # ขึ้นบรรทัดใหม่
