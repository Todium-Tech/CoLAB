#Binary Search 
def binary(arr,ele):
    start,end=0,(len(arr)-1)
    while start<=end:
        mid=(start+end)//2
        if ele==arr[mid]:
            return mid
        if ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return False
a=int(input("Enter the No Of Elements"))
l=[]
for i in range(a):
    g=int(input("Enter tHe Element"))
    l.append(g)
b=int(input("Ente The Search Element"))
h=binary(l,b)
print(h)
        
