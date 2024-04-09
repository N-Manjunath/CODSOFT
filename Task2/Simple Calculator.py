# select an operation to perform
# 1- Addition
# 2- Subtraction
# 3- Multiplication
# 4- Division
num1=int(input('enter the first number :'))
num2=int(input('enter the second number :'))
operation=input('enter the operation to be performed:')
# checking of operation
if operation=='+':
    r1=num1+num2
    print('the result is :',r1)
elif operation=='-':
     r2=num1-num2
     print('the result is :',r2)
elif operation=='*':
     r3=num1*num2
     print('the result is :',r3)
elif operation=='/':
     r4=num1//num2
     print('the result is :',r4)
else:
    print('enter a valid operation')
