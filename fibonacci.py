n=int(input("Enter limit=>"))
l=[]
a=0
b=1
count=0
if n<=0:
   print("series DNE")
elif n==1:
     print("0")
elif n==2:
     print("0,1")
else:
     l.append(0)
     l.append(1)
     while count<n-2:
           c=a+b
           l.append(c)
           a=b
           b=c
           count+=1
print(l)