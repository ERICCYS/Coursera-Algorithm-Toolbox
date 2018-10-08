import random

def MergeSort(A,inversion):
	length_A = len(A)
	if length_A > 1:
		m = length_A // 2
		B,inversion = MergeSort(A[:m],inversion)
		C,inversion = MergeSort(A[m:],inversion)
		A, inversion = Merge(B,C,m,(length_A - m),inversion)
	return A,inversion

def Merge(B,C,m,n,inversion):
	D = []
	length_B = m
	length_C = n
	while length_B * length_C != 0:
		if B[0] <= C[0]:
			D += [B[0]]
			B = B[1:]
			length_B -= 1
		else:
			D += [C[0]]
			inversion += length_B
			C = C[1:]
			length_C -= 1
	D += (B + C)
	return D, inversion

inversion = 0
n = int(input())
A = list(map(int, input().split()))
A, inversion = MergeSort(A,inversion)
print(inversion)
