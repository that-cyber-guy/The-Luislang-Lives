import logging
from config import setup_tenable_io, EXCEL_PATH
from create_tags import process_tags, print_error_tags
# from create_user_groups import process_user_groups  # Uncomment and use it when needed

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

# Configure global logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    """Main function to orchestrate the tag processing."""
    try:
        tio = setup_tenable_io()
        
        # Check if TenableIO setup failed
        if tio is None:
            logging.error("Failed to initialize Tenable.io setup")
            return  # Exit the function if setup fails
        
        logging.info("Started processing...")

        # Process IPv4 tags with 'eq' filter type
        process_tags(tio, EXCEL_PATH, "tags_ipv4", 'ipv4', 'eq')
        logging.info("Processing IPv4 tags with 'eq' filter type")

        # Process OS tags with 'match' filter type
        process_tags(tio, EXCEL_PATH, "tags_for_os", 'operating_system', 'match')
        logging.info("Processing tags for OS with 'match' filter type")

           # Process FQDN tags with 'match' filter type
        process_tags(tio, EXCEL_PATH, "tags_for_fqdn", 'fqdn', 'eq')
        logging.info("Processing tags for OS with 'match' filter type")

        # # Process User Groups
        # process_user_groups(tio, EXCEL_PATH, 'user_groups')
        # print_error_groups()

        # Continue with other sheets/processes as needed
        logging.info("Completed processing.")
        print_error_tags()

    except ValueError as e:
        logging.critical(f"Setup failed: {e}")

if __name__ == "__main__":
    main()