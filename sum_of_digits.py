t = int(input())
for i in range(t):
    x = int(input())
    sum_digits = 0
    while x != 0:
        digit = x % 10       # Extract the last digit
        sum_digits += digit  # Add the digit to the sum
        x //= 10             # Integer division to remove the last digit
    print(sum_digits)        # Print the sum for the current test case