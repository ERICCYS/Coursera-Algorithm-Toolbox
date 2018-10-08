def input_info():
	info = []
	n, W = input().split()
	n = int(n)
	W = int(W)
	for i in range(n):
		value_weight_ratio = []
		v, w = input().split()
		value_weight_ratio.append(int(v))
		value_weight_ratio.append(int(w))
		value_weight_ratio.append(int(v)/int(w))
		info.append(value_weight_ratio)

	info = sorted(info,key = lambda info: info[2])
	return (n,W,info)

def greedy_arranging(n,W,info):
	Total_Value = 0
	while (W >= 0) and (len(info) > 0):
		if (info[-1][1] < W):
			Total_Value += info[-1][0]
			W -= info[-1][1]
		else:
			Total_Value += W * info[-1][2]
			W -= W
		info.pop()
	return Total_Value

n,W,info = input_info()
print(info)
print(greedy_arranging(n,W,info))
