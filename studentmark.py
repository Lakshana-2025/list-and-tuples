x=int(input("enter the number"))
d={}
for i in range(x):
    n=input("Enter name:")
    m=input("Enter marks:")
    d[n]=m
while True:
    n=input("Enter name for finding marks:")
    m=d.get(n,-1)
    if m==-1:
        print("not found")
    else:
        print(n,"==>",m)
    opt=input("Do you want to find another information [Yes|No]")
    if opt=="No":
        break
print("Thank you")
