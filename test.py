# *_*author:songtao *_*
# *_*coding:utf-8 *_*

from config import settings
import os




def check_path_exist(log_abs_file):
    log_path,a = os.path.split(log_abs_file)

    print(log_abs_file,a)
    print(log_path)
    if not os.path.exists(log_path):
        os.mkdir(log_path)

run_log_file = settings.RUN_LOG_FILE
file2 = check_path_exist(run_log_file)

