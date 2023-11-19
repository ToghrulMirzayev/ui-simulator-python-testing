"""
Module contains custom logger implementation
"""
from __future__ import annotations
import logging as log


class CustomLogger:
    def __init__(self, log_level=log.INFO, log_file='logfile.log'):
        """
        Custom implementation of logger
        :param log_level: level for log
        :param log_file: file that will contain logs
        """
        self.log_level = log_level
        self.log_file = log_file
        self.logger = self._set_logger()

    def _set_logger(self) -> log.Logger:
        """
        Method that will create custom way implementation of logging
        :return: Logger class
        """
        logger_name = f"{self._set_logger.__name__}"

        logger = log.getLogger(logger_name)
        logger.setLevel(self.log_level)

        fh = log.FileHandler(self.log_file)
        formatter = log.Formatter("%(asctime)s - %(levelname)s - %(message)s", '%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger

    def log(self, message: str, level: int | None = None) -> None:
        """
        Methid that will capture the log
        :param message: Message for log
        :param level: Level for log
        :return: None
        """
        if level is None:
            level = self.log_level
        self.logger.log(level, message)
