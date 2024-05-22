# n = int(input("Enter a number: "))
# count=0
# sum=0

# while(n>0):
#     remain=n%10
#     sum+=remain*(2**count) 
#     n=n//10
#     count+=1 

# print(sum)

# n=int(input("enter a number of terms: "))

# a=0
# b=1

# for i in range (n):
#     sum=a+b
#     print(a)
#     a=b
#     b=sum


# n=int(input("enter a number of terms: "))

# a=0
# b=1
# i=1
# while (i<=n):
#     sum=a+b
#     print(a)
#     a=b
#     b=sum
#     i+=1


#  by default wrong answer 

# n=int(input("enter a number of terms: "))

# rev=0
# k=n

# for i in range (k):
#     remain=n%10
#     rev=rev*10+remain # yha multiply by 10 ke karan 0 bar bar repeat ho rha h 
#     n=n//10
# print(rev)

# count=0
# sum=0
# n=int(input("enter a number:"))
# num=n
# number=n
# while (n>0):
#     count+=1
#     n=n//10
# while(num>0):
#     remain=num%10
#     sum+=remain**count
#     num=num//10

# if(sum==number):
#     print("It's a armstrong number")
# else:
#     print("It's not a armstrong number")
    

# Star pattern 1

# *
# **
# ***
# ****
# *****
# ******


# number_of_raws=int(input("Enter a number of raw:  "))
# for i in range(number_of_raws):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# Star Pattern 2:

#      *
#     **
#    ***
#   ****
#  *****
# ******

# number_of_raws=int(input("Enter a number of raw:  "))
# for i in range(1,number_of_raws+1):
#     print(" "*(number_of_raws-i), end="")
#     print("*"*i)

# number_of_raws=int(input("Enter a number of raw:  "))
# for i in range(number_of_raws):
#     for j in range(number_of_raws-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()


# Star pattern 3

# * 
#  *
#   *
#    *
#     *

# n =int(input("Enter a number of raws: "))
# for i in range(n):
#     print(" "*i,end="")
#     print("*",end="")
#     print()

# Star pattern 4

#     *
#    ***
#   *****
#  *******
# *********

# n=int(input("Enter the number of raws: "))
# for i in range(n):
#     for j in range(1,n-i):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()


# n=int(input("Enter the number of raws: "))
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1))
 
# n = int(input("Enter a number: "))  # Prompting user to enter the number
# rev = 0  # Initializing the reversed number to 0

# # Calculate the number of digits in the number
# num_digits = len(str(n))

# for i in range(num_digits):
#     remain = n % 10  # Getting the last digit of n
#     rev = rev * 10 + remain  # Adding the last digit to the reversed number
#     n = n // 10  # Removing the last digit from n

# print(rev)  # Printing the reversed number



# n=int(input("enter a number of terms: "))

# rev=0
# # k=len(str(n))

# for i in range (len(str(n))):
#     remain=n%10
#     rev=rev*10+remain   #yha multiply by 10 ke karan 0 bar bar repeat ho rha h 
#     n=n//10
# print(rev)
