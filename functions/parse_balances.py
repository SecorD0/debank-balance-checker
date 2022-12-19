import asyncio
import logging
import re
from typing import List, Dict, Optional

from pretty_utils.miscellaneous.files import read_lines
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime
from pretty_utils.type_functions.lists import split_list
from pretty_utils.type_functions.strings import format_number
from py_debank_async.custom import get_balance
from py_debank_async.models import Chain

from data import config
from data.models import Settings


async def parse(address: str, parse_nfts: bool, proxies: str or List[str]) -> Dict[str, Optional[Dict[str, Chain]]]:
    tries = 3
    info = {address: None}
    for i in range(tries):
        try:
            balances = await get_balance(address=address, parse_nfts=parse_nfts, proxies=proxies)
            if balances:
                info[address] = balances
                print(f'[V] {address}')
                break

        except:
            logging.exception(f'parse {i}')

        if i >= tries - 1:
            print(f'[X] {address}')

        else:
            await asyncio.sleep(10)

    return info


async def run(addresses: List[str], proxies: str or List[str]):
    tasks = []
    for address in addresses:
        task = asyncio.ensure_future(parse(address, Settings().parse_nfts, proxies))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    return await responses


def parse_balances(loop):
    asyncio.set_event_loop(loop)

    addresses = []
    for address in read_lines(config.ADDRESSES_FILE, True):
        if re.match('0x' + r'\w' * 40, address):
            addresses.append(address)

    addresses = list(dict.fromkeys(addresses))
    if addresses:
        not_parsed = []
        header = 'Checking time: {checking_time}\nTotal addresses: {total_addresses}\nTotal balance: ${total_usd_value}\n'
        text = ''
        total_addresses = len(addresses)
        total_usd_value = 0
        address_list = split_list(addresses, Settings().threads)
        for addresses in address_list:
            proxies = read_lines(config.PROXIES_FILE, True)
            future = asyncio.ensure_future(run(addresses, proxies))
            responses = loop.run_until_complete(future)
            results: Dict[str, Optional[Dict[str, Chain]]] = {}
            for response in responses:
                results.update(response)

            for address in addresses:
                balances = results.get(address)
                address_usd_value = 0
                text += '------------------------ Address {address} (${address_usd_value})\n'
                if balances:
                    for chain, balance in balances.items():
                        usd_value = balance.usd_value
                        address_usd_value += usd_value
                        text += f'\n------------ {chain} (${format_number(usd_value, 2)})'
                        if balance.tokens:
                            text += f'\nTokens ({len(balance.tokens)}):'
                            for token in balance.tokens:
                                text += f'\n\t{format_number(token.amount)} {token.symbol} (${format_number(token.usd_value, 2)})'

                            text += '\n\n'

                        if balance.projects:
                            text += f'\nProjects ({len(balance.projects)}):'
                            for project in balance.projects:
                                text += f'\n\t{project.name} {project.site_url}: (${format_number(project.usd_value, 2)})'
                                for portfolio_item in project.portfolio_item_list:
                                    tokens = ' + '.join(
                                        f'{format_number(token.amount)} {token.symbol} (${format_number(token.usd_value, 2)})' for
                                        token in
                                        portfolio_item.tokens)
                                    text += f'\n\t\t{portfolio_item.name} (${format_number(portfolio_item.asset_usd_value, 2)}): {tokens}'

                                text += '\n'

                            text += '\n\n'

                        if balance.nfts:
                            text += f'\nNFTs ({len(balance.nfts)}):'
                            for nft in balance.nfts:
                                collection = nft.collection
                                text += (f'\n\t{nft.amount} pcs, {nft.name}, collection: {collection.name}, '
                                         f'avg. price: {format_number(collection.avg_price_24h)} '
                                         f'{collection.spent_token.symbol} (${format_number(collection.spent_token.usd_value, 2)})')

                            text += '\n\n'

                else:
                    text += 'ERROR'
                    not_parsed.append(address)

                text += '\n\n'
                total_usd_value += address_usd_value
                text = text.format(address=address, address_usd_value=format_number(address_usd_value, 2))

        header = header.format(checking_time=unix_to_strtime(), total_addresses=total_addresses,
                               total_usd_value=format_number(total_usd_value, 2))
        text = header + text
        if not_parsed:
            text += f'Not parsed balances ({len(not_parsed)}):\n' + '\n'.join(not_parsed) + '\n'

        print(f'\n\n\n{text}')
        try:
            with open(config.RESULT_FILE, 'a') as file:
                file.write(text + '\n')

            print(f'The result is written in the {config.RESULT_FILE} file!')

        except:
            print(f'Failed to write result to the {config.RESULT_FILE} file!')

    else:
        print("You didn't provide any addresses!")

    input('\nPress Enter to exit.\n')
