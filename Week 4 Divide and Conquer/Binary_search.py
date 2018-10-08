import math

def read_input():
	List_1 = list(map(int,input().split()))
	n = List_1[0]
	num_list = List_1[1:]
	List_2 = list(map(int,input().split()))
	k = List_2[0]
	search_list = List_2[1:]
	return n, num_list, k, search_list

def Binary_search(number,num_list,lb,hb,length):
	mid = math.floor(lb + 0.5*(hb - lb))
	if number == num_list[mid]:
		return mid
	elif length > 1:
		if number > num_list[mid]:
			lb = mid + 1
			return Binary_search(number,num_list,lb,hb,(hb - lb + 1))
		else:
			hb = mid - 1
			return Binary_search(number,num_list,lb,hb,(hb - lb + 1))
	else:
		return -1


n, num_list, k, search_list = read_input()
lb = 0
hb = len(num_list) - 1
length = len(num_list)
result = []

for number in search_list:
	result.append(Binary_search(number,num_list,lb,hb,length))

for element in result:
	print(element,end = ' ')

print()
