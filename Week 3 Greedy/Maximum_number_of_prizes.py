def dividing(n):
	prizes = []
	i = 1
	while n >= i:
		prizes.append(i)
		n -= i
		i += 1
	prizes[-1] += n
	print(len(prizes))

n = int(input())
dividing(n)
