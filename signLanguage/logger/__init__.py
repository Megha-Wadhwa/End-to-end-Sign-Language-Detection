import logging
import os
from datetime import datetime
from from_root import from_root

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_path = os.path.join(from_root(), 'log', LOG_FILE)

# Create the log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Define the full path to the log file
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=lOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)