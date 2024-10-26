import itertools

# Define the digits and the length of each combination
digits = '0123456789'
length = 10

with open('10_digit_wordlist.txt', 'w') as f:
    for combination in itertools.product(digits, repeat=length):
        f.write(''.join(combination) + '\n')
