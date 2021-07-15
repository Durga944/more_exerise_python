# list=[1,1,2,3,4,4,5,1]
# str = "aabcddddadnss"

num=int(input('enter a num='))
a=num
sum=0
count=0
while a>0:
	count=count+1
	a=a//10
a=num
while a>0:
	rem=a%10
	sum=sum+(rem**count)
	a=a//10
if num==sum:
	print(num,'armstrong number')
else:
	print(num,'not armstrong number')


