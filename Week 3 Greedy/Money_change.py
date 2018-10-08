def change_return(m):
	counter = 0
	counter += (m // 10)
	m = m % 10
	counter += (m // 5)
	m = m % 5
	counter += m
	return counter
while True:
	m = int(input())
	print(change_return(m))
