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

# Define a function to convert Morse code to English text
def morse_it2(string, MORSECODE2):
    # Converts Morse code to English text.

    # Args:
    # - string (str): The input Morse code.
    # - MORSECODE2 (dict): Dictionary mapping Morse code to English letters.
    #
    # Returns:
    # - str: The converted English text.

    if not string:
        raise MorseCodeError("Input cannot be empty. Please enter Morse code for conversion.")
    
    morse_words = string.split('/')  # Split Morse code by '/'
    result = ""
    for morse_word in morse_words:
        morse_letters = morse_word.strip().split()  # Split Morse word into Morse letters
        for letter in morse_letters:
            if letter in MORSECODE2:
                result += MORSECODE2[letter]  # Append English letter for the Morse code
            else:
                raise MorseCodeError(f"The '{letter}' key doesn't exist in the dictionary")  # Raise an error if the Morse code is not recognized
        result += " "  # Add space between words
    return result.strip()  # Remove  spaces

