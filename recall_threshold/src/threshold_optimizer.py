import os
import pandas as pd
from numba import cuda
import numpy as np
from loguru import logger

class ThresholdOptimizer:
    """
    Class to find the best threshold that yields a recall >= 0.9, using GPU for recall calculation.
    """

    def __init__(self, file_path):
        """
        Initializes the ThresholdOptimizer with the given CSV file path.
        """
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")

    @staticmethod
    @cuda.jit
    def calculate_recall_on_gpu(TP, FN, recall):
        """
        CUDA kernel to calculate recall for arrays of TP and FN.
        
        :param TP: Array of True Positives.
        :param FN: Array of False Negatives.
        :param recall: Output array for recall values.
        """
        idx = cuda.grid(1)  # Get the global index for the current thread
        if idx < TP.size:
            if (TP[idx] + FN[idx]) > 0:
                recall[idx] = TP[idx] / (TP[idx] + FN[idx])
            else:
                recall[idx] = 0  # Handle division by zero

    def find_best_threshold(self):
        """
        Finds the best threshold with recall >= 0.9.

        :return: Best threshold value or None if not found.
        """
        best_threshold = None
        best_recall = 0

        chunk_size = 100000  # Adjust based on available memory

        try:
            reader = pd.read_csv(self.file_path, chunksize=chunk_size)
        except Exception as e:
            logger.error(f"Error reading CSV file: {e}")
            raise

        for chunk in reader:
            TP = chunk['TP'].values.astype(np.float32)
            FN = chunk['FN'].values.astype(np.float32)
            recall = np.zeros_like(TP, dtype=np.float32)

            # Move arrays to the GPU
            TP_device = cuda.to_device(TP)
            FN_device = cuda.to_device(FN)
            recall_device = cuda.to_device(recall)

            # Calculate recall on the GPU
            threads_per_block = 128
            blocks_per_grid = (TP.size + (threads_per_block - 1)) // threads_per_block
            self.calculate_recall_on_gpu[blocks_per_grid, threads_per_block](TP_device, FN_device, recall_device)

            # Copy the result back to the host
            recall_device.copy_to_host(recall)

            # Add recall values back to the chunk dataframe
            chunk['recall'] = recall

            # Filter rows where recall is >= 0.9
            valid_recall_rows = chunk[chunk['recall'] >= 0.9]

            if not valid_recall_rows.empty:
                max_recall_row = valid_recall_rows.loc[valid_recall_rows['recall'].idxmax()]
                current_recall = max_recall_row['recall']

                if current_recall > best_recall:
                    best_threshold = max_recall_row['threshold']
                    best_recall = current_recall
                    logger.info(f"New best threshold found: {best_threshold} with recall {best_recall}")

        if best_threshold is not None:
            logger.info(f"Best threshold with recall >= 0.9 is: {best_threshold}")
        else:
            logger.warning("No threshold found with recall >= 0.9.")

        return best_threshold
