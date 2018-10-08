import numpy as np

def input_info():
	n = int(input())
	profits = list(map(int,input().split()))
	clicks = list(map(int,input().split()))
	profits.sort()
	clicks.sort()
	return n,profits,clicks

n,profits,clicks = input_info()
print(np.dot(profits,clicks))
