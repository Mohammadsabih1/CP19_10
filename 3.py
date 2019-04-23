#Program(Perfect Square)
#Written by(Mohammad Sabih)

import math
a=input("Please enter a number=")
while(a!="x"):
	a=int(a)
	sqrt=math.sqrt(a)
	if(int(sqrt)==float(sqrt)):
	    print(a,"is a perfect square")
	else:
	    print(a,"not a perfect square")
	a=input("Please enter a number=")
print("The End")
