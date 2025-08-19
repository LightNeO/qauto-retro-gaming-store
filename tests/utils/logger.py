import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Generate a log file name with the current timestamp
log_file_name = f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# Get the root logger
logger = logging.getLogger("qauto-retro-gaming-store")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if this module is imported multiple times
if not logger.handlers:
    # Create a file handler to write log messages to a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create a console handler to display log messages in the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
