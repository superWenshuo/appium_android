# -*- coding:utf-8 -*-
from appium import webdriver
import os,time,pymysql
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
class configureApp(object):
    '''需要定义全局变量的放在这里，最好定义一个初始值'''
#     setup1(self).dr
#     driver=testrun.testRun().setUp().dr

#     @classmethod
    def setup1(self):
        try:
            #获取当前路径的父路径
            global driver
            
            self.p =os.path.abspath('..')
            #获取app路径
            self.appPath =lambda x:os.path.join( self.p, "app", x)    
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '7.0'
            self.desired_caps['automationName'] = 'uiautomator2'
            self.desired_caps['deviceName'] = 'Android Emulator'
            #app name
            self.desired_caps['app'] =  self.appPath("app-release.apk")
            self.desired_caps['appPackage'] = 'com.rn.DAOLEND'
            self.desired_caps['appActivity'] = 'com.rn.DAOLEND.MainActivity'
            self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
             
            self.dr = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
#             log.get_log("appium启动成功")
            driver=self
            return self
             
        except Exception as e:
            raise e

    def getDrive(self):
        return self.dr


        #获得屏幕大小
    def getSize(self):
 
        x = self.dr.get_window_size()['width']
        y = self.dr.get_window_size()['height']
        print(x,y)
        return (x, y)
        #屏幕左滑动
    def swipLeft(self,t):
        l=self.getSize()

        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print(x1,y1,x2)
        #     dr = self.webdriver.Remote
        print('左滑动')
        self.dr.swipe(x1,y1,x2,y1,t)
        #根据相对坐标点击
    def clickByPoint(self):
#设定系数，a=X坐标/调试屏幕宽度，b=y坐标/调试时屏幕宽度
        a = 1296.0/1440
        b = 2735.0/2768
        x =  self.dr.get_window_size()['width']
        y =  self.dr.get_window_size()['height']
        x1 = int(x*a)
        y1 = int(y*b)
        self.dr.swipe(x1, y1, x1, y1,1) 
        #读取区块链数据库验证码
    def showMysqlDao(self,sql_in):
        sql=sql_in
        # 连接MySQL数据库
        connection = pymysql.connect(host='192.168.10.84', port=23307, user='xz_dev', password='xz_739', db='blockchainnew_dev', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 执行数据查询  
        cursor.execute(sql)
        #查询数据库单条数据
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        print(result)
        return result
        #读取数据库1验证码
    def showMysql(self,sql_in):
        sql=sql_in
        # 连接MySQL数据库
        connection = pymysql.connect(host='192.168.10.84', port=23307, user='xz_beta', password='xz_739', db='current_beta', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 执行数据查询  
        cursor.execute(sql)
        #查询数据库单条数据
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        print(result)
        return result
    #等待元素出现
    def wait_element(self,element):
        WebDriverWait(self.dr,10).until(expected_conditions.visibility_of_element_located(element))


    # 截图
    def take_screen(self):
        p =os.path.abspath('..')
        img_path=os.path.join(p, "Result")
        img_path1=os.path.join(img_path, "screen/")
        print(img_path1)
        print('{}/{}_测试结果.png'.format(img_path1,time.strftime('%Y%m%d%H%M%S')))
        screen_save_path = '{}/{}_测试结果.png'.format(img_path1,time.strftime('%Y%m%d%H%M%S'))
        driver.dr.get_screenshot_as_file(screen_save_path)



