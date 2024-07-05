def fibonacci():
    a, b = 0, 1 
    while True:
        yield a 
        a, b = b, a + b 

fib = fibonacci()
print(next(fib)) # 0
print(next(fib)) # 1 
# 0 1 1 2 3 5 8 
