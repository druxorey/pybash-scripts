def fibonacci_sequence(n):
    a, b = 1, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
        

def main():
    pass


if __name__ == "__main__": 
    fibonacci_sequence(int(input("Introduce la posición final de la secuencia de fibonacci: ")))
