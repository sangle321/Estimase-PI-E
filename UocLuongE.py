import math

def fatorial(n):
	if n == 0:
		return 1;
	return n * fatorial(n-1)


def Estimase_E(n):
	result  = 1
	for i in range(1,n):
		result = result + 1/fatorial(i)
	return result

print(Estimase_E(10))