# src/fsm.py
from src.logger import setup_logger

logger = setup_logger()

class FSM:
    """
    A generic Finite State Machine (FSM) class.
    """
    def __init__(self, states, input_alphabet, initial_state, final_states, transition_function):
        self.states = states
        self.input_alphabet = input_alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.current_state = initial_state

    def reset(self):
        """Reset the FSM to the initial state."""
        self.current_state = self.initial_state
        logger.info("FSM reset to initial state %s", self.initial_state)

    def process_input(self, input_sequence):
        """Process an input sequence."""
        for symbol in input_sequence:
            if symbol not in self.input_alphabet:
                logger.error(f"Invalid input symbol encountered: {symbol}")
                raise ValueError(f"Invalid input symbol: {symbol}")
            key = (self.current_state, symbol)
            if key not in self.transition_function:
                logger.error(f"No transition defined for state {self.current_state} with input {symbol}")
                raise ValueError(f"No transition defined for state {self.current_state} with input {symbol}")
            next_state = self.transition_function[key]
            logger.info("Transition from state %s to %s on input %s", self.current_state, next_state, symbol)
            self.current_state = next_state
        return self.current_state

    def get_current_state(self):
        """Return the current state."""
        return self.current_state
