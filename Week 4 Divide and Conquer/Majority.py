import math
def read_input():
	n = int(input())
	num_list = list(map(int,input().split()))
	num_list.sort()
	return n, num_list

n,num_list = read_input()
frequency = []
conti = 1
for i in range (len(num_list) - 1):
	if num_list[i] == num_list[i + 1]:
		conti += 1
	else:
		frequency.append(conti)
		conti = 1
max_conti = max(frequency)
half = len(num_list) // 2
if max_conti > half:
	print(1)
else:
	print(0)
