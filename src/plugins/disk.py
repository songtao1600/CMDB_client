# *_*author:songtao *_*
# *_*coding:utf-8 *_*
from .base import BasePlugin
from lib.response import BaseResponse

class DiskPlugin(BasePlugin):
    def linux(self):
        response = BaseResponse()