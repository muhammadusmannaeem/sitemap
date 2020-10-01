"""__config.py: Config manipulation."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Umer Farooq"
__developers__ = ("Muhammad Usman Naeem", "Muhammad Umer Farooq")
__email__ = ("usman.naeem2212@gmail.com", "contact@muhammadumerfarooq.me")
__status__ = "Production"

import os


def get_config(key, filename="config.txt"):
    """
     Get config value from config file.
     Args:
         key: key the value you want to get!.
         filename: File to be opened!.
     Returns:
         mixed.
     Raises:
         None.
     """
    configurations = dict()
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        for line in lines:
            if not line.startswith("#") or not line.strip():
                c = line.split("=")
                configurations[c[0].strip()] = c[1].strip()

    if key in configurations:
        return configurations[key]
    else:
        return None
