""""""
"""
Example 1:
number = int(input('Enter number:'))
if number % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')
output:
Enter number100
Even Number
Enter number89
Odd Number
==============================================================================
Example 2
height = float(input('Enter Height in inches'))
if height >= 60:
    print('Selected')
else:
    print('Rejected')
OUTPUT:
Enter Height in inches67
Selected
Enter Height in inches49
Rejected
================================================================
Example 3:
marks = float(input ('Enter percentage'))
if marks >= 75:
    print('Excellent!! You got Distinction')
elif marks >= 60 and marks <=74:
    print('Nice-- You got First class')
elif marks >= 50 and marks <=59:
    print('Good --You got Second Class')
elif marks >=35 and marks <=49:
    print('Pass Class')
else:
    print('You are Fail')
OUTPUT:
Enter percentage76
Excellent You got Distinction
Enter percentage74
Nice-- You got First class
Enter percentage55
Good --You got Second Class
Enter percentage45
Pass Class
Enter percentage34
You are Fail
=======================================================================================
Example 4:
stream = input('Select your interest from below\n1. Science\n2. Commerce\n3. Arts')
if stream == 'Science':
    print('You must secure more than 80 % in tenth to get admission ')
elif stream == 'Commerce':
    print('You must secure more than 65 % in tenth to get admission ')
elif stream == 'Arts':
    print('You must secure more than 40 % in tenth to get admission ')
else:
    print('Choose correctly from given list ')
OUTPUT:
Select your interest from below
1. Science
2. Commerce
3. ArtsScience
You must secure more than 80 % in tenth to get admission
Select your interest from below
1. Science
2. Commerce
3. ArtsCommerce
You must secure more than 65 % in tenth to get admission
Select your interest from below
1. Science
2. Commerce
3. ArtsArts
You must secure more than 40 % in tenth to get admission
Select your interest from below
1. Science
2. Commerce
3. Artsarts
Choose correctly from given list
====================================================================================
Example 5:
weather = input('Enter weather conditions')
if weather == 'Sunny':
    print('Please use Hat and Goggles in bright sunny day')
elif weather == 'raining':
    print('Please use raincoats or umbrellas to avoid getting wet ')
elif weather == 'cold and dry':
    print('Please wear sweaters to avoid getting cold')
else:
    print('Wrong entry')
OUTPUT:
Enter weather conditionsraining
Please use raincoats or umbrellas to avoid getting wet
Enter weather conditionsSunny
Please use Hat and Goggles in bright sunny day
Enter weather conditionscold
Wrong entry
Enter weather conditionscold and dry
Please wear sweaters to avoid getting cold
=====================================================================================
Example 6:
num = int(input('Enter Number'))
if num > 0:
    print('It is a Positive number')
elif num < 0:
    print('It\'s a Negative Number')
else:
    print('ZERO')
OUTPUT:
Enter Number4
It is a Positive number
Enter Number-5
It's a Negative Number
Enter Number0
ZERO
===========================================================================
Example 7:
x = int(input('enter x'))
y = int(input('enter y'))
z = int(input('enter z'))
if x > y and x > z:
    print('x is greatest')
elif y > z:
    print('y is greatest')
else:
    print('z is greatest')
OUTPUT:
enter x77
enter y88
enter z99
z is greatest
enter x99
enter y88
enter z77
x is greatest
enter x88
enter y99
enter z77
y is greatest
=============================================================================
Example 8:
print('Pizza n more\nCelebration Time...')
print('Please select\n1.Veg pizza\n2.Non veg pizza')
category1 = input('Enter your choice:')
if category1 == 'Veg pizza':
    print('Please select\n1. Corn Cheese Pizza\n2. Paneer Paratha Pizza')
    category2 = input('Enter your choice:')
    if category2 == 'Corn Cheese Pizza':
        print ('Price is Rs.179')
        qty = int(input('Enter quantity:'))
        bill = 179*qty
        print('Final Bill is Rs.',bill,'/-')
        order1 = int(input('Press 1 to confirm order'))
        if order1 == 1:
            print('Thank you for your order !!!')
        else:
            print('please enter 1 properly')
    elif category2 == 'Paneer Paratha Pizza':
        print('Price is Rs.209')
        qty1 = int(input('Enter quantity:'))
        bill1 = 209 * qty1
        print('Final Bill is Rs.', bill1,'/-')
        order2 = int(input('Press 1 to confirm order'))
        if order2 == 1:
            print('Thank you for your order !!!')
        else:
            print('please enter 1 properly')
    else:
        print ('Enter correct choice')
elif category1 == 'Non veg pizza':
    print('Please select\n1.Chicken paratha pizza\n2.Pepper Barbeque chicken')
    category3 = input('Enter your choice:')
    if category3 == 'Chicken paratha pizza':
        print('Price is Rs.249')
        qty2 = int(input('Enter quantity:'))
        bill2 = 249 * qty2
        print('Final Bill is Rs.', bill2, '/-')
        order3 = int(input('Press 1 to confirm order'))
        if order3 == 1:
            print('Thank you for your order !!!')
        else:
            print('please enter 1 properly')
    elif category3 == 'Pepper Barbeque chicken':
        print('Price is Rs.449')
        qty3 = int(input('Enter quantity:'))
        bill3 = 449 * qty3
        print('Final Bill is Rs.', bill3, '/-')
        order4 = int(input('Press 1 to confirm order'))
        if order4 == 1:
            print('Thank you for your order !!!')
        else:
            print('please enter 1 properly')
    else:
        print('Enter correct choice')
else:
    print('Please Enter properly from list')
print('Hopefully you are satisfied with our service\nThank you\nVisit again!!!')
******************************************************************************************************OUTPUT******
Pizza n more
Celebration Time...
Please select
1.Veg pizza
2.Non veg pizza
Enter your choice:Non veg pizza
Please select
1.Chicken paratha pizza
2.Pepper Barbeque chicken
Enter your choice:Pepper Barbeque chicken
Price is Rs.449
Enter quantity:4
Final Bill is Rs. 1796 /-
Press 1 to confirm order1
Thank you for your order !!!
Hopefully you are satisfied with our service
Thank you
Visit again!!!
===============================================================================
Example 9:
print('Example of if else loop in python')
age = int(input('enter your age'))
if age >= 18:
    print ('You are eligible for voting')
else:
    print('You are not eligible for voting')
OUTPUT:
Example of if else loop in python
enter your age20
You are eligible for voting
Example of if else loop in python
enter your age10
You are not eligible for voting
==========================================================================
Example 10:
package = ['US', 'UK','Japan', 'France', 'South Africa', 'Indonesia', 'Singapore', 'Turkey']
destination = input('Enter your choice:')
if destination in package:
    print('Your choice of',destination,'is available\nBook package')
else:
    print('The destination',destination,' is not available currently')
OUTPUT:
Enter your choice:UK
Your choice of UK is available
Book package
Enter your choice:Mumbai
The destination Mumbai  is not available currently
=========================================================================
Example 11:
year = int(input('Enter Year'))
if year %4 == 0:
    print (year,'is a Leap Year')
else:
    print(year,'is not a Leap Year')
OUTPUT:
  Enter Year2022
2022 is not a Leap Year
Enter Year2020
2020 is a Leap Year
`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
"""