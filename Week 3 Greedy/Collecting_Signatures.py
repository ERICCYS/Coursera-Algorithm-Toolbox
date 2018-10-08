def input_info():
	n = int(input())
	info = []
	for i in range (n):
		info.append(list(map(int,input().split())))

	info = sorted(info,key = lambda info: info[1])
	info = sorted(info,key = lambda info: info[0])
	print(info)
	return info

def determine_points(info):
	if len(info) == 1:
		return 1,[info[0][1]]
	else:
		leftend = info[0][0]
		rightend = info[0][1]
		common_points_left = []
		common_points_right = []
		segment_junctions = []
		for i in range(1,len(info)):
			if (info[i][0] <= rightend) and (len(common_points_right) == 0 or info[i][0] <= min(common_points_right)):
				common_points_left.append(info[i][0])
				if (info[i][1] <= rightend):
					common_points_right.append(info[i][1])
			else:
				if common_points_right == []:
					segment_junctions.append(rightend)
				else:
					segment_junctions.append(min(common_points_right))

				common_points_right = []
				common_points_left = []
				leftend = info[i][0]
				rightend = info[i][1]
				common_points_left.append(leftend)
				
		if common_points_right == []:
			segment_junctions.append(max(rightend,max(common_points_left)))
		else:
			segment_junctions.append(min(common_points_right))	

		return len(segment_junctions),segment_junctions

info = input_info()
length,points = determine_points(info)

print(length)
if length == 1:
	print(points[0])
else:
	for point in points:
		print(point,end = ' ')
	print()