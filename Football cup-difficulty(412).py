# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x!=y and x>y or x<y:
        print("no")
    elif x==0 and y==0:
        print("no")
    else:
        print("yes")
