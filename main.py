# main.py
def greet():
    print("Hello, World!")

if __name__ == "__main__":
    greet()
# main.py
def greet():
    print("Hello, World!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    greet()
    print("Add 5 + 3 =", add(5, 3))
    print("Subtract 5 - 3 =", subtract(5, 3))

x = 5
b = 10

if x > b:
    print("x is greater than b")
elif b > x:
    print("b is greater than x")
else:
    print("both are not greater than each other")
