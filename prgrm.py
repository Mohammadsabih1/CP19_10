num=int(input("ENTER A NUMBER: "))
for i in range(num-1):
	print((num-i)*" "+(2*i+1)*"*")
for i in range(num-1,-1,-1):
	print((num-i)*" "+(2*i+1)*"*")