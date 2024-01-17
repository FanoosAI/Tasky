from opsdroid.cli.start import start
import googleAPI
import yaml


def setup():
    googleAPI.init()


if __name__ == '__main__':
    setup()
    # start()
