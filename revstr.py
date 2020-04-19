s=input()
c=0
l=list(s)
#print(l)
a=l[::-1]
#print(a)
for i in a:
    if i=="_":
        c=c+1
    else:
        break
#print(c)
a=l[:len(l)-c]
#print(a)
j=''
d=1
i=0
e=2
while d<=c:
    if a[i]=="_":
        a.insert(i+1,"_")
        #print(b)
        i=i+e
        d=d+1
    else:
        i=i+1
    if i==len(a)-1:
        i=0
        e=e+1
    j=''.join(a)
print(j)
