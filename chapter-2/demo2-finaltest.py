fileFinal = open('../test.txt', 'w')  # Open file for writing
print('Live is short, you need Python', file=fileFinal)  # Print to file
fileFinal.close()  # Close file

name = input('Please input your name: ')
age = input('Please input your age: ')
description = input('Please input your description: ')

print ('My name is ' + name)
print ('I am ' + age + ' years old')
print('I am ' + description)
