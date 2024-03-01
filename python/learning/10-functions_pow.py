def power(value):
    times = 0
    while times != value:
        new_value = value * value
        times += 1
    return new_value    

def main():
    pass


if __name__ == "__main__":
    function_value = int(input("Introduce un número: "))
    print(power(function_value))

