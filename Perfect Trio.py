# cook your dish here
"""Perfect Trio
Chef defines a group of three friends as a perfect group if the age of one person is equal to the sum of the age of remaining two people.

Given that, the ages of three people in a group are A,B and C
 respectively, find whether the group is perfect."""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+b==c or b+c==a or a+c==b):
        print("yes")
    else:
        print("no")