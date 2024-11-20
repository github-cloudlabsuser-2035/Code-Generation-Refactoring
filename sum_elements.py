MAX = 100

def calculate_sum(arr):
    return sum(arr)

def main():
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            return

        arr = []
        print(f"Enter {n} integers:")
        for _ in range(n):
            try:
                arr.append(int(input()))
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                return

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()