f=open("train_content","r")
x=""
y=1
for i in f:
   r=i
   if(i==""):
       print(i)
       print(y)
   if(x==r):
       print(x)
       print(y)
   y=y+1
   x=r
