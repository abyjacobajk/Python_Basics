# Python program to print Multiplication table
n = int(input("Input a number: "))
l= int(input("enter the limit"))
# use for loop to iterate 10 times
for i in range(1,l):
   print(n,'x',i,'=',n*i)
