
from mod_three_fsm import mod_three_fsm

def compute_mod_three(binary_string):
    """
    Compute the remainder when the binary number represented by binary_string is divided by three.

    Parameters:
    - binary_string: A string of '0's and '1's representing a binary number.

    Returns:
    - The remainder as an integer (0, 1, or 2).
    """
    fsm = mod_three_fsm()
    # Process each character in the binary string, from most significant bit
    input_sequence = list(binary_string)
    try:
        fsm.reset()
        fsm.process_input(input_sequence)
        final_state = fsm.get_current_state()
        # Map the final state to the remainder
        state_to_remainder = {'S0': 0, 'S1': 1, 'S2': 2}
        remainder = state_to_remainder[final_state]
        return remainder
    except ValueError as e:
        print(f"Error processing input: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    binary_input = input("Enter a binary number: ")
    remainder = compute_mod_three(binary_input)
    if remainder is not None:
        print(f"Remainder when {binary_input} is divided by 3: {remainder}")
