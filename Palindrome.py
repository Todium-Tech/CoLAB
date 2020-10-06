#Palindrome Program Method 1
t=""
name=input("enter the Word You Want To Check Palindrome")
name=name.lower()
for i in name[::-1]:
    t=t+i
if t==name:
    print("palindrome")
    print(t)
else:
    print("Not palindrome")
    print(t)

