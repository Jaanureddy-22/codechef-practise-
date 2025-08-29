"""Course Registration
There is a group of N friends who wish to enroll in a course together. The course has a maximum capacity of M students that can register for it. 
If there are K other students who have already enrolled in the course,
 determine if it will still be possible for all the N friends to do so or not."""
# cook your dish here
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if (abs(m-k) >= n):
        print("YES")
    else:
        print("NO")
