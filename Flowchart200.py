# Answer to the Question Number 1:

# num1 = int(input("Enter the first Number:"))
# num2 = int(input("Enter the second Number:"))
# print("Total sum is",num1+num2)

# Answer to the Question Number 2:

# num1 = int(input("Enter the first Number:"))
# num2 = int(input("Enter the second Number:"))
# average=(num1+num2)/2
# print(average)

# Answer to the Question Number 4:

# base=float(input("Enter the triange base:"))
# height=float(input("Enter the triangle height:"))
# area_of_triangle=(base*height)*1/2
# print(area_of_triangle)

# Answer to the Question Number 6:

# P = int(input("Enter the invested amount:"))
# I = int(input("Enter the interest percentage:"))
# N = int(input("Enter the number of years:"))

# T=  P*(1+I/100)**N
# print(f"Total amount of I'll have after 'N' years is{T:.2f}")

# Answer to the Question Number 7:

# A=int(input("Enter the first number:"))
# B=int(input("Enter the second number:"))

# temp =0;

# Two number swapping with using a third value
# temp=A
# A=B
# B=temp;

# print(A,B)

# Answer to the Question Number 8:

# A=int(input("Enter the first number:"))
# B=int(input("Enter the second number:"))

# Two number swapping without using a third value
# A=A+B
# B=A-B
# A=A-B

# print(A,B)

# Answer to the Question number 9:

# name=str(input("Enter the name:"))
# print("Welcome",name)

# Answer to the Question number 10:

# A=int(input("Enter the number1:"))
# B=int(input("Enter the number2:"))

# Sum=A+B
# Sub=A-B
# Multiple=A*B
# Divide=A/B

# print("Sum:",Sum,"\nSub:",Sub,"\nMultiple",Multiple,f"\nDivide:{Divide:.2f}")

# Answer to the Question number 11:
# length=int(input("Enter the length:"))
# breadth=int(input("Enter the breadth:"))

# perimeter_of_rectangle=2*(length+breadth)
# print("Perimeter of rectangle:",perimeter_of_rectangle)

# Answer to the Question number 12:
# side=int(input("Enter the length:"))
# perimeter_of_square=4*side
# area_of_square=side*side
# print("Perimeter of square:",perimeter_of_square,"\nArea of Square:",area_of_square)

# Answer to the Questionn number 13:
# side1=int(input("Enter the side1:"))
# side2=int(input("Enter the side2:"))
# side3=int(input("Enter the side3:"))
# semiperimeter_of_triangle=(side1+side2+side3)/2
# print("semiperimeter of triangle:",semiperimeter_of_triangle)

# Answer to the Question number 14:
# radius=int(input("Enter the length of circle:"))
# area_of_circle=3.14*(radius**2)
# print("Area of circle is",area_of_circle)

# Answer to the Question number 15:
# circumference=int(input("Enter the circumference:"))
# diameter=circumference/3.14;
# print(f"Diameter of Circumference is {diameter:.2f}")

# Answer to the Question number 16:
# side=int(input("Enter the length of Cube:"))

# lateral_surface_area=4*(side**2)
# total_surface_area=6*(side**2)

# print(f"lateral surface area is={lateral_surface_area} \nTotal surface is={total_surface_area}")


# Answer to the Question number 17:
# length=int(input("Enter the length of length:"))
# volume_of_cube=length**3
# print("Volume of cube is=",volume_of_cube)

# Answer to the Question number18:
# length=int(input("Enter the length of Cube:"))
# width=int(input("Enter the breadth of Cube:"))
# height=int(input("Enter the height of Cube:"))

# formula_for_lateral_surface_area_of_cuboid = 2 * height * (length + width)
# formula_for_Total_surface_area_of_cuboid  = 2 * (length * width + width * height + height * length)
# print(formula_for_lateral_surface_area_of_cuboid,formula_for_Total_surface_area_of_cuboid)


# Start Condition operator from 33:


# Answer to the question number 33(i):
# A=int(input("Enter the number1:"))
# B=int(input("Enter the number2:"))
# print((A//B)*B)

# Answer to the Question number 33(ii):
# A=int(input("Enter the number1:"))
# B=int(input("Enter the number2:"))

# if A>B:
#     print("A is greater than B")
# elif A==B:
#     print("A is equal to B")
# else:
#      print("A is greater than B")


# Answer to the question number 34:
# A=int(input("Enter the number1:"))
# B=int(input("Enter the number2:"))
# C=int(input("Enter the number3:"))

# A,B,C =map(int,input("Enter the number:").split())

# if A>B and A>C:
#     print(A,"is a greatest number")
# elif B>C:
#     print(B,"is a greatest number")
# else:
#     print(C,"is a greatest number")

# Answer to the question number 39

# A=int(input("Enter the number1:"))
# B=int(input("Enter the number2:"))

# if A==B:
#     print("Square")
# else:
#     print("Rectangle")

# SP,CP=map(int,input("Enter the selling and cost price:").split())

# if SP>CP:
#     print("profit of",SP-CP)

# elif SP==CP:
#     print("No profit,No loss")
# else:
#     print("loss of",CP-SP)

# Answer to the Question number 41:

# A,B,C,D=map(int,input().split())

# with method
# print(min(A,B,C,D))

# without method
# if(A<B and A<C and A<D):
#     print(A,"is a smallest number")
# elif(B<C and B<D):
#     print(B,"is a smallest number")
# elif(C<D):
#     print(C,"is a smallest number")
# else:
#     print(D,"is a smallest number")

# Answer to the question number 43:

# number=int(input("Enter the number: "))
# if(number%7==0):
#     print(number,"is divisible by 7")
# else:
#     print(number,"is not divisible by 7")

# Answr to the question number 44:
# number=int(input("Enter the number: "))
# if(number%2==0):
#     print("Even")
# else:
#     print("Odd")

# Answr to the question number 45:
# number=int(input("Enter the number: "))
# if(number%10==3):
#     print("last number divisible by 3")
# else:
#      print("last number not divisible by 3")


# Answr to the question number 46:
# Age=int(input("Enter the Age: "))

# if Age>=18:
#     print("Eligible for voting")
# else:
#     print("Not Eligible for voting")


# Answer to the question number 47

# number=int(input("Enter the number: "))
# if number%5==0:
#     print("Hello")
# else:
#     print("Bye")

# Answer to the question number 49

# number=int(input("Enter the number: "))

# count=0

# while (number>0):
#     count+=1
#     number=number//10

# print(count)

# Answer to the Question number 50:
# Age=int(input("Enter the Age: "))
# if(Age>=60):
#     print("Senior Citizen")
# else:
#     print("Not Senior Citizen")

# Answer to the Question number 51:
# Temperature=float(input("Enter the temperature: "))
# if(Temperature>=100):
#     print("YES")
# else:
#     print("NO")


# Answer to the question number 53:
# Quantity=int(input("Enter the Quantity: "))

# Price=Quantity*100

# if Price>1000:
#     Price=Price-Price*10/100
#     print(Price)
# else:
#     print(Price)

# Answer to the Question number 54:
# Salary=int(input("Enter the Salary:"))
# serviceYear=int(input("Enter the Year: "))

# if(serviceYear>5):
#     print("Bonus amount is",Salary*11/10)


# Answer to the Question no 276:
# N=int(input("Enter the number:"))
# num=0
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(num+j,end=" ")
#     print("\n")
#     num+=j
   

# Answer to the Question number 275 :

# number=int(input("Enter the number:"))
# count=0
# reverse=0
# rev=number

# for i in range(2,number+1):
#     if(number%2==0):
#         count+=1
#         print("It's not a prime number")
#         break
# if count==0:
#     while rev>0:
#        remain=rev%10
#        reverse=(reverse*10)+remain
#        rev=rev//10

#     for i in range(2,reverse+1):
#       if(reverse%2==0):
#         count+=1
#         break
#     if count==0:
#         print(number,"is a prime number and",reverse,"is also a prime number","SO it's a twisted prime number")
#     else:
#         print(number,"is not a twisted prime number")


# numbers = in


# Initialize variables to store the numbers
# number1 ,number2 , number3 =  map(int,input("Enter three numbers separated by spaces: "))

# if number1>number2 and number1>number3:
#   print(number1)
# elif number2>number3:
#   print(number2)
# else:
#   print(number3)




  



   




