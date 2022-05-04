def fizz_buzz(n):

    # Initialize result
    result = n

    # Calculate Output
    try:
        if (n % 3 == 0) and (n % 5 == 0):
            result = "Fizz Buzz"
        elif (n % 3 == 0):
            result = "Fizz"
        elif (n % 5 == 0):
            result = "Buzz"
        elif (n % 100 == 0):
            result = "Surprise!"
        else:
            result = n
    except:
        print("Not a number")

    return result

if __name__ == "__main__":
    print(fizz_buzz(15))