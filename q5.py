def fact(n):
    if(n==1):
        return 1
    else:
        return(n*fact(n-1))
    
x=int(input("enter a number:"))
fact=fact(x)
print("the factorial of",x,"is",fact)

