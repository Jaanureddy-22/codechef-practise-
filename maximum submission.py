# cook your dish here
"""Here the condition is A participant can make 
1
1 submission every 
30
30 seconds. If a contest lasts for 
X
X minutes, what is the maximum number of submissions that the participant can make during it?

It is also given that the participant cannot make any submission in the last 
5
5 seconds of the contest."""




#code for maximum submission
t=int(input())
for i in range(t):
    x=int(input())
    print(int((x*60)/30))