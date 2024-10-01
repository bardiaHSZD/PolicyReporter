from loguru import logger
import sys

# Configure logger
logger.remove()  # Remove default logger
logger.add(sys.stderr, level="INFO")  # Adjust log level as needed
logger.add("logs/threshold_optimizer.log", rotation="1 MB")
