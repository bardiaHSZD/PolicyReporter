
# Threshold Optimizer

## Overview

This project implements a threshold optimization system for a binary classification model. It calculates various metrics (e.g., Precision, Recall, F1 Score, False Positive Rate) across different thresholds and selects the best threshold. The best threshold can be determined based on a **composite score** (weighted metrics), or you can prioritize individual metrics such as F1 Score or Recall. 

The solution is designed to handle large datasets efficiently and includes optional GPU acceleration (though not required for basic functionality).

---

## Strategy to Reach the Solution

The objective of this project is to find the best threshold for a binary classification task by calculating performance metrics for each threshold and selecting the optimal one based on user-defined criteria. Here’s the strategy followed to reach the solution:

### 1. **Understanding the Problem**

The task involves **threshold optimization** for binary classification. Given a dataset with true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN) at various thresholds, the goal is to compute metrics like **recall**, **precision**, and **F1 score**. The challenge is to choose the best threshold that maximizes the desired metrics.

### 2. **Metrics Calculation**

We compute several key metrics:
- **Precision**: Proportion of true positives among all predicted positives.
- **Recall**: Proportion of actual positives that are correctly identified.
- **F1 Score**: Harmonic mean of precision and recall, which balances these two metrics.
- **False Positive Rate (FPR)**: The proportion of negatives that were incorrectly classified as positives.
- **True Negative Rate (TNR or Specificity)**: Proportion of negatives that were correctly classified.

These metrics are calculated for each threshold in the dataset.

### 3. **Composite Score (Optional)**

Users can define a **composite score** by assigning weights to each metric (precision, recall, F1 score, etc.). This allows for custom optimization based on the user's preferences. For example, if minimizing false positives is more important, you can assign a higher weight to **FPR** in the composite score calculation.

### 4. **Edge Cases Consideration**

We considered several edge cases:
- Empty datasets or files with missing values are handled with appropriate error logging.
- If multiple thresholds yield the same performance, the solution can select based on secondary metrics like precision.
- Thresholds where no predictions are made (e.g., zero TP + FN or TP + FP) are handled to avoid division errors.

### 5. **Error Handling and Logging**

The project uses **loguru** for logging, ensuring clear logs for:
- Missing or corrupt data files.
- Errors during metric computation (such as division by zero).
- Outputting the selected best threshold and associated metrics.

### 6. **Extensibility**

The code is modular and designed to be easily extensible. New metrics can be added as needed, and the optimizer can be adjusted to work with different classification tasks or evaluation metrics.

---

## Requirements

- Python 3.8 or higher
- pandas (for data manipulation)
- loguru (for logging)
- scikit-learn (for ROC-AUC computation)

---

## Installation

1. **Clone the Repository** and Change Directory:
    ```bash
    cd threshold_optimizer
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv threshold_env
    ```

3. **Activate the Virtual Environment**:

    On **Windows**:
    ```bash
    threshold_env\Scripts\activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Data

The input data for this project is stored in a CSV file located in the `data/` folder. The CSV file should contain the following columns:

- `threshold`: Confidence score threshold values (e.g., 0.1, 0.2, ..., 0.9).
- `TP`: True positives for each threshold.
- `TN`: True negatives for each threshold.
- `FP`: False positives for each threshold.
- `FN`: False negatives for each threshold.

A sample CSV file is included: `data/large_classification_thresholds.csv`.

---

## How to Run the Code

1. Ensure the CSV file is located in the `data/` folder.
2. Run the following Python script to compute the best threshold based on selected metrics:

    ```bash
    python src/threshold_optimizer.py
    ```

3. By default, the code will compute metrics for all thresholds and return the best threshold based on the **composite score** or the highest **F1 score**. The output will log the best threshold, precision, recall, F1 score, and more.

---

## Unit Tests

Unit tests are provided to validate the metric calculations and threshold selection. Run the tests using:

```bash
python -m unittest discover tests
```

---

## File Structure

```
threshold_optimizer/
├── data/
│   └── large_classification_thresholds.csv  # The sample CSV file
├── src/
│   ├── __init__.py
│   ├── threshold_optimizer.py  # Main code for threshold optimization
│   ├── logger.py  # Logging configuration
│   └── utils.py  # Helper functions for metric calculation
├── tests/
│   └── test_threshold_optimizer.py  # Unit tests
├── README.md  # This file
└── requirements.txt  # Python dependencies
```

---

## License

MIT License
