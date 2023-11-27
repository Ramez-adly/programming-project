class MorseCodeError(Exception):            #custom error for errors
    pass
# Define the Morse code mappings for English letters
MORSECODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

# Define the Morse code mappings for Morse to English conversion
MORSECODE2 = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

# Define a function to convert English text to Morse code
def morse_it(string, MORSECODE):
    
    # Converts English text to Morse code.

    # Args:n
    # - string (str): The input English text.
    # - MORSECODE (dict): Dictionary mapping English letters to Morse code.

    # Returns:
    # - str: The converted Morse code.
    
    if not string:
        raise MorseCodeError("Input cannot be empty. Please enter text for conversion.")
    
    string = string.upper()  # Convert input to uppercase
    result = []
    for letter in string:
        if letter in MORSECODE:
            result.append(MORSECODE[letter])  # Append Morse code for the letter
        elif letter == " ":
            result.append("/")  # Append space for space in the input
        else:
            raise MorseCodeError(f"The '{letter}' key doesn't exist in the dictionary")  # Raise an error if the letter is not recognized
    return ' '.join(result)  # Join Morse code representations with spaces between letters
