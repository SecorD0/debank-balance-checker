from pretty_utils.miscellaneous.files import read_json
from pretty_utils.type_functions.classes import AutoRepr

from data import config


class Settings(AutoRepr):
    def __init__(self):
        json_settings = read_json(config.SETTINGS_FILE)

        self.threads: int = json_settings.get('threads')
        self.parse_nfts: bool = json_settings.get('parse_nfts')
