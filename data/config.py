import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ERRORS_FILE = os.path.join(ROOT_DIR, 'files', 'errors.log')

ADDRESSES_FILE = os.path.join(ROOT_DIR, 'files', 'addresses.txt')
PROXIES_FILE = os.path.join(ROOT_DIR, 'files', 'proxies.txt')
SETTINGS_FILE = os.path.join(ROOT_DIR, 'files', 'settings.json')
RESULT_FILE = os.path.join(ROOT_DIR, 'files', 'result.txt')
