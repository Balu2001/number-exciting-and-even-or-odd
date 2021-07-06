#number is excited or not in gien numbers
n=int(input())
j=int(input())
found=0
while (n):
    r=n%10
    if(r==j):
        found=1
        print(j,'is found in ',n)
        break
    else:
        print(j,'is not found in ',n)
        break
    n=n//10   