# tests/test_fsm.py
import unittest
from main import compute_mod_three

class TestModThreeFSM(unittest.TestCase):
    def setUp(self):
        # Initialize counters for passed valid and invalid tests
        self.passed_valid_tests = 0
        self.passed_invalid_tests = 0

    def test_valid_inputs(self):
        test_cases = {
            '1101': 1,
            '1110': 2,
            '1111': 0,
            '110': 0,
            '1010': 1,
            '': 0,  # Empty input
            '0': 0,
            '1': 1,
            '1001': 0,  # Expected output should be 0
        }
        for binary_string, expected in test_cases.items():
            with self.subTest(binary_string=binary_string):
                self.assertEqual(compute_mod_three(binary_string), expected)
                self.passed_valid_tests += 1  # Increment counter for valid tests

    def test_invalid_inputs(self):
        invalid_inputs = ['1102', 'abc', '10a1', '2', '01b01']
        for binary_string in invalid_inputs:
            with self.subTest(binary_string=binary_string):
                self.assertIsNone(compute_mod_three(binary_string))
                self.passed_invalid_tests += 1  # Increment counter for invalid tests

    def tearDown(self):
        """Print the number of passed valid and invalid tests at the end."""
        total_passed_tests = self.passed_valid_tests + self.passed_invalid_tests
        print(f"\nTotal number of valid input tests passed: {self.passed_valid_tests}")
        print(f"Total number of invalid input tests passed: {self.passed_invalid_tests}")
        print(f"Total number of passed tests: {total_passed_tests}")

if __name__ == '__main__':
    unittest.main()
