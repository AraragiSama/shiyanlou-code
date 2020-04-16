a = 0
for i in range(1,101):
	if i % 7 == 0:
		a=a+1
	elif (i // 10 ==7 or i % 10 ==7):
		a=a+1
	else:
		print(i)

