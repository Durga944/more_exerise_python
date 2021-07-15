# que1
# num=int(input("enter any num:-"))
# i=1
# while i<=num:
#     if i%3==0 or i%5==0:
#         print(i,end="  ")
#     i=i+1


# que2
# year=int(input('enter any year:'))
# if year%4==0:
# 	if year%100==0:
# 		if year%400==0:
# 			print('year is century leap year')
# 		else:
# 				print('not century leap year')
# 	else:
# 		print('leap year')
# else:
# 	print('not leap year')

# que3
# i = 1  
# while i<=10:
#     n=2*i-1
#     print(n)
#     i=i+1

# que4
# i=1
# c=0
# while i>0:
#     if i%2==0:
#         print(i)
#         c=c+1
#     if c==10:
#         break
    # i=i+1


# que5
num = int(input("enter any num"))
n = num
n1 = num
c = 0
print(" even number from 10")
while n>0:
    if n%2==0:
        print(n)
        c=c+1
    if c==3:
        break
    n=n-1
d = 0
print(" odd number from 10")
while n1 > 0:
    if(n1 % 2 != 0):
        print(n1)
        d = d + 1
        n1 = n1 - 1
        if(d == 3):
            break
    else:
        n1 = n1 - 1

