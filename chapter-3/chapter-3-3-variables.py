lucky_number = 8  # This is a lucky number

my_name = 'Raymond Gao'  # This is my name

float_type_test_01 = 10.01
float_type_test_02 = 100.02

imaginary_test_01 = 10 + 30j

print('The type of lucky_number is', type(lucky_number))
print('The type of my_name is', type(my_name))
print('The type of float_type_test_01 is', type(float_type_test_01))
print('The sum of float variables is', float_type_test_01 + float_type_test_02)
print('Round of the sum of float variables is', round(float_type_test_01 + float_type_test_02, 3))
print('The real part of imaginary_test_01 is', imaginary_test_01.real)
print('The imaginary part of imaginary_test_01 is', imaginary_test_01.imag)

print(my_name, ' lucky name is', lucky_number)

# Python could update the type of variable dynamically

lucky_number = 'Raymond Gao'  # This is a lucky number of String type
print('The latest type of lucky_number is', type(lucky_number))

number1=number2=100

print('number1 is', number1, 'number2 is', number2, sep='##')

NUMBER_CONST = 1000
