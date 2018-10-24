#Abhishek Satkar
#11810805
#M 52

n=int(input("Enter number of terms"))
if n<=0:
 print("invalid")
elif num==1:
 print("0")
elif n==2:
 print("0,1")
else:
 y=[0,1]
 i=0,a=0,b=1
 for i in range(n-2):
  f=a+b 
  y.append(f)
  a=b
  b=f 
  print(y)
