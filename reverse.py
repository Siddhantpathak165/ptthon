n=int(input())
r=0
while n>0 :
    r=n%10
    r=(r*10)+r
    n=n//10
print("reverse",r)
