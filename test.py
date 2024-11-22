from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
RESTAURANT_NAME = os.getenv('RESTAURANT_NAME')
DATE = os.getenv('DATE')
TARGET_TIME = os.getenv('TARGET_TIME')
EARLIEST = os.getenv('EARLIEST')
LATEST = os.getenv('LATEST')
PARTY_SIZE = os.getenv('PARTY_SIZE')

if __name__ == "__main__":


    print(EMAIL) 
    print(PASSWORD) 
    print(RESTAURANT_NAME)
    print(DATE)
    print(TARGET_TIME)
    print(EARLIEST)
    print(LATEST)
    print(PARTY_SIZE)

    EARLIEST = datetime.strptime(EARLIEST, "%H:%M:%S").time()
    print(EARLIEST)

    