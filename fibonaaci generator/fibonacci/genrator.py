def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def main():
    while True:
        try:
            num = int(input("Enter the number of Fibonacci numbers to generate: "))
            if num < 0:
                print("Please enter a positive integer.")
                continue
            fib_gen = fibonacci_generator(num)
            print(f"The first {num} Fibonacci numbers are:")
            for fib_num in fib_gen:
                print(fib_num, end=" ")
            print()  # For a new line
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
