# Written and tested in Python 2.7.10

# Get the integer input from the user.
entered_num = input('Enter an integer number please : ')

# Recursively calculates the number of 1s in the binary represenation of an integer.
def num_of_ones_in_bin(num):
    if not num:
        return 0
    if num < 0:
        num = 2**64 - num #64 bit system assumed
    return (num & 1) + num_of_ones_in_bin(num>>1)

# Print the result on the console.
print 'Number of 1\'s in the binary representation of', entered_num,': ', num_of_ones_in_bin(entered_num)

