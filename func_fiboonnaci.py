def fibonacci():
    a,b = 1,1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for i in range(100000):
    print(next(gen))


