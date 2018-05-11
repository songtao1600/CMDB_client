# *_*author:songtao *_*
# *_*coding:utf-8 *_*

from config import settings
from lib.log import Logger
from lib.serialize import Json
import hashlib,time,requests,json,os
from src import plugins

class AutoBase(object):
    def __init__(self):
        self.asset_api = settings.ASSET_API
        self.key = settings.KEY
        self.key_name = settings.AUTH_KEY_NAME

    def auth_key(self):
        '''
        接口认证
        :return:
        '''
        ha = hashlib.md5(self.key.encode('utf-8'))
        time_span = time.time()
        ha.update(bytes('%s|%f' % (self.key,time_span),encoding='utf-8'))
        encryption = ha.hexdigest()
        result = '%s|%f' % (encryption, time_span)

    def get_asset(self):
        '''
        get方式获取未采集的资产
        :return:
        '''
        try:
            headers = {}
            headers.update(self.auth_key())
            response = requests.get(url=self.asset_api, headers = headers)
        except Exception as e:
            response = e

        return response.json()

    def post_asset(self, msg, callback = None):
        '''
        post方式向接口发送资产信息
        :param msg:
        :param callback:
        :return:
        '''
        status = True
        try:
            headers = {}
            headers.update(self.auth_key())
            response = requests.post(url=self.asset_api, headers=headers, json=msg)
        except Exception as e:
            response = e
            status = False
        if callback:
            callback(status,response)

    def process(self):
        '''
        子类必须实现的方法
        :return:
        '''
        raise NotImplementedError('you must implement process method')

    def callback(self, status, response):
        '''
        资产提交后的回调函数
        :param status: 是否请求成功
        :param response: 请求成功，则是响应内容对象；请求错误，则是异常对象
        :return:
        '''
        if not status:
            Logger.log(str(response), False)
        ret = json.loads(response.text)
        if ret['code'] == 1000:
            Logger().log(ret['message'], True)
        else:
            Logger().log(ret['message'], False)


class AutoAgent(AutoBase):
    def __init__(self):
        self.cert_file_path = settings.CERT_FILE_PATH
        super(AutoAgent, self).__init__()

    def load_local_cert(self):
        '''
        获取本地标识
        :return:
        '''
        if not os.path.exists(self.cert_file_path):
            return None
        with open(self.cert_file_path, 'r') as f:
            data = f.read()
        if not data:
            return None
        cert = data.strip()
        return cert

    def write_local_cert(self, cert):
        '''
        写入本地标识
        :param cert:
        :return:
        '''
        if not os.path.exists(self.cert_file_path):
            os.makedirs(os.path.dirname(self.cert_file_path))
        with open(self.cert_file_path,'w') as f:
            f.write(cert)

    def process(self):
        """
        获取当前资产信息
        1. 在资产中获取主机名 cert_new
        2. 在本地cert文件中获取主机名 cert_old
        如果cert文件中为空，表示是新资产
            - 则将 cert_new 写入该文件中，发送数据到服务器（新资产）
        如果两个名称不相等
            - 如果 db=new 则，表示应该主动修改，new为唯一ID
            - 如果 db=old 则，表示
        :return:
        """
        server_info = plugins.get_server_info()
        if not server_info.status:
            return
        local_cert = self.load_local_cert()
        if local_cert:
            if local_cert == server_info.data['hostname']:
                pass
            else:
                server_info.data['hostname'] = local_cert
        else:
            self.write_local_cert(server_info.data['hostname'])
        server_json = Json.dump(server_info.data)
        self.post_asset(server_json, self.callback)

class AutoSSH(AutoBase):
    pass

class AutoSalt(AutoBase):
    pass

