# test_fsm.py

import unittest
from main import compute_mod_three

class TestModThreeFSM(unittest.TestCase):
    total_tests_run = 0  # Class-level variable to track the number of sub-tests

    def test_valid_inputs(self):
        test_cases = {
            '1101': 1,
            '1110': 2,
            '1111': 0,
            '110': 0,
            '1010': 1,
            '': 0,       # Empty input
            '0': 0,
            '1': 1,
            '1001': 0,  # Expected output is 0
        }
        for binary_string, expected in test_cases.items():
            with self.subTest(binary_string=binary_string):
                self.assertEqual(compute_mod_three(binary_string), expected)
                TestModThreeFSM.total_tests_run += 1  # Increment the test count for each sub-test

    def test_invalid_inputs(self):
        invalid_inputs = ['1102', 'abc', '10a1', '2', '01b01']
        for binary_string in invalid_inputs:
            with self.subTest(binary_string=binary_string):
                self.assertIsNone(compute_mod_three(binary_string))
                TestModThreeFSM.total_tests_run += 1  # Increment the test count for each sub-test

    @classmethod
    def tearDownClass(cls):
        """ This will run after all the tests are finished. """
        print(f"\nTotal number of sub-tests run: {cls.total_tests_run}")

if __name__ == '__main__':
    unittest.main()
