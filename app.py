import asyncio

from functions.parse_balances import parse_balances
from utils.create_files import create_files

if __name__ == '__main__':
    create_files()
    parse_balances(asyncio.new_event_loop())
