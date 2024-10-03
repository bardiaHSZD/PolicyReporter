
# PolicyReporter

This repository contains two distinct Python projects: 

1. **Finite State Machine (FSM) for Modulo Three Calculation**
2. **Threshold Optimizer for Binary Classification**

Both projects aim to solve specific computational problems through modular, testable code structures and provide detailed logging and user interaction through command-line interfaces.

---

## 1. Finite State Machine (FSM) for Modulo Three Calculation

### Overview
This project implements a generic Finite State Machine (FSM) class that solves the modulo three problem for binary numbers. It processes a binary string and computes the remainder when the binary number is divided by three.

### Features
- **Generic FSM Class**: Can be adapted for any FSM problem.
- **Modulo Three Calculation**: Specific setup for calculating modulo three.
- **CLI Interaction**: Allows users to input binary numbers via the command line.
- **Logging**: State transitions are logged, with color-coded output for better readability using `colorlog`.
- **Unit Tests**: Covers valid and invalid inputs.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/bardiaHSZD/PolicyReporter
   cd finite_state_machine
   ```
2. Install dependencies:
   ```bash
   pip install colorlog
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Run the unit tests:
   ```bash
   python -m unittest discover tests
   ```

### Folder Structure
```
finite_state_machine/
├── logs/
├── src/
├── tests/
└── main.py
```

For more details, check the [`finite_state_machine/README.md`](finite_state_machine/README.md).

---

## 2. Threshold Optimizer for Binary Classification

### Overview
This project implements a threshold optimizer for binary classification models. It computes performance metrics like precision, recall, F1 score, and false positive rate for different thresholds and selects the best one based on user-defined criteria or a composite score.

### Features
- **Metrics Calculation**: Computes precision, recall, F1 score, and more across thresholds.
- **Composite Score**: Users can define a composite score to prioritize specific metrics.
- **Logging**: Uses `loguru` for clear and structured logging.
- **Extensible Code**: Easily customizable for different metrics or classification tasks.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/bardiaHSZD/PolicyReporter
   cd recall_threshold
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the optimizer:
   ```bash
   python main.py --file_path data/classification_thresholds.csv
   ```

4. Run unit tests:
   ```bash
   python -m unittest discover tests
   ```

### Folder Structure
```
recall_threshold/
├── data/
├── src/
├── tests/
└── main.py
```

For more details, check the [`recall_threshold/README.md`](recall_threshold/README.md).

---

## License

This repository is licensed under the MIT License.
