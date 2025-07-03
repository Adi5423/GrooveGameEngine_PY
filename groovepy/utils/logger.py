# groovepy/utils/logger.py

import logging
import sys

# ANSI escape codes for coloring
_COLORS = {
    "DEBUG": "\033[94m",    # blue
    "INFO": "\033[92m",     # green
    "WARNING": "\033[93m",  # yellow
    "ERROR": "\033[91m",    # red
}
_RESET = "\033[0m"

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        if levelname in _COLORS:
            prefix = _COLORS[levelname] + levelname + _RESET
            record.levelname = prefix
        return super().format(record)

def get_logger(name: str = __name__, level: int = logging.DEBUG) -> logging.Logger:
    """Creates or retrieves a logger with colored console output."""
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # avoid duplicate handlers

    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    fmt = "[%(asctime)s] [%(levelname)s] %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler.setFormatter(ColoredFormatter(fmt, datefmt))

    logger.addHandler(handler)
    return logger
