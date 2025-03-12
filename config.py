import os
import logging
from tenable.io import TenableIO

# Determine script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Logging Configuration - write log file in the same directory as the script
LOG_FILE_PATH = os.path.join(SCRIPT_DIR, "error.log")
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for Excel and environment keys
EXCEL_PATH = os.path.join(SCRIPT_DIR, 'data.xlsx')
# ACCESS_KEY = 'yuor_access_key_here'
# SECRET_KEY = 'your_secret_key_here'

def setup_tenable_io():
    """Set up the TenableIO connection using hardcoded credentials."""
    
    """Set up the TenableIO connection by prompting for user credentials."""
    # Prompt user for access and secret keys
    access_key = input("Please enter your Tenable Access Key: ")
    secret_key = input("Please enter your Tenable Secret Key: ")
    
    # Check if the keys are not set
    if not access_key or not secret_key:
        print("\033[91mTenable access key and/or secret key are not set.\033[0m")
        logging.error("ERROR - Tenable access key and/or secret key are not set.")
        return None
    
    # Create the TenableIO connection
    return TenableIO(access_key, secret_key)