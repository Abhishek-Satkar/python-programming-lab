
#Abhishek Satkar  11810805  M 52


def maximum(x,y):
  if x>y:
     return x
  return y
x=int(input())
y=int(input())
z=int(input())
a=maximum(z,maximum(x,y))
print(a)