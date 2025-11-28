
#
#if else statement
#check number is positive or negative

num = input('Enter a number')

num= int(num)

if type(num) is not int :
    print("Enterd number is not integer")   
elif num > 0 :
    print("Entered number is Positive")    
elif  num < 0 :
    print('Entered number is negative')
else :
    print("Entered number is zero")   




# try except
name= input ('Enter your name')

try :
    name = int(name)
    print('Enterd name is not string')
except ValueError:
    print('Enterd name is string')