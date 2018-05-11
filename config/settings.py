# *_*author:songtao *_*
# *_*coding:utf-8 *_*

import os

# 项目根目录
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\

# 用于API认证的KEY
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'

# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'

# 错误日志
ERROR_LOG_FILE = os.path.join(BASEDIR, "log", "error.log")

#运行日志
RUN_LOG_FILE = os.path.join(BASEDIR, 'log', 'run.log')

# Agent模式服务器唯一ID标识文件路径
CERT_FILE_PATH = os.path.join(BASEDIR, 'config', 'cert')

# 测试模式开关
TEST_MODE = True

# 资产采集方式(支持：ssh、salt、agent)
MODE = 'ssh'

# 如果是ssh模式，需要配置user和key
# SSH_PRIVATE_KEY = 'C:\Users\Administrator\.ssh\id_rsa'
SSH_PRIVATE_KEY = os.path.join(BASEDIR, '.ssh', 'id_rsa')
SSH_USER = 'root'
SSH_PORT = '22'

# 采集资产信息的url
PLUGINS_DICT = {
    'disk': 'src.plugins.disk.DiskPlugin',
    'cpu': 'src.plugins.cpu.CpuPlugin',
}

# 资产信息API
ASSET_API = 'http:127.0.0.1:8000/api/asset'

