import redis
from json import loads


class Redis(object):

    def __init__(self,app=None):
        if app:
           self.init_app(app)

    def init_app(self,app):
        '''初始化工具类，从flask配置文件中读取相关参数
        :param app: Flask app
        :return: None
        '''
        redis_host = app.config.get('REDIS_HOST')
        redis_port = app.config.get('REDIS_PORT')
        redis_password = app.config.get('REDIS_PASSWORD')
        redis_db = app.config.get('REDIS_DB')
        pool = redis.ConnectionPool(host=redis_host,port=redis_port,db=redis_db,password=redis_password)
        self.r = redis.Redis(connection_pool=pool)

        return

    def set(self,name,value,ex=None):
        '''
        :param name: key名
        :param value: 存储的值
        :param ex: 过期时间
        :return: True or False
        '''
        return self.r.set(name=name,value=value,ex=ex)

    def get(self,name,json:bool):
        '''
        :param name: key名
        :param json: True or False, key是否为json对象
        :return:
        '''
        value = self.r.get(name)
        if value:
            if json:
                return loads(value.decode())
            return value
