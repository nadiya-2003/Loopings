n=int(input())
a=0
b=0
c=1
print(a,end=’ ‘)
print(b,end=’ ‘)
print(c,end=’ ‘)
for i in range (4,n+1):
	d=a+b+c
	a=b
	b=c
	c=d
	print(d,end=’ ‘)
