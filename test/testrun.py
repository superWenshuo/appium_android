#coding=utf-8  
import os
import configure.excelManage_new
import unittest


class testRun(unittest.TestCase):
    
 
#     def setUp(self):
#         try:
#             #获取当前路径的父路径
#             self.p =os.path.abspath('..')
#             #获取app路径
#             self.appPath =lambda x:os.path.join( self.p, "app", x)    
#             self.desired_caps = {}
#             self.desired_caps['platformName'] = 'Android'
#             self.desired_caps['platformVersion'] = '7.0'
#             self.desired_caps['automationName'] = 'uiautomator2'
#             self.desired_caps['deviceName'] = 'Android Emulator'
#             #app name
#             self.desired_caps['app'] =  self.appPath("app-release.apk")
#             self.desired_caps['appPackage'] = 'com.rn.DAOLEND'
#             self.desired_caps['appActivity'] = 'com.rn.DAOLEND.MainActivity'
#             self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
#              
#             self.dr = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
#             log.get_log("info","appium启动成功")
#         
# #             time.sleep(3)
#             return self
#              
#         except Exception as e:
#             raise e



    def run(self):
        #当前路径的父包
        p =os.path.abspath('..')
        print(p)
#         #获得当前路径
#         print(os.path.realpath(__file__))
#         #获得当前工作目录的上级路径
#         print(os.path.abspath('..'))     
        excelPath=lambda x:os.path.join(p, "configure", x)
        print(excelPath('DaoLend_case1.xlsx'))
        configure.excelManage_new.readExcel(excelPath('DaoLend_case1.xlsx'));


if __name__ == '__main__':
    testRun().run()

    

