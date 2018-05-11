# *_*author:songtao *_*
# *_*coding:utf-8 *_*

from src.plugins.base import BasePlugin
from config import settings

def get_server_info(hostname=None):
    '''
    获取服务器信息
    :param  hostname: agent模式时，hostname为空；salt或ssh模式时，hostname表示要连接的远程服务器
    :return:
    '''
    response = {}
    # response = BasePlugin(hostname).execute()
    # if not response.status:
    #     return response
    for k,v in settings.PLUGINS_DICT.items():
        import importlib
        module_path, cls_name = v.rsplit('.',1)
        cls = getattr(importlib.import_module(module_path),cls_name)
        obj = cls(hostname).execute()
        response[k] = obj
    return response

if __name__ == '__main__':
    ret = get_server_info()
    print(ret.__dict__)