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
