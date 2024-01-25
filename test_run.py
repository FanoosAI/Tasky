import datetime

from opsdroid.configuration import load_config_file
from opsdroid.logging import configure_logging
from opsdroid.core import OpsDroid
from opsdroid.cli.utils import configure_lang, check_dependencies
from opsdroid.cli import start

import googleAPI
from googleAPI import get_events

from nlu import manual_rasa_caller

if __name__ == '__main__':
    check_dependencies()
    config_path = ["configuration.yaml"]
    config = load_config_file(config_path)

    configure_lang(config)
    configure_logging(config.get("logging", {}))
    bot_instance = OpsDroid(config=config, config_path=config_path)
    bot_instance.run()