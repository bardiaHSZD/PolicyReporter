# src/logger.py
import logging
import os
import colorlog  # Import colorlog for colored logs in the terminal

def setup_logger():
    """
    Sets up a logger for the FSM application, writing logs to both the terminal (with colors) and a file (plain text).
    """
    # Ensure the logs directory exists
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Configure logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create handlers
    file_handler = logging.FileHandler(os.path.join(log_dir, 'fsm.log'))  # Log to file
    console_handler = logging.StreamHandler()  # Log to console (terminal)

    # Set level for handlers
    file_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)

    # Create a logging format for the file (plain text)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Create a logging format for the console (with colors)
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'bold_blue',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_purple',
        }
    )
    console_handler.setFormatter(color_formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
