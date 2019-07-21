import random
import math

def UocLuong():
	N = 10000
	N_T = 0 
	for _ in range(N):
		x = random.random()*2 - 1
		y = random.random()*2 - 1

		x1 = math.pow(x,2)
		y1 = math.pow(y,2)

		if math.sqrt(x1+y1) <= 1:
			N_T += 1
	pi = (N_T/N)*4
	print(pi)

UocLuong()
		
