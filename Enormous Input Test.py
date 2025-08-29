"""----Enormous Input Test------
You are given N integers. Find the count of numbers divisible by K.

----Input Format----
The input begins with two positive integers N, K. The next N lines contains one positive integer each denoted by Ai​

------Output Format---
Output a single number denoting how many integers are divisible by K."""

(n, k) = map(int, input().split())

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)	

