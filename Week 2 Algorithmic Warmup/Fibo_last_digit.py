def Fibo_last_digit(n):
	a = 0
	b = 1
	for i in range(n):
		a = a % 10
		b = b % 10
		a, b = b, a + b
	return (a % 10)

n = int(input())
print(Fibo_last_digit(n))