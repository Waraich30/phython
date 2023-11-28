def takeinput():
    A=float(input("Enter First Number: "))
    print("Number 1: ",A)
    B=float(input("Enter Second Number: "))
    print("Number 2: ",B)
    C=str(input("Enter Operation: "))
    print("Your operation: ",C)
    return A,B,C

    
def diplayresult():
    A,B,C=takeinput()
    if C=="+":
        ans=A+B
        print("Ans: ",ans)    
    
    elif C=="-":
        ans=A-B
        print("Ans: ",ans) 
    
    elif C=="*":
        ans=A*B
        print("Ans: ",ans) 
    
    elif C=="/":
        ans=A/B
        print("Ans: ",ans) 
    else:
        print("You Entered the wrong operator!")
        
diplayresult()