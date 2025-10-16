def greet(name):
    print('hello',name)
greet('hemanth')

def c_r(r):
    return 3.14*r*r
print(c_r(0))


def add(a,b):
    return a+b

print(add(10,100))


def math_operations(a, b):
    return a + b, a - b, a * b

add, sub, mul = math_operations(10, 5)
print("Add:", add, "Sub:", sub, "Mul:", mul)
