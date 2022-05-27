# Question-1:
# list=[8,2,3,-1,7]
# def multiply(*list):
#     total=1
#     for i in list:
#         total*=i
#     print(f"Total Multiplication = {total}")
# multiply(*list)

# Question-2:
# list=[8,2,3,0,7]
# def sum(*list):
#     total=0
#     for i in list:
#         total+=i
#     print(f'Total sun  of the list is {total}')
# sum(*list)

# Question-3:
# def minimum():
#     num1=int(input("Enter 1st number\n"))
#     num2=int(input("Enter 2nd number\n"))
#     num3=int(input("Enter 3rd number\n"))
#     # min=min(num1,num2,num3)
#     # print(f"Minimum value is {min}")
#     if(num1<num2 and num1<num3):
#         print(f'Minimum value is {num1}')
#     elif(num2<num1 and num2<num3):
#         print(f'Minimum value is {num2}')
#     else:
#         print(f'Minimum value is {num3}')
# minimum()

# Question-4:
# def fizz_buzz():
#     num=int(input("Enter a number\n"))
#     if(num%3==0 and num%5==0):
#         print("FizzBuzz")
#     elif(num%3==0):
#         print("Fizz")
#     elif(num%5==0):
#         print("Buzz")
#     else:
#         pass
# fizz_buzz()

# Question-5:
# def hello(name,age):
#     print(f'Your name is {name} and ypur age is {age}')
# hello("Ram",20)

# Question-6:
# def maximum():
#     num1=int(input("Enter 1st number\n"))
#     num2=int(input("Enter 2nd number\n"))
#     num3=int(input("Enter 3rd number\n"))
#     if(num1>num2 and num1>num3):
#         print(f'Maximum value is {num1}')
#     elif(num2>num1 and num2>num3):
#         print(f'Maximum value is {num2}')
#     else:
#         print(f'Maximum value is {num3}')
# maximum()

# Question-7:
# list=[1,2,3,4,5,6]
# def check(*list):
#     print("Even numbers are ",end="")
#     for i in list:
#         if(i%2==0):
#             print(i,end=",")
#         else:
#             pass
# check(*list)

# Question-8:
# list=[1,2,3,4,5,6]
# def odd(*list):
#     print("Odd numbers are ",end="")
#     for i in list:
#         if(i%2!=0):
#             print(i,end=",")
# odd(*list)


# Question-9:
# num=int(input("Enter a number\n"))
# def check_prime(num):
#     if(num==1):
#         print("f{num} is a prime number")
#     elif(num==2):
#         print(f'{num} is a prime number')
#     elif(num==3):
#         print(f'{num} is a prime number')
#     elif(num%2 is  0 or num%3 is   0):
#         print(f'{num} is a not prime number')
#     else:
#         print(f'{num} is a prime number')
# check_prime(num)


# Question-10:
# str=input("Enter a string\n")
# def reverse_string(str):
#     print(str[::-1])
# reverse_string(str)


# Question-11:
# name=input("Enter your name\n")
# age=int(input("Enter your age\n"))
# def display(name,age):
#     print(name,age)
# display(name,age)




# Question-12:
# def func1(num1,num2,num3):
#        print(num1,num2,num3)
# func1(10,20,30)

# Question-13:
# num1=int(input("Enter 1st Number\n"))
# num2=int(input("Enter 2nd number\n"))

# def calculation(num1,num2):
#     return num1+num2,num1-num2
# sum,sub=calculation(num1,num2)
# print(f"The sum of {num1} and {num2} is {sum}")
# print(f'The subtraction of {num1} and {num2} is {sub}')

# Question-14:
# name=input("Enter Your name\n")
# def show_employee(name,salary=9000):
#     print(f'Your name is {name} and your salary is {salary}')
# show_employee(name)

# Question-15:
# list=[4, 6, 8, 24, 12, 2]
# def largest(*list):
#         print(max(list))
# largest(*list)

#Question-16:
# list=[4,6,8,24,12,2]
# def small(*list):
#     print(min(list))
# small(*list)

# Question-17:
# num=int(input("Enter rollnumber\n"))
# def check(num):
#   list=[10,20,14,16,22,17]
#   if num in list:
#       print(f'Roll number {num} is present')
#   else:
#       print(f'Roll number {num} is absent')
# print(check(num))
#
# Question-18:
# num=int(input("Enter a number\n"))
# def check(num):
#     if(num%2==0):
#         return(f"{num} is an even number")
#     else:
#         return(f'{num} is an odd number')
# print(check(num))


# Question-19:
# str=input("Enter a string\n")
# def count(str):
#     string=str.lower()
#     vowel=0
#     consonant=0
#     for i in string:
#         if(i=="a" or i=="e"or i=="i" or i=="o" or i=="u"):
#             vowel+=1
#         elif(i==" "):
#             pass
#         else:
#             consonant+=1
#     print(f'Number of vowel is {vowel} and number consonant is {consonant}')
# count(str)

# Question-20:
# num=int(input("Enter a number\n"))
# def factorial(num):
#     total=1
#     if(num==0):
#          return(f'factorial of {num} is 1')
#     elif(num==1):
#          return(f'Factorial of {num} is 1')
#     else:
#         for i in range(1,num+1):
#               total*=i
#         return(f'Factorial of {num} is {total}')
# print(factorial(num))
# Question-21:
# str=input("Enter a word\n")
# def convert(str):
#     string=str.upper()
#     return string
# print(convert(str))

# Question-22:
# from cmath import pi

# radius=int(input("Enter radius of circle\n"))
# def area(r):
#     area=pi*(r*r)
#     return (f'The area of cirlce is {area}')
# print(area(radius))

# import main
# main.add(8,7)









