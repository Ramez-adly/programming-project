from moursecode import morse_it,morse_it2,MORSECODE,MORSECODE2,MorseCodeError
import unittest
# Define a test class that's from 'unittest.TestCase'
class TestMorseCodeConversion(unittest.TestCase):
    
    # Define a test method for converting English to Morse code
    def test_english_to_morse(self):
        # Define the expected Morse code result for the input 'HELLO WORLD'
        expected_result = '.- .... -- . -.. / .. ... / .... .- .--. .--. -.--'
        # Call the 'morse_it' function to convert 'HELLO WORLD' to Morse code
        actual_result = morse_it('AHMED IS HAPPY', MORSECODE)
        # Assert that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")

# Define a test method for converting Morse code to English
    def test_morse_to_english(self):
        # Define the expected English result for the input Morse code
        expected_result = 'AHMED IS HAPPY' 
        # Call the 'morse_it2' function to convert the Morse code to English
        actual_result = morse_it2('.- .... -- . -.. / .. ... / .... .- .--. .--. -.--', MORSECODE2)
        # check that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\Actual: {actual_result}")

# to handle invalid english  characters
    def test_invalid_english_character(self):
        with self.assertRaises(MorseCodeError):
            morse_it('#Invalid#', MORSECODE)

# to handle invalid Morse code
    def test_invalid_morse_code(self):
        with self.assertRaises(MorseCodeError):
            morse_it2('.... . .-.. .-.. --- / .-- --- .-. .-.. -.. #Invalid#', MORSECODE2)

# to handle empty input
    def test_empty_input(self):
        # Test handling empty input
        with self.assertRaises(MorseCodeError):
            morse_it('', MORSECODE)

    # To handle empty Morse code input
    def test_empty_morse_code_input(self):
        # Test handling empty Morse code input
        with self.assertRaises(MorseCodeError):
            morse_it2('', MORSECODE2)

if __name__ == '__main__':
    unittest.main()