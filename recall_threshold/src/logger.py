from loguru import logger
import sys

# Configure the logger
logger.remove()  # Remove default logger
logger.add(sys.stderr, level="INFO")  # Log to stderr with INFO level
logger.add("logs/threshold_optimizer.log", rotation="1 MB")  # Save logs to file
