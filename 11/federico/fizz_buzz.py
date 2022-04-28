def fizz_buzz(n):

    # Initialize result
    result = -1

    # Calculate Output
    if (n % 3 == 0) and (n % 5 == 0):
        result = "Fizz Buzz"
    elif (n % 3 == 0):
        result = "Fizz"
    elif (n % 5 == 0):
        result = "Buzz"
    else:
        result = n

    return result

if __name__ == "__main__":
    print(fizz_buzz(15))