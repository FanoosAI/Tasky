from sys import argv

# from opsdroid.cli import start
from opsdroid.cli.utils import (
    check_dependencies,
    configure_lang,
    welcome_message,
)
from opsdroid.configuration import load_config_file
from opsdroid.const import DEFAULT_CONFIG_LOCATIONS
from opsdroid.core import OpsDroid
from opsdroid.logging import configure_logging

import googleAPI
import mongo_manager


def setup():
    # googleAPI.init()
    mongo_manager.setup()


def start_server(path=None):
    check_dependencies()

    config_path = [path] if path else DEFAULT_CONFIG_LOCATIONS
    config = load_config_file(config_path)

    configure_lang(config)
    configure_logging(config.get("logging", {}))
    welcome_message(config)

    with OpsDroid(config=config, config_path=config_path) as opsdroid:
        opsdroid.run()


if __name__ == '__main__':
    setup()
    if len(argv) > 1:
        if argv[1]:
            start_server(argv[1])

    start_server()
