# *_*author:songtao *_*
# *_*coding:utf-8 *_*

import os, logging
from config import settings

class Logger(object):
    __instance = None

    def __init__(self):
        self.error_log_file = settings.ERROR_LOG_FILE
        self.run_log_file = settings.RUN_LOG_FILE
        self.run_logger = None
        self.error_logger = None

        self.init_error_log()
        self.init_run_log()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def check_path_exist(log_abs_file):
        log_path = os.path.split(log_abs_file)
        if not log_path:
            os.mkdir(log_path)

    def init_run_log(self):
        self.check_path_exist(self.run_log_file)
        file_obj = logging.FileHandler(self.run_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s :  %(message)s")
        file_obj.setFormatter(fmt)
        logger_obj = logging.Logger('run.log', level=logging.INFO)
        logger_obj.addHandler(file_obj)
        self.run_logger = logger_obj

    def init_error_log(self):
        self.check_path_exist(self.error_log_file)
        file_obj = logging.FileHandler(self.error_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s :  %(message)s")
        file_obj.setFormatter(fmt)
        logger_obj = logging.Logger('run.log', level=logging.ERROR)
        logger_obj.addHandler(file_obj)
        self.run_logger = logger_obj

