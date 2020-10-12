import os
from pathlib import Path  # Python 3.6+ only

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


def get_configuration_value(configuration_key):
    return os.getenv(configuration_key)
