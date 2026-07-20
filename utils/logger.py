"""
Centralized logging configuration.
"""

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name: Usually __name__.

    Returns:
        logging.Logger
    """
    return logging.getLogger(name)