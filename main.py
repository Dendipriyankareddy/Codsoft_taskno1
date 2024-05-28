number1=input('Enter the num:\n')
num1=int(number1)
sign=input('Enter the sign:\n')
number2=input('Enter the number:\n')
num2=int(number2)
if sign == '+':
    print('Your result is' +str(num1+num2))
elif sign == '-':
    print('Your result is' +str(num1-num2))
elif sign == '*':
    print('Your result is' +str(num1*num2))    
elif sign == '/':
    print('Your result is' +str(num1/num2))
else:
    print('please enter +,-,/,*')
    