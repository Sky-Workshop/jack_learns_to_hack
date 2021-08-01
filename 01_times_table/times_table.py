#day1_step2.3: #trick: how to avoid printing 3*2, 4*2, 4*3 ...? breakpoint will be helpful!
for i in range(1, 9):
	for j in range(i, 9):
		print(i+1, "*", j+1, "=", (i+1)*(j+1))
	print("---------")