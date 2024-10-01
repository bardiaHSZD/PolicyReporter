
from fsm import FSM

def mod_three_fsm():
    """
    Configure the FSM for the modulo three problem.

    Returns:
    - An instance of FSM configured for modulo three calculation.
    """
    # Define the states
    states = {'S0', 'S1', 'S2'}

    # Define the input alphabet
    input_alphabet = {'0', '1'}

    # Define the initial state
    initial_state = 'S0'

    # Define the set of accepting/final states
    final_states = states  # All states are accepting in this context

    # Define the transition function
    # (state, input_symbol) -> next_state
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2',
    }

    # Create the FSM instance
    fsm = FSM(states, input_alphabet, initial_state, final_states, transition_function)

    return fsm
