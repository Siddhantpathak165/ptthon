n=int(input())
sum=0
tmp=n
while tmp>0 :
    d=tmp%10
    sum +=d**3
    tmp //=10
if n==sum :
    print("it is an armstrong" ,n)
else :
    print("it is not armstrong",n)























