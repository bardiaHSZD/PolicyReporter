import unittest
import pandas as pd
from src.threshold_optimizer import ThresholdOptimizer
import os

class TestThresholdOptimizer(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV file for testing
        self.test_file = "data/test_classification_thresholds.csv"
        data = {
            'threshold': [0.1, 0.2, 0.3, 0.4, 0.5],
            'TP': [90, 85, 83, 92, 91],
            'TN': [80, 85, 86, 75, 76],
            'FP': [10, 5, 4, 15, 14],
            'FN': [5, 10, 12, 3, 4]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_file, index=False)

    def test_find_best_threshold(self):
        optimizer = ThresholdOptimizer(self.test_file)
        results = optimizer.find_best_threshold()

        # Check that results is not None
        self.assertIsNotNone(results, "The optimizer returned None instead of results.")

        # Assert best threshold is found correctly
        if results:
            self.assertEqual(results['best_threshold'], 0.5)

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
