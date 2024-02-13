"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility Principle

def f(x): # assinatura
    result = 5 * (x / 2) # corpo da função
    return result


def double(x):
    return x * 2

valor = double(f(10))

print(valor) # 25.0
print(valor == 50)

####


def print_in_upper(text):
    """Procedure with no explicit return value. Implicitly returns None."""
    print(text.upper())

print_in_upper("Hello, World!") # HELLO, WORLD!

def heron(a, b, c):
    """Calculates the area of a triangle using Heron's formula."""
    perimeter = (a + b + c)
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # square root
    return area

triangle_area = heron(3, 4, 5)
print(triangle_area) # 6.0

triangles = [
    (3,4,5),
    (6,8,10),
    (9,12,15),
    (7,24,25),
    (8,15,17)
]

for t in triangles:
    area = heron(*t) # unpacking the tuple
    print(f"A area do triangulo é {area}") # 6.0, 24.0, 54.0, 84.0, 60.0

####

