def LFSR():
	a = [{seed: list data type}] #Variable is the seed
	for i in range(0, 2001, 1):
		a[0] = (a[9] ^ a[6])
		print(a[0], end="")
		for i in range (10, -1, -1):
			a[i] = a[i-1]

if __name__ == "__main__":
	LFSR()
