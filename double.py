def generate_square_dict(n):
    square_dict = {}
    for x in range(1, n + 1):
        square_dict[x] = x * x
    return square_dict

if __name__ == "__main__":
    try:
        n_str = input("Enter an integer (n): ")
        n = int(n_str)

        if n < 1:
            print("Please enter a positive integer.")
        else:
            result_dict = generate_square_dict(n)
            print(f"Generated dictionary: {result_dict}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
