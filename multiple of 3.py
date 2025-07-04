
n = int(input())
if n % 3 == 0:
    print(n)
else:
    # Find the remainder when n is divided by 3
    remainder = n % 3

    # If the remainder is 1, check if n-1 or n+2 is closer
    if remainder == 1:
        if abs(n - (n - 1)) <= abs(n - (n + 2)):
            print(n - 1)
        else:
            print(n + 2)
    # If the remainder is 2, check if n-2 or n+1 is closer
    else:
        if abs(n - (n - 2)) <= abs(n - (n + 1)):
            print(n - 2)
        else:
            print(n + 1)