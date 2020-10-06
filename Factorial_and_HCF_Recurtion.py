inp=int(input('''Enter 1 For Factorial  
                  2 HCF'''))
def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)
def HCF(a,b):
    if b==0:
        return a
    return(HCF(b,a%b))
if inp==1:
    inpu=int(input("enter the Number To Find Facorial"))
    print(fact(inpu))
    
elif inp==2:
    inpu1=int(input("enter the Number 1 To Find HCF"))
    inpu2=int(input("enter the Number 2 To Find HCF"))
    print(HCF(inpu1,inpu2))
    

    
