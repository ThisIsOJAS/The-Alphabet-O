n=int(input("The height of my alphabet : "))

if(n==1):
    print("*")

else:
    for i in range(1,int(n/5)+2):
        for j in range(1,n+1):
            print("*",end="")
        print()
        
    for i in range(int(n/5)+2,n-int(n/5)):
        for j in range(1,2):
            print('*'*(int(n/5)+1)+' '*(n-(2*(int(n/5)+1)))+'*'*(int(n/5)+1),end=" ")
        print()
        
    for i in range(n-int(n/5),n+1):
        for j in range(1,n+1):
            print("*",end="")
        print()
