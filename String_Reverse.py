
def Using_My_Method():
    a="belgin Android"
    rev=""
    for i in range(len(a)-1,-1,-1):
        rev=rev+a[i]
    print(rev) 

def Using_Method_1():
    a="Belgin"
    rev=""
    temp=list(a)
    temp.reverse()
    for i in temp:
        rev=rev+i
    print(rev)    


    
