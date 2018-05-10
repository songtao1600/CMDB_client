# *_*author:songtao *_*
# *_*coding:utf-8 *_*

class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.message = None
        self.error = None
        self.data = True