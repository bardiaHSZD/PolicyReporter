
# Finite State Machine (FSM) for Modulo Three Calculation

## Project Overview

This project implements a generic Finite State Machine (FSM) class in Python and uses it to solve the modulo three problem for binary numbers. The FSM processes a binary string and computes the remainder when the binary number is divided by three.

## Features

- **Generic FSM Class**: Can be configured for any FSM problem.
- **Modulo Three FSM Configuration**: Specific setup for the modulo three calculation.
- **Command-Line Interface**: Accepts user input for binary numbers.
- **Unit Tests**: Covers valid and invalid input cases.
- **Logging**: Provides informative logs for state transitions.
- **Colored Logs**: Terminal logs are color-coded using the `colorlog` library for improved readability.

## Requirements

- **Python**: Version 3.6 or higher.
- **Operating System**: Windows, macOS, or Linux.
- **Dependencies**: 
  - `colorlog` for colored terminal output: Install it via `pip install colorlog`.

## Folder Structure

```
project_root/
│
├── logs/                # To keep the log files
│   └── fsm.log          # Logs are stored here (plain text)
│
├── src/                 # To keep the source files and utilities
│   ├── __init__.py
│   ├── fsm.py           # FSM class implementation
│   ├── logger.py        # Logger configuration (with colors)
│   └── utils.py         # Utility functions, including mod_three_fsm
│
├── tests/               # To keep unit tests
│   ├── __init__.py
│   └── test_fsm.py      # Unit tests
│
└── main.py              # Entry point of the application
```

## Setup Instructions

### 1. Clone the Repository

If you have Git installed, you can clone the repository. Otherwise, you can manually create the project directory and files.

```bash
cd finite_state_machine
```

### 2. Install Python

Download and install Python from the [official website](https://www.python.org/downloads/). Ensure you add Python to your system PATH during installation.

### 3. Install Dependencies

Install the `colorlog` library for colored terminal output. Run the following command:

```bash
pip install colorlog
```

### 4. Create Project Files

Ensure the following files are created in your project directory:

- `fsm.py`: Contains the generic FSM class.
- `logger.py`: Configures the logger to output colored logs in the terminal and plain logs to a file.
- `utils.py`: Configures the FSM for the modulo three problem.
- `main.py`: Main script to run the application.
- `test_fsm.py`: Unit tests for the application.
- `README.md`: Project documentation (this file).

## Running the Application

### Run the Main Script

In the terminal, navigate to your project directory and run:

```bash
python main.py
```

The script will prompt you to enter a binary number:

```
Enter a binary number: 1101
```

**Example Output:**

```
Remainder when 1101 is divided by 3: 1
```

### Running Unit Tests

To execute the unit tests, run the following command in your terminal:

```bash
python -m unittest tests/test_fsm.py
```

**Verbose Output**:

If you want more detailed output from the tests, run:

```bash
python -m unittest -v tests/test_fsm.py
```

This will display each sub-test and provide detailed test case results.

**Total Number of Tests**:

After running the tests, the total number of sub-tests will be displayed:

```bash
Total number of sub-tests run: 14
```

### Using Logs

The application uses Python's `logging` module and `colorlog` to log transitions between states during execution. Logs are set to the `INFO` level by default and will display state transitions and FSM resets in the console (with colors) and in the `logs/fsm.log` file (plain text).

If you'd like to modify or view logs in more detail, you can change the logging configuration in the `logger.py` file.

### Example of Running with Logs and Test Output

**Running the Main Script:**
```bash
python main.py
```

**Example Terminal Output (with Colors):**
```bash
Enter a binary number: 1010
2024-10-03 - INFO - FSM reset to initial state S0
2024-10-03 - INFO - Transition from state S0 to S1 on input 1
2024-10-03 - INFO - Transition from state S1 to S2 on input 0
2024-10-03 - INFO - Transition from state S2 to S2 on input 1
2024-10-03 - INFO - Transition from state S2 to S1 on input 0
Remainder when 1010 is divided by 3: 1
```

**Running the Tests:**

```bash
python -m unittest tests/test_fsm.py
```

**Example Terminal Output (with Colors):**
```
2024-10-03 - INFO - FSM reset to initial state S0
2024-10-03 - INFO - Transition from state S0 to S1 on input 1
2024-10-03 - INFO - Transition from state S1 to S0 on input 1
2024-10-03 - ERROR - Invalid input symbol encountered: 2
```

### Example Output in `logs/fsm.log` (Plain Text):
```
2024-10-03 - INFO - FSM reset to initial state S0
2024-10-03 - INFO - Transition from state S0 to S1 on input 1
2024-10-03 - INFO - Transition from state S1 to S0 on input 1
2024-10-03 - ERROR - Invalid input symbol encountered: 2
```

### Logging Configuration

If you want to change the logging level or output the logs to a file instead of the console, modify the following lines in `logger.py`:

```python
# logger.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Change INFO to DEBUG, ERROR, etc.
logger = logging.getLogger(__name__)

# To log to a file, use:
# logging.basicConfig(filename='fsm.log', level=logging.INFO)
```

## Code Structure

- **fsm.py**: Contains the `FSM` class, which implements the generic finite state machine logic.
- **logger.py**: Configures the logger to write to both the console (with colors) and a log file (plain text).
- **utils.py**: Configures the FSM specifically for the modulo three problem.
- **main.py**: Contains the `compute_mod_three` function and handles user interaction.
- **test_fsm.py**: Contains unit tests to validate the functionality of the FSM and modulo three calculation.
- **README.md**: Provides documentation and setup instructions for the project.

## Extending the FSM

To use the FSM class for other problems:

1. **Create a New Configuration Module**: Similar to `utils.py`, create a new Python file for your FSM configuration.
2. **Define FSM Components**:
   - **States (Q)**
   - **Input Alphabet (Σ)**
   - **Initial State (q0)**
   - **Final/Accepting States (F)**
   - **Transition Function (δ)**
3. **Instantiate the FSM**: Use your configuration to create an `FSM` instance.
4. **Process Input**: Use the `process_input` method to process your input sequence.
5. **Integrate into Application**: Use your FSM in the application logic as needed.

## Error Handling

- **Invalid Input Symbols**: The FSM will raise a `ValueError` if an input symbol is not in the input alphabet.
- **Undefined Transitions**: The FSM will raise a `ValueError` if there is no transition defined for a given state and input symbol.
- **User Feedback**: The application catches exceptions and informs the user of invalid inputs.
