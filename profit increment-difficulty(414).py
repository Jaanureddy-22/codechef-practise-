# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    selling_amt=x-y              #the actual now selling the fruits    
    add_dis=x+(x*0.1)            #the amonut that seller rice 10% per 100/-
    fdis=add_dis - selling_amt    #the profit that he gained after incrementing
    print(int(fdis))
    
