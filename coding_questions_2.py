def count_squares_recursive(X):
    # Base case: If X is 1, return 1
    if X == 1:
        return 1
    # Recursive case: Sum the squares of X and the result for X-1
    else:
        return X ** 2 + count_squares_recursive(X - 1)


# tests
if __name__ == '__main__':
    print(count_squares_recursive(2))  # Output: 5 => 1+4
    print(count_squares_recursive(3))  # Output: 14 => 1+4+9
    print(count_squares_recursive(4))  # Output: 30 => 1+4+9+16
