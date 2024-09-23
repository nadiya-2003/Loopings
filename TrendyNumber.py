n=int(input())
if(n>=100 and n<=999):
    a=n//10
    b=n%10
    if(b//3==0):
        print("Trendy Number")
    else:
        print("Not a Trendy number")
else:
    print("Not a Trendy Number")
