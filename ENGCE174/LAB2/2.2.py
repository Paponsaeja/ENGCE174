n = int(input("Enter the number of stars: "))

def star( n, current = 1 ):
    if current > n:
        return []
    else:
        return ['*' * current] + star(n, current + 1) # + ทำหน้าที่รวม list เข้าด้วยกัน

lines = star(5)     #  ['*', '**', '***', '****', '*****']
result = '\n'.join(lines)    # join จะทำการรวมสตริงและแทรก delimiter \n ระหว่างสตริงแต่ละตัว
print(result)

print("===========================================")

def star(n):
    if n == 0:
        return []
    else:
        return ['*' * n] + star(n - 1)

lines = star(5)    # ['*****', '****', '***', '**', '*']
result = '\n'.join(lines)  
print(result)

print("===========================================")

def star(n, current=1):
    if current > n:
        return []
    else:
        spaces = ' ' * (n - current)
        stars = ' '.join(['*'] * current)
        return [spaces + stars] + star(n, current + 1)

lines = star(5)
result = '\n'.join(lines)
print(result)

print("===========================================")

def inverted_star(n, current=1):
    if current > n:
        return []
    else:
        spaces = ' ' * (current - 1)
        stars = ' '.join(['*'] * (n - current + 1))
        return [spaces + stars] + inverted_star(n, current + 1)

lines = inverted_star(5)
result = '\n'.join(lines)
print(result)

print("===========================================")

def star(n, current=1):
    if current > n:
        return []
    else:
        spaces = ' ' * (n - current)
        stars = ''.join(['*'] * current)
        return [spaces + stars] + star(n, current + 1)

lines = star(5)
result = '\n'.join(lines)
print(result)

