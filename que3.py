# question 1 .......

redius = int(input("enter the redius..."))
area = (22/7)*redius
print(area)

#  question 2 ......
fahrenheit = int(input("enter the tempreture....."))
c = (fahrenheit - 32)*5/9
print(c)
    
    
# question 3.....
num1 = int(input ("enter the number......."))
num2 = int(input ("enter the number......."))
if num1 > num2 :
    print(num1 ,"is greater than num2")
else:
    print(num2,"greater than num1 ")


# question 4 .......

num  = int(input ("enter the number......."))
if num % 2 == 0:
    print(num , "num is even....")
else:
    print(num, "num is odd....")


# question 5 ........
num1 = int(input ("enter the number......."))
num2 = int(input ("enter the number......."))
num3 = int(input ("enter the number......."))
num4 = int(input ("enter the number......."))
num5 = int(input ("enter the number......."))

sum = num1 + num2 + num3 + num4 + num5
average = sum/5
print(average)