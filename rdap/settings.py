import os


# General Settings
DNS_FILE_CHECK_INTERVAL = 7 # Number of days to evaluate until check again the dns file
RDAP_CACHE_FILENAME = "cache.json" # Name of the file where the history is going to be saved
RDAP_DNS_FILENAME = "dns.json" # Name of the file where the hosts and tlds are going to be saved.
UNDEFINED_DATA = "Undefined" # Name of the variable to show if some data is not present.


# Files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Base dir of the project
