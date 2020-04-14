from configparser import ConfigParser
from pathlib import Path

FILE = Path(__file__).parent / 'config.ini'

config = ConfigParser()
config.read(FILE)