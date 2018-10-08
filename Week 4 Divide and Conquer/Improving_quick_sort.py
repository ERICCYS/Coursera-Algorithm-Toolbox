import random

def read_input():
	n = int(input())
	A = list(map(int,input().split()))
	return n,A

def randomized_stress_test():
	n = random.randint(1,100)
	A = []
	for i in range (n):
		A.append(random.randint(0,10))
	return n,A

def Partition3(A,l,r):
	j = l
	for i in range (l + 1, r):
		if A[i] == A[j]:
			j += 1
			A[i],A[j] = A[j],A[i]

	k = j
	for i in range (j + 1, r):
		if A[i] < A[j]:
			k += 1
			A[i],A[k] = A[k],A[i]

	for i in range (l, j + 1):
		A[i],A[k + l - i] = A[k + l - i],A[i]

	return l + k - j, k + 1

def QuickSort(A,l,r):
	if l >= r:
		pass
	else:
		k = random.randint(l,r - 1)
		A[k],A[l] = A[l],A[k]
		m1,m2 = Partition3(A,l,r)
		QuickSort(A,l,m1)
		QuickSort(A,m2,r)

n,A = read_input()
QuickSort(A,0,len(A))
for a in A:
	print(a,end = ' ')
