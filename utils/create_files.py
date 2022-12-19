import os
from typing import Optional

from pretty_utils.miscellaneous.files import touch, write_json, read_json

from data import config


def create_files():
    touch(os.path.join(config.ROOT_DIR, 'files'))
    touch(config.ADDRESSES_FILE, True)
    touch(config.PROXIES_FILE, True)
    touch(config.RESULT_FILE, True)

    try:
        current_settings: Optional[dict] = read_json(config.SETTINGS_FILE)
    except FileNotFoundError:
        current_settings = {}

    settings = {
        'threads': 10,
        'parse_nfts': False
    }

    for key, value in settings.items():
        if key not in current_settings:
            current_settings.update({key: value})

    write_json(config.SETTINGS_FILE, current_settings, 2)


create_files()
