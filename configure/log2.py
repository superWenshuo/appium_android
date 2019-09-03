 
 
'''
@module: loggingmodule.FinalLogger
 
'''
import logging,os,time
from logging import handlers


class Logger(object):

    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        # 创建一个handler 写入文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) 
        th = handlers.logging.FileHandler('../Result/log/{0}.log'.format(rq), encoding='utf-8')
        # 判断文件夹是否存在
        if not os.path.exists('../Result/log/'):
            os.makedirs('../Result/log')
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
             
            streamhandler = logging.StreamHandler()
            #什么级别以上的放入日志中
            streamhandler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            streamhandler.setFormatter(formatter)
            self.logger.addHandler(streamhandler)
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    log2 = Logger('all.log',level='debug')
    log2.logger.debug('debug')
    log2.logger.info('info')
    log2.logger.warning('警告')
    log2.logger.error('报错')
    log2.logger.critical('严重')
    Logger('error.log', level='error').logger.error('error')