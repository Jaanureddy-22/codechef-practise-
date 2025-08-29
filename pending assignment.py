"""Pending Assignments
Chef has finally decided to complete all of his pending assignments.

There are X assignments where each assignment takes Y minutes to complete.
Find whether Chef would be able to complete all the assignments in Z days."""
# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (x*y <= z*1440):
        print("YES")
    else:
        print("NO")
