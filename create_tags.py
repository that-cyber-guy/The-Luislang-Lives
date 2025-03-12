import logging
import re
from tqdm import tqdm
import openpyxl_dictreader

error_tags = []

def process_tags(tio, excel_path, sheet_name, filter_key, filter_type='eq'):
    """Process tags based on the provided sheet name and filter."""
    reader = openpyxl_dictreader.DictReader(excel_path, sheet_name)
    total_rows = sum(1 for row in openpyxl_dictreader.DictReader(excel_path, sheet_name) if any(row.values()))

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

def print_error_tags():
    """Prints the tags that encountered errors during processing."""
    if error_tags:
        print("Tag categories and values with errors: Please see the log file for details.")
        for category, value, rule in set(error_tags):
            print(f"Category: {category}, Value: {value}, Rule: {rule}")
    else:
        print("No errors encountered.")