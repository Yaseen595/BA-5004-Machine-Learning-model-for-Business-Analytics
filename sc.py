# example.py - A Python file with various code examples

def greet(name):
    """A simple greeting function"""
    print(f"Hello, {name}!")

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

class Circle:
    """A simple Circle class"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle"""
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * 3.14159 * self.radius

if __name__ == "__main__":
    # Demonstrate the functions and class
    greet("Python Developer")
    
    print("\nArea calculation (5x7):", calculate_area(5, 7))
    
    num = 10
    print(f"\nIs {num} even?", is_even(num))
    
    fib_terms = 8
    print(f"\nFirst {fib_terms} Fibonacci numbers:", fibonacci(fib_terms))
    
    my_circle = Circle(5)
    print(f"\nCircle with radius {my_circle.radius}:")
    print("Area:", my_circle.area())
    print("Circumference:", my_circle.circumference())