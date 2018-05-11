# *_*author:songtao *_*
# *_*coding:utf-8 *_*

from config import settings
from src import client

def client():
    if settings.MODE == 'agent':
        cli = client.AutoAgent()
    elif settings.MODE == 'ssh':
        cli = client.AutoSSH()
    elif settings.MODE == 'salt':
        cli = client.AutoSalt()
    else:
        raise Exception('请配置资产采集模式，如：ssh、agent、salt')
    cli.process()