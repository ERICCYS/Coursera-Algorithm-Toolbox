def GCD(a,b):
	if b == 0:
		return a
	else:
		return GCD(b,(a%b))

def LCM(a,b):
	return a * b // GCD(a,b)

a,b = input().split()
print(LCM(int(a),int(b)))