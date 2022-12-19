import asyncio

import utils
from functions.parse_balances import parse_balances

if __name__ == '__main__':
    parse_balances(asyncio.new_event_loop())
