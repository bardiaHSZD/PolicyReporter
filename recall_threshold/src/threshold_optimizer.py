import pandas as pd
from src.logger import logger
from src.utils import calculate_metrics, calculate_composite_score
from sklearn.metrics import roc_auc_score

class ThresholdOptimizer:
    def __init__(self, file_path):
        """
        Initialize the ThresholdOptimizer with a file path to the CSV data.
        Args:
            file_path (str): Path to the CSV file containing thresholds and metrics.
        """
        self.file_path = file_path

    def find_best_threshold(self, weights=None):
        """
        Finds the best threshold based on a composite score or individual metrics.

        Args:
            weights (dict): Weights for calculating composite score (optional).

        Returns:
            dict: Results containing the best threshold and all metrics.
        """
        best_threshold = None
        best_composite_score = float('-inf')
        results = []

        # Read the CSV file
        try:
            df = pd.read_csv(self.file_path)
            logger.info(f"Successfully read CSV file: {self.file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            return None
        except pd.errors.EmptyDataError:
            logger.error(f"Empty data file: {self.file_path}")
            return None
        except Exception as e:
            logger.error(f"Error reading the file: {e}")
            return None

        # Check if the DataFrame is empty
        if df.empty:
            logger.error("The DataFrame is empty. No data to process.")
            return None

        # Log DataFrame for debugging
        logger.info(f"DataFrame read from file:\n{df}")

        # Iterate through each threshold
        for index, row in df.iterrows():
            try:
                TP = row['TP']
                FP = row['FP']
                TN = row['TN']
                FN = row['FN']
                threshold = row['threshold']

                # Calculate precision, recall, F1 score, false positive rate (FPR), and TNR
                precision, recall, f1, fpr, tnr = calculate_metrics(TP, FP, TN, FN)

                # Log calculated values
                logger.info(f"Threshold: {threshold}, Precision: {precision}, Recall: {recall}, F1: {f1}")

                # Check recall condition
                if recall >= 0.9:
                    logger.info(f"Threshold {threshold} satisfies recall >= 0.9")

                    # Update best threshold if weights are not provided
                    if weights is None:
                        best_threshold = threshold

                # Calculate composite score if weights are provided
                if weights:
                    composite_score = calculate_composite_score(precision, recall, f1, fpr, weights)

                    # Update the best threshold based on composite score
                    if composite_score > best_composite_score:
                        best_composite_score = composite_score
                        best_threshold = threshold

                # Store the results for reporting
                results.append({
                    'threshold': threshold,
                    'precision': precision,
                    'recall': recall,
                    'f1': f1,
                    'fpr': fpr,
                    'tnr': tnr,
                    'composite_score': composite_score if weights else None
                })

            except KeyError as e:
                logger.error(f"Missing key in data: {e}")
                continue  # Skip the current row if there are missing keys

        # Check if any valid threshold was found
        if best_threshold is None:
            logger.warning("No valid threshold found that meets the criteria.")
            return None

        logger.info(f"Best threshold selected: {best_threshold}")
        return {
            "best_threshold": best_threshold,
            "results": results
        }


def run_optimizer(file_path, weights=None):
    """
    Helper function to run the optimizer.
    
    Args:
        file_path (str): Path to the CSV file.
        weights (dict): Weights for composite score calculation (optional).
    
    Returns:
        dict: Best threshold and metrics.
    """
    optimizer = ThresholdOptimizer(file_path)
    result = optimizer.find_best_threshold(weights=weights)
    
    if result is None:
        logger.error("No valid threshold found.")
    else:
        best_threshold = result["best_threshold"]
        logger.info(f"Best threshold selected: {best_threshold}")
    
    return result
