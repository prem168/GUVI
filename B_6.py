x=int(input())
if x%4==0:
	if x%100==0 and x%400!=0:
		print("no")
	else:
		print("yes")
else:
	print("no")
