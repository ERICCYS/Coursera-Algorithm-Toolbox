def One_round_compute(a,b,m,period):
	a = a % m
	b = b % m
	a,b = b, a+b
	period += 1
	return (a % m),(b % m),period

def period (m):
	a = 0
	b = 1
	period = 0
	while True:
		a,b,period = One_round_compute(a,b,m,period)
		if (a % m == 0):
			a,b,period = One_round_compute(a,b,m,period)
			if (a % m == 1):
				break;	
	return period - 1

def Fibo_modulo_with_period_concernd(n,m):
	a = 0
	b = 1
	for i in range(n % period (m)):
		a = a % m
		b = b % m
		a, b = b, a + b
	return (a % m)

n,m = input().split()
print(Fibo_modulo_with_period_concernd(int(n),int(m)))