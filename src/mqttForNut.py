import logging
import os
from . import mqtt

log = logging.getLogger("mqtt-for-nut")


def setup(self, parameter_list):
    """
    docstring
    """

    comm = mqtt()
    
    

if __name__ == "__main__":
    """[summary]
    """
    logging.basicConfig(level=logging.DEBUG)
    log.info("BEGIN")
    setup()
