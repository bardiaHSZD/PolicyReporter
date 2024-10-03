# main.py
from src.utils import mod_three_fsm

def compute_mod_three(binary_string):
    """
    Compute the remainder when the binary number is divided by 3.
    """
    fsm = mod_three_fsm()
    input_sequence = list(binary_string)
    try:
        fsm.reset()
        fsm.process_input(input_sequence)
        final_state = fsm.get_current_state()
        state_to_remainder = {'S0': 0, 'S1': 1, 'S2': 2}
        remainder = state_to_remainder[final_state]
        return remainder
    except ValueError as e:
        print(f"Error processing input: {e}")
        return None

if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    remainder = compute_mod_three(binary_input)
    if remainder is not None:
        print(f"Remainder when {binary_input} is divided by 3: {remainder}")
