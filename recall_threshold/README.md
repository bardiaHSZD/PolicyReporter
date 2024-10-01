
# Threshold Optimizer with GPU Acceleration

## Overview

This project demonstrates how to optimize threshold selection for a binary classification model based on recall values, using GPU acceleration for large datasets. The recall is computed for each threshold, and the best threshold that yields a recall greater than or equal to 0.9 is selected.

## Requirements

- Python 3.8 or higher
- CUDA-capable GPU (optional, for GPU acceleration)
- Numba (for GPU acceleration)
- pandas (for data manipulation)
- loguru (for logging)

## Installation

1. **Clone the Repository and Change the Directory to 'threshold_optimizer'**:
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

    On **Linux/Mac**:
    ```bash
    source threshold_env/bin/activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install pandas loguru numba
    ```

## CUDA Installation (Optional, if using GPU Acceleration)

If you want to leverage GPU acceleration, you will need to install the CUDA Toolkit and cuDNN:

1. **Install CUDA Toolkit**: Download from [here](https://developer.nvidia.com/cuda-downloads).
2. **Install cuDNN**: Download from [here](https://developer.nvidia.com/cudnn).

## Data

The input data for this project is stored in a CSV file located in the `data/` folder. The CSV file should contain the following columns:

- `threshold`: Confidence score threshold values (e.g., 0.1, 0.2, ..., 0.9).
- `TP`: True positives for each threshold.
- `TN`: True negatives for each threshold.
- `FP`: False positives for each threshold.
- `FN`: False negatives for each threshold.

Download the sample CSV: [classification_thresholds.csv](./data/classification_thresholds.csv)

## How to Run the Code

1. Ensure the CSV file is located in the `data/` folder. If you are using the sample CSV, ensure it's located at `data/large_classification_thresholds.csv`.
2. Run the following Python script to compute the best threshold based on recall values:

    ```bash
    python src/threshold_optimizer.py
    ```

3. The output will log the best threshold with a recall greater than or equal to 0.9.

## Unit Tests

Unit tests are provided to validate the recall computation and threshold selection process. You can run the tests using the following command:

```bash
python -m unittest discover tests
```

This will run all the unit tests in the `tests/` folder.

## File Structure

```
threshold_optimizer/
├── data/
│   └── large_classification_thresholds.csv  # The sample CSV file
├── src/
│   ├── __init__.py
│   ├── threshold_optimizer.py  # Main code for threshold optimization
│   └── logger.py  # Logging configuration
├── tests/
│   └── test_threshold_optimizer.py  # Unit tests
├── README.md  # This file
└── requirements.txt  # Python dependencies
```

## License

MIT License
