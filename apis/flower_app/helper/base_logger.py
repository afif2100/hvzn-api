import logging
import sys
import os


def BaseLogger(name, log_path=None):
    process_id = os.getpid()
    formatter = logging.Formatter(fmt=f'[%(asctime)s] [{process_id}] [%(levelname)-4s] {name}: %(message)s',
                                  datefmt="%Y-%m-%d %H:%M:%S %z")

    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if log_path:
        handler = logging.FileHandler(log_path, mode='w')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

# logger = BaseLogger("app name")
# logger.info("hallo info")
# logger.debug("hallo debug")