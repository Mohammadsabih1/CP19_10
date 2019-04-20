#Assignment:4
#task 2
#Author Salman Hameed

pattern_length = int(input("Enter a Pattern Length : "))
num1 = int(input("Enter a First Number : "))
num2 = int(input("Enter a Second Number : "))
def pattern(num1,num2):
    for a in range(1,pattern_length):
        for b in range(1,pattern_length+1-a):
            print(" ",end=" ")
        for c in range(1,a):
            print(num2 ,end=" ")
        for d in range(1,2):
            print(num1 ,end=" ")
        for e in range(1,1*a):
            print(num2 ,end=" ")
        print("")
    for f in range(1,pattern_length+pattern_length):
        print(num1,end=" ")
    print("")
    for a in range(1,pattern_length):
        for b in range(1,a+1):
            print(" ",end=" ")
        for c in range(1,pattern_length-a):
            print(num2 ,end=" ")
        for d in range(1,2):
            print(num1 ,end=" ")
        for e in range(1,pattern_length-1*a):
            print(num2 ,end=" ")
        print("")
        
pattern(num1,num2)