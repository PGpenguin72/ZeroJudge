i=input()
a=i.split(" ")
M=int(a[0])
D=int(a[1])
s=(M*2+D)%3
if s==0:
 print("普通")
elif s==1:
 print("吉")
else:
 print("大吉")