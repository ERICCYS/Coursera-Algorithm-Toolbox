def Compute_Fibo_sum_last_digit(m,n):
	a = 0
	b = 1
	Last_digt_of_sum_part_1 = 0
	Last_digt_of_sum_part_2 = 0
	Last_digt_of_sum = 0

	for i in range(m % 60):
		Last_digt_of_sum_part_1 += a
		Last_digt_of_sum_part_1 %= 10
		a, b = b % 10, (a+b) % 10


	a = 0
	b = 1
	for i in range((n + 1) % 60):
		Last_digt_of_sum_part_2 += a
		Last_digt_of_sum_part_2 %= 10
		a, b = b % 10, (a+b) % 10


	Last_digt_of_sum = Last_digt_of_sum_part_2 - Last_digt_of_sum_part_1
	Last_digt_of_sum = Last_digt_of_sum + 10
	Last_digt_of_sum %= 10

	return Last_digt_of_sum

m,n = input().split()
print(Compute_Fibo_sum_last_digit(int(m),int(n)))
