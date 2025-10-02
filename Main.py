################Program 1##################
def backwards(value):
    length = len(value)
    while length > 0:  # Iterate until all characters are printed in reverse order
        print(value[length - 1], end='')  # Print characters in reverse without newlines
        length -= 1  # Decrease length to move backwards through the string
    print()  # Add a newline after the reversed string is printed

################Program 2##################
def backwards1(value):
    length = len(value)  # Get the length of the input string
    result = ""  # Initialize an empty string to store the reversed result
    for i in range(length - 1, -1, -1):  # Loop from the last character to the first
        result += value[i]  # Append each character in reverse order
        if i % 2 == 1:  # If the character index is odd, append a '*'
            result += '*'
    return result  # Return the final modified string

################Program 3##################
def exponent(base, power):
    total = base ** power  # Calculate base raised to the power (exponentiation)
    
    if base < 1 or base > 10:  # Check if base is out of the allowed range (1-10)
        return 'Invalid base entered'  # Return an error message for invalid base value
    
    if power < 1 or power > 5:  # Check if power is out of the allowed range (1-5)
        return 'Invalid power entered'  # Return an error message for invalid power value
    
    else:
        return total  # Return the calculated result
