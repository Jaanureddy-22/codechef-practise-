# cook your dish here
"""-------Selling Coins----- 
Chef has A silver coins and B gold coins.
He can avail the following 2 deals (multiple times):
Sell 1 silver coin for Rs.1 Trade 
1 gold coin for 2 silver coins.
Chef is trying to sell all his coins and earn money now. How much money will Chef be able to earn?"""
a,b=map(int,input().split())
print(a+(b*2))
