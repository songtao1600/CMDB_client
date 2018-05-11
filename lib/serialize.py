# *_*author:songtao *_*
# *_*coding:utf-8 *_*

import json
from json.encoder import JSONEncoder
from .response import BaseResponse

class JsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,BaseResponse):
            return o.__dict__
        return JSONEncoder.default(self, o)

class Json(object):
    @staticmethod
    def dumps(response, ensure_ascii=True):
        return json.dumps(response, ensure_ascii=ensure_ascii, cls=JsonEncoder)