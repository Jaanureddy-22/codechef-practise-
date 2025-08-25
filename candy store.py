"""Candy Store
Chef has started working at the candy store. The store has 
100
100 chocolates in total.

Chef’s daily goal is to sell 
X chocolates. For each chocolate sold, he will get 
1 rupee. However, if Chef exceeds his daily goal, he gets 
2 rupees per chocolate for each extra chocolate.
If Chef sells Y chocolates in a day, find the total amount he made."""
t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    if x >= y:
        print(y)
    else:
        print(x+2*(y-x))
    t -= 1
