def input_info():
	n = int(input())
	number_strings = input().split()

	lengths = []
	for number_string in number_strings:
		lengths.append(len(number_string))
	max_length = max(lengths)

	info = []
	for number_string in number_strings:
		info_piece = []
		info_piece.append(number_string)
		for i in range (max_length):
			info_piece.append(int(number_string[i % len(number_string)]))

		info_piece.append((number_string[-1]))
		info.append(info_piece)
	for i in range ((len(info_piece) - 1),0,-1):
		info = sorted(info, key = lambda info: info[i])

	return info


def max_salary(info):
	max_salary = ''
	for i in range ((len(info) - 1), -1, -1):
		max_salary += info[i][0]

	max_salary = int(max_salary)
	print(max_salary)

info = input_info()
max_salary(info)
