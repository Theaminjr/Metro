HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def print_header(text):
    print(f"{HEADER}{text}{ENDC}")

def print_OKBLUE(text):
    print(f"{OKBLUE}{text}{ENDC}")

def print_OKGREEN(text):
    print(f"{OKGREEN}{text}{ENDC}")

def print_FAIL(text):
    print(f"{FAIL}{text}{ENDC}")

def print_WARNING(text):
    print(f"{WARNING}{text}{ENDC}")
    
def print_OPTIONS(text):
    print(f"{OKCYAN}{text}{ENDC}")