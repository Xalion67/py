from random import randint
from time import sleep
import sys


START_GREEN = '\033[38;5;48m'
END_GREEN = '\033[0m'


while True:
    try:
        print(START_GREEN + chr(randint(33, 126)) + END_GREEN, end='')
        sys.stdout.flush()
        sleep(0.005)
    except KeyboardInterrupt:
        print('\nLog out\n')
        break
