#day1_step2.2: omit 1*n and n*1, and add a group seprator
for i in range(1,9):
	for j in range(1,9):
		print(i+1, "*", j+1, "=", (i+1)*(j+1))
	print("---------")