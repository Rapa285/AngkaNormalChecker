from collections import Counter

def champernowne_constant(n):
    """
    Generate the first n digits of Champernowne's constant in base 10.
    
    :param n: Number of digits to generate.
    :return: A string representing the first n digits of Champernowne's constant.
    """
    constant = ''
    i = 1
    while len(constant) < n:
        constant += str(i)
        i += 1
    return constant[:n]

def digit_frequencies(sequence):
    """
    Calculate the frequency of each digit in the given sequence.
    
    :param sequence: A string representing the sequence of digits.
    :return: A dictionary with digits as keys and their frequencies as values.
    """
    counter = Counter(sequence)
    total_digits = len(sequence)
    frequencies = {digit: (count / total_digits) * 100 for digit, count in counter.items()}
    return frequencies

# Generate the first 999,999 digits of Champernowne's constant
num_digits = 999999
champernowne_seq = champernowne_constant(num_digits)

# Calculate the frequencies
frequencies = digit_frequencies(champernowne_seq)

# Display the frequencies
print("Digit frequencies in the first 999,999 digits of Champernowne's constant:")
for digit in sorted(frequencies):
    print(f"Digit {digit}: {frequencies[digit]:.15f}%")
