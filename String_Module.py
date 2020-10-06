sr=input("enter the string")
print("the length of the string is----",len(sr))
print("traversing  string seprated by @----")
for i in range(len(sr)):
    print(sr[i],'@',end=" ")
print()
print("multipling the string a*2----",sr*2)
print("adding \"bye\"+\"hi\"----","bye"+"hi")
print("using the \"b\" in \"belgin\"---","b" in "belgin")
print("using the \"b\" not in \"belgin\"----","b" not in "belgin")
print("printing the ACSII value of \"a\"ord('a')----",ord('a'))
print("Captilize----",sr.capitalize())
print("find----",sr.find("gi"))


