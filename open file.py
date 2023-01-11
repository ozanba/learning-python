# fil = open('mail.txt')
# word = 'gmail'

# for line in fil:
#     if  word in line:
#         print(line)
        


    
# Open the file and read the integer
with open('numbers.txt') as f:
    number1 = int(f.read().strip())

# Get the second integer from the user
number2 = int(input('Enter an integer: '))

with open('new-number.txt', 'w') as f:
    f.write(str(number2))


# Add the two integers
sum = number1 + number2

# Open the file in write mode and write the sum to it
with open('numbers.txt', 'w') as f:
    f.write(str(sum))


