# -*- coding:UTF-8 -*-
import logging
import os
import time

"""
指定保存日志的文件路径，日志级别，以及调用文件
将日志存入到指定的文件中
:param logger:
"""

def get_log(message):
        global logger
        logger = logging.getLogger('AUTOTEST')
        # 判断文件夹是否存在
        if not os.path.exists('../Result/log/'):
            os.makedirs('../Result/log')
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not logger.handlers:
            
            streamhandler = logging.StreamHandler()
            #什么级别以上的放入日志中
            streamhandler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            streamhandler.setFormatter(formatter)
            logger.addHandler(streamhandler)
           
            # 创建一个handler 写入文件
            rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) 
            # 设置编码格式
            fh = logging.FileHandler('../Result/log/{0}.log'.format(rq), encoding='utf-8')
            fh.setFormatter(formatter)
            logger.addHandler(fh)


        logger.error(message)
#             if type1=="error":
#                 logger.error(message)
#             else:
#                 logger.info(message)

if __name__ == '__main__':
#     get_log('hi')
#     get_log('hi too')
#     get_log('hi three')
#     logger.debug('阿斯蒂芬')
    get_log( "我是一般的log")
    get_log("error级别的log")
