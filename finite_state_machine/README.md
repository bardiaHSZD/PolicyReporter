
# Finite State Machine (FSM) for Modulo Three Calculation

## Project Overview

This project implements a generic Finite State Machine (FSM) class in Python and uses it to solve the modulo three problem for binary numbers. The FSM processes a binary string and computes the remainder when the binary number is divided by three.

## Features

- **Generic FSM Class**: Can be configured for any FSM problem.
- **Modulo Three FSM Configuration**: Specific setup for the modulo three calculation.
- **Command-Line Interface**: Accepts user input for binary numbers.
- **Unit Tests**: Covers valid and invalid input cases.
- **Logging**: Provides informative logs for state transitions.

## Requirements

- **Python**: Version 3.6 or higher.
- **Operating System**: Windows, macOS, or Linux.
- **Dependencies**: None (uses Python's standard library).

## Setup Instructions

### 1. Clone the Repository

If you have Git installed, you can clone the repository. Otherwise, you can manually create the project directory and files.

```bash
git clone https://github.com/yourusername/fsm_mod_three.git
cd fsm_mod_three
```

### 2. Install Python

Download and install Python from the [official website](https://www.python.org/downloads/). Ensure you add Python to your system PATH during installation.

### 3. Set Up Visual Studio Code (Optional)

- **Install Python Extension**: Open Visual Studio Code, go to the Extensions tab (Ctrl+Shift+X), search for "Python", and install the extension by Microsoft.
- **Open the Project Folder**: Go to `File` > `Open Folder` and select your project folder (`fsm_mod_three`).

### 4. Create Project Files

Ensure the following files are created in your project directory:

- `fsm.py`: Contains the generic FSM class.
- `mod_three_fsm.py`: Configures the FSM for the modulo three problem.
- `main.py`: Main script to run the application.
- `test_fsm.py`: Unit tests for the application.
- `README.md`: Project documentation (this file).

### 5. Install Dependencies (Optional)

If you use a virtual environment or have a `requirements.txt` file, you can install dependencies:

```bash
pip install -r requirements.txt
```

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
python -m unittest test_fsm.py
```

**Verbose Output**:

If you want more detailed output from the tests, run:

```bash
python -m unittest -v test_fsm.py
```

This will display each sub-test and provide detailed test case results.

**Total Number of Tests**:

After running the tests, the total number of sub-tests will be displayed:

```bash
Total number of sub-tests run: 14
```

### Using Logs

The application uses Python's `logging` module to log transitions between states during execution. Logs are set to the `INFO` level by default and will display state transitions and FSM resets in the console.

If you'd like to modify or view logs in more detail, you can change the logging configuration in the `fsm.py` file. Logs will look something like this:

```
INFO:fsm:FSM reset to initial state S0
INFO:fsm:Transition from state S0 to S1 on input 1
INFO:fsm:Transition from state S1 to S0 on input 1
```

To see logs while running the main script:

```bash
python main.py
```

To see logs while running tests:

```bash
python -m unittest test_fsm.py
```

### Logging Configuration

If you want to change the logging level or output the logs to a file instead of the console, modify the following lines in `fsm.py`:

```python
# fsm.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Change INFO to DEBUG, ERROR, etc.
logger = logging.getLogger(__name__)

# To log to a file, use:
# logging.basicConfig(filename='fsm.log', level=logging.INFO)
```

### Example of Running with Logs and Test Output

**Running the Main Script:**

```bash
python main.py
```

**Example Output:**

```
Enter a binary number: 1010
INFO:fsm:FSM reset to initial state S0
INFO:fsm:Transition from state S0 to S1 on input 1
INFO:fsm:Transition from state S1 to S2 on input 0
INFO:fsm:Transition from state S2 to S2 on input 1
INFO:fsm:Transition from state S2 to S1 on input 0
Remainder when 1010 is divided by 3: 1
```

**Running the Tests:**

```bash
python -m unittest test_fsm.py
```

**Example Output:**

```
INFO:fsm:FSM reset to initial state S0
INFO:fsm:Transition from state S0 to S1 on input 1
INFO:fsm:Transition from state S1 to S0 on input 1
INFO:fsm:Transition from state S0 to S0 on input 0
INFO:fsm:Transition from state S0 to S1 on input 1
......
----------------------------------------------------------------------
Ran 2 tests in 0.006s

OK
Total number of sub-tests run: 14
```

## Code Structure

- **fsm.py**: Contains the `FSM` class, which implements the generic finite state machine logic.
- **mod_three_fsm.py**: Configures the FSM specifically for the modulo three problem.
- **main.py**: Contains the `compute_mod_three` function and handles user interaction.
- **test_fsm.py**: Contains unit tests to validate the functionality of the FSM and modulo three calculation.
- **README.md**: Provides documentation and setup instructions for the project.

## Extending the FSM

To use the FSM class for other problems:

1. **Create a New Configuration Module**: Similar to `mod_three_fsm.py`, create a new Python file for your FSM configuration.
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

## Contact

For any questions or issues, please contact:

- **Email**: [youremail@example.com](mailto:youremail@example.com)
- **GitHub**: [yourusername](https://github.com/yourusername)

---

**Note**: Replace `[youremail@example.com]` and GitHub links with your actual contact information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
