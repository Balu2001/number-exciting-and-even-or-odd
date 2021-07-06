#adding even and odd number inthe given number
n=int(input())
j=n
e_count=0
o_count=0
while (n):
    r=n%10
    if(r%2==0):
        e_count+=1
    else :
        o_count+=1
    n=n//10
print('there are',e_count, 'even number and ',o_count,'odd number in given ',j,' numbers')
    
