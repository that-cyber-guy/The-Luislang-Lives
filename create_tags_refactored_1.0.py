import os
import logging
import re
from tenable.io import TenableIO
from tqdm import tqdm
import openpyxl_dictreader

ascii_art = r"""
   
______          _           _          
| ___ \        (_)         | |         
| |_/ / __ ___  _  ___  ___| |_        
|  __/ '__/ _ \| |/ _ \/ __| __|       
| |  | | | (_) | |  __/ (__| |_        
\_|  |_|  \___/| |\___|\___|\__|       
              _/ |                     
             |__/                      
 _           _     _                   
| |         (_)   | |                  
| |    _   _ _ ___| | __ _ _ __   __ _ 
| |   | | | | / __| |/ _` | '_ \ / _` |
| |___| |_| | \__ \ | (_| | | | | (_| |
\_____/\__,_|_|___/_|\__,_|_| |_|\__, |
                                  __/ |
                                 |___/ 

                              (_)(_)
                             /     \
                            /       |
                           /   \  * |
             ________     /    /\__/
     _      /        \   /    /
    / \    /  ____    \_/    /
   //\ \  /  /    \         /
   V  \ \/  /      \       /
       \___/        \_____/
Automate everything!                                          
"""
print(ascii_art)

# Determine script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Logging Configuration - write log file in the same directory as the script
LOG_FILE_PATH = os.path.join(SCRIPT_DIR, "tag_errors.log")
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for Excel and environment keys
EXCEL_PATH = os.path.join(SCRIPT_DIR, 'data.xlsx')
ENV_ACCESS_KEY = 'TENABLE_ACCESS_KEY'
ENV_SECRET_KEY = 'TENABLE_SECRET_KEY'

# List to store tag categories and values with errors
error_tags = []

def setup_tenable_io():
    access_key = os.getenv(ENV_ACCESS_KEY)
    secret_key = os.getenv(ENV_SECRET_KEY)
    return TenableIO(access_key, secret_key)

def process_tags(tio, sheet_name, filter_key, filter_type='eq'):
    reader = openpyxl_dictreader.DictReader(EXCEL_PATH, sheet_name)
    total_rows = sum(1 for row in openpyxl_dictreader.DictReader(EXCEL_PATH, sheet_name) if any(row.values()))

    with tqdm(total=total_rows, desc=f"Processing {sheet_name}") as pbar:
        for row in reader:
            if not any(row.values()):
                continue
            try:
                tag_category = row['tag_category']
                tag_value = row['tag_value']
                filter_value = row[filter_key]
                tio.tags.create(
                    category=tag_category,
                    value=tag_value,
                    filters=[(filter_key, filter_type, filter_value)]
                )
            except Exception as e:
                error_message = str(e)
                rule_match = re.search(r'"rule":"([^"]+)"', error_message)
                rule = rule_match.group(1) if rule_match else "unknown"
                logging.error(f"Error processing row {row} with filter value {filter_value}: rule: {rule}")
                error_tags.append((tag_category, tag_value, rule))
            finally:
                pbar.update(1)

def main():
    tio = setup_tenable_io()
    logging.info("Started processing...")

    # Process IPv4 tags with 'eq' filter type
    process_tags(tio, "tags_ipv4", 'ipv4', 'eq')
    logging.info("Processing IPv4 tags with 'eq' filter type")

    # Process OS tags with 'match' filter type
    process_tags(tio, "tags_for_os", 'operating_system', 'match')
    logging.info("Processing tags for OS with 'match' filter type")

    # Continue with other sheets/processes as needed
    logging.info("Completed processing.")

    # Print tag categories and values with errors
    if error_tags:
        print("Tag categories and values with errors: Please see the log file for details.")
        for category, value, rule in set(error_tags):
            print(f"Category: {category}, Value: {value}, Rule: {rule}")
    else:
        print("No errors encountered.")

if __name__ == "__main__":
    main()