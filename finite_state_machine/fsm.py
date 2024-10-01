# fsm.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FSM:
    """
    A generic Finite State Machine (FSM) class.
    """

    def __init__(self, states, input_alphabet, initial_state, final_states, transition_function):
        """
        Initialize the FSM.

        Parameters:
        - states: a set of states (Q)
        - input_alphabet: a set of input symbols (Σ)
        - initial_state: the initial state (q0)
        - final_states: a set of accepting/final states (F)
        - transition_function: a dictionary mapping (state, input_symbol) to next_state (δ)
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

        self.current_state = initial_state

    def reset(self):
        """Reset the FSM to the initial state."""
        self.current_state = self.initial_state
        logger.info(f"FSM reset to initial state {self.initial_state}")

    def process_input(self, input_sequence):
        """
        Process an input sequence (list of input symbols).

        Parameters:
        - input_sequence: a list of input symbols

        Returns:
        - The final state after processing the input sequence.
        """
        for symbol in input_sequence:
            if symbol not in self.input_alphabet:
                raise ValueError(f"Invalid input symbol: {symbol}")
            key = (self.current_state, symbol)
            if key not in self.transition_function:
                raise ValueError(f"No transition defined for state {self.current_state} with input {symbol}")
            next_state = self.transition_function[key]
            logger.info(f"Transition from state {self.current_state} to {next_state} on input {symbol}")
            self.current_state = next_state
        return self.current_state

    def get_current_state(self):
        """Return the current state."""
        return self.current_state
