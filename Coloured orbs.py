# cook your dish here
r,b=map(int,input().split())
if r <= b:
    print(r*5+abs(r-b)*2)
else:
    print(b*5+abs(r-b)*1)