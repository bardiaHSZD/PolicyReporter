from src.fsm import FSM

def mod_three_fsm():
    """
    Configure the FSM for the modulo-three problem.
    """
    states = {'S0', 'S1', 'S2'}
    input_alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = states
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2',
    }
    return FSM(states, input_alphabet, initial_state, final_states, transition_function)
