def Compute_Fibo_sum_last_digit(n):
	a = 0
	b = 1
	Last_digt_of_sum = 0
	for i in range(n%60):
		a, b = b % 10, (a+b) % 10
		Last_digt_of_sum += a
		Last_digt_of_sum %= 10
	return Last_digt_of_sum 
	
n = int(input())
print(Compute_Fibo_sum_last_digit(n))
