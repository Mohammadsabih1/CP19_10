#Written by(Mohammad Sabih)

numberstop="x"
positive=0
negative=0
i=1
while (i<=83):
    num=int(input("Please enter a number==>"))
    if(num>0):
        positive+=1
    elif(num<0):
        negative+=1
    if numberstop==input("Please enter a number to continue or x to Exist==>"):
        break
    i+=1    
print("Total positive number is==>",positive)
print("Total negative number is==>",negative)