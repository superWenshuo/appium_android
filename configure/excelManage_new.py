# -*- coding:utf-8 -*-
from xlrd import sheet
import xlrd,time,os
from configure import diff, log2
from xlutils import copy
from configure import log,configure1
from configure.configure1 import configureApp
global log2
log2 = log2.Logger('all.log',level='debug')

def readExcel(file_path):  
    ''''' 
    读取excel测试用例的函数 
    :param file_path:传入一个excel文件，或者文件的绝对路径 
    :return:返回这个excel第一个sheet页中的所有测试用例的list 
    '''  
    try:  
        book = xlrd.open_workbook(file_path)#打开excel    

        #无需每次滑动开场动画
#         wd1.openApp()
#         wd1.clickByPoint()
    except :
        log2.logger.error('路径不在或者excel不正确')
#    
#     except Exception as e:  
# #         #如果路径不在或者excel不正确，返回报错信息 
# #         log2.Logger.error('路径不在或者excel不正确') 
#         print ('路径不在或者excel不正确',e)  
#         return e  
    else:  
        print ('进入读取excel')
        sheet = book.sheet_by_index(0)#取第一个sheet页  
        rows= sheet.nrows#取这个sheet页的所有行数  
        print ('进入读取excel,总共行数：',rows)
        case_list = []#保存每一条case  
        for i in range(rows):  
            if i !=0:  
                #把每一条测试用例添加到case_list中  
                case_list.append(sheet.row_values(i))
        p =os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
        excelPath=lambda x:os.path.join(p, "configure", x)

        interfaceTest(case_list,excelPath('DaoLend_case1.xlsx'))       

    
#根据点击，输入等方法操作
def get_action():
    #获得行为，如点击，输入
    mytype = str(action)
    mysql = str(sql)
    if 'send_key' in mytype and 'database' in mytype:
        #获取excel中的sql
        print('case 中包含数据库中的变量')
        print('sql语句：',mysql)
        data=configure1.configureApp().showMysqlDao(mysql)
#         print(configure.configure1.configureApp().showMysql(mytype))
        print(data.get('busi_priv'))

        return data.get('busi_priv')
    elif 'send_key' in mytype and 'database' not in mytype:
        print('不包含变量,send_key'+mytype[8:])
        return mytype[9:]

def interfaceTest(case_list,file_path): 
    #存测试结果的list
    global res_flags
    res_flags = []
    #实际结果
    global real_results
    real_results = [] 
    #获得driver
#     wd1=configure.configure1.configureApp().get_driver()
#     wd1=test.testrun.testRun().setUp()
    wd1 = configureApp().setup1().dr

    print(wd1)
    #存返回报文的list  
    for case in case_list: 
        try:  
            ''''' 
            这里捕捉一下异常，如果excel格式不正确的话，就返回异常 
            '''  
            #项目，模块  
            product = case[0]  
            #用例id，提bug的时候用  
            global case_id
            case_id = case[1]  
            #功能描述  
            global case_detail
            case_detail = case[2]  
            #元素定位方式  
            element_locate = case[3]  
            #元素定位器  
            global element
            element = case[4]  
            #行为  
            global  action
            action = case[5]  
            #数据库语句 
            global sql 
            sql = case[6]  
            #预期结果  
            res_check = case[7]  

        except Exception as e:  
            return '测试用例格式不正确！%s'%e 
        
        
        
        #引用实例化的driver,通过id定位元素，执行点击等方法         
        if 'click' in action:
#             wd1=configure.configure1.configureApp().get_driver()
#             wd1.wait_element(element)
#             configure.configure1.configureApp().wait_element(element)
            time.sleep(2)
             
            if element_locate=='id':
                #元素是否存在
                try:
                    if(wd1.dr.find_element_by_id(element).is_displayed() ==True):
                        wd1.dr.find_element_by_id(element).click();
                        res_flags.append('')
                        real_results.append('点击成功')
                except:
                    get_error()
#                     log.get_log('case id={0}的元素未找到,{1}出错'.format(case_id,case_detail))
                   
#                     configureApp().take_screen()
#                     res_flags.append('')
#                     real_results.append('未点击成功') 
                
               
            elif element_locate=='xpath':
                #使用try 判断元素是否存在，不存在log记录，并且截图
                try:
                    if(wd1.dr.find_element_by_xpath(element).is_displayed() ==True):
                        wd1.dr.find_element_by_xpath(element).click()
                        res_flags.append('')
                        real_results.append('点击成功')     
                except:
#                     log.get_log('{0}的元素未找到'.format(case_id))
                    get_error()
#                     log2.logger.error('case id{0}的元素未找到'.format(case_id))
#                     configure1.configureApp().take_screen()
#                     res_flags.append('')
#                     real_results.append('未点击成功')
                    
            elif element_locate=='class':
                try:
                    if(wd1.dr.find_element_by_class_name(element).is_displayed() ==True):
#                 configure1.configureApp().element_exist(wd1.dr.find_element_by_xpath(element))
                        wd1.dr.find_element_by_class_name(element).click();
                        res_flags.append('')
                        real_results.append('点击成功')
                except:
                    get_error()
#                     log.get_log('{0}的元素未找到'.format(case_id))
#                     configureApp().take_screen()
#                     res_flags.append('')
#                     real_results.append('未点击成功')

#             print(res_flags)
        #处理断言，getText：获得想要的内容
        if 'getText' in str(action):
            expected =res_check
            time.sleep(1)
            if element_locate=='id':
                realResult=wd1.dr.find_element_by_id(element).text
            if element_locate =='xpath':

                try:
                    if(wd1.dr.find_element_by_xpath(element).is_displayed() ==True):
                        realResult=wd1.dr.find_element_by_xpath(str(element)).text
                except:
                    log2.logger.error('case id={0}的元素未找到,{1}出错'.format(case_id,case_detail))
#                     log.get_log('{0}的元素未找到'.format(case_id))
                    configureApp().take_screen()
                    realResult=('case id={0}的元素未找到,{1}出错'.format(case_id,case_detail))
                
                
            diff.MyClass().equal(expected, realResult)
            print('我是期望结果:',expected,'我是实际值:',realResult)
            #判断text和期望是否相同，然后记录                  
            if diff.MyClass().equal(expected, realResult)=='success':
                print('期望结果=实际值')
                real_results.append(realResult)
                res_flags.append('一致')
            elif diff.MyClass().equal(expected, realResult)=='fail':
                print('不同')
                real_results.append(realResult)
                res_flags.append('不一致')
        #输入文字
        if 'send_key' in str(action): 
            time.sleep(3)
        #元素是否存在
            if element_locate=='id':
                try:
                    if(wd1.dr.find_element_by_id(element).is_displayed() ==True):
                        print(get_action())
                        wd1.dr.find_element_by_id(element).send_keys(get_action());
                    
                        real_results.append("输入成功")
                except:
                    get_error()
#                     log.get_log('{0}的元素未找到'.format(case_id))
#                     configureApp().take_screen() 

#                     real_results.append("输入失败")
            if element_locate=='xpath':
                try:
                    if(wd1.dr.find_element_by_xpath(element).is_displayed() ==True):
                        wd1.dr.find_element_by_xpath(element).send_keys(get_action());
                        real_results.append("输入成功")
                except:
                    get_error()
 #                     log.get_log('{0}的元素未找到'.format(case_id))
#                     configureApp().take_screen()
#                     real_results.append("输入失败")
            if element_locate=='class':   
                try:
                    if(wd1.dr.find_element_by_class_name(element).is_displayed() ==True):
                        print(get_action())
                        wd1.dr.find_element_by_class_name(element).send_keys(get_action());
                except:
                    get_error()
 #                     log.get_log('{0}的元素未找到'.format(case_id))
#                     configureApp().take_screen()
#                     real_results.append("输入失败")
            res_flags.append('')
          
    copy_excel(file_path,real_results,res_flags)    
                    
                    
def copy_excel(file_path,real_results,res_flags):  
    ''''' 
    :param file_path: 测试用例的路径 
    :param res_flags: 测试结果的list 
    :return: 
    '''  
    ''''' 
    这个函数的作用是写excel，把请求报文、返回报文和测试结果写到测试用例的excel中 
    因为xlrd模块只能读excel，不能写，所以用xlutils这个模块，但是python中没有一个模块能 
    直接操作已经写好的excel，所以只能用xlutils模块中的copy方法，copy一个新的excel，才能操作 
    '''  
    #打开原来的excel，获取到这个book对象  
    book = xlrd.open_workbook(file_path)  
    #复制一个new_book  
    new_book = copy.copy(book)  
    #然后获取到这个复制的excel的第一个sheet页  
    sheet = new_book.get_sheet(0)  
    i = 1
    for flag,real_result in zip(res_flags,real_results):  
        ''''' 
            同时遍历请求报文、返回报文和测试结果这3个大的list 
            然后把每一条case执行结果写到excel中，zip函数可以将多个list放在一起遍历 
            因为第一行是表头，所以从第二行开始写，也就是索引位1的位置，i代表行 
            所以i赋值为1，然后每写一条，然后i+1， i+=1同等于i=i+1 
            请求报文、返回报文、测试结果分别在excel的8、9、11列，列是固定的，所以就给写死了 
            后面跟上要写的值，因为excel用的是Unicode字符编码，所以前面带个u表示用Unicode编码 
            否则会有乱码 
        ''' 
        sheet.write(i,8,u'%s'%real_result) 
        sheet.write(i,9,u'%s'%flag) 
        i+=1     
        '''
                保存在excel的包下,p：当前路径的父包，
        os.path.join：进入当前路径的package
        format:
        '''
        p =os.path.abspath('..')
        excel_path=os.path.join(p, "Result")
        excel_path1=os.path.join(excel_path, "excel_result")
        print(excel_path1)    
        print('{}/{}_测试结果.xls'.format(excel_path1,time.strftime('%Y%m%d%H%M%S')))
        new_book.save('{}/{}_测试结果.xls'.format(excel_path1,time.strftime('%Y%m%d%H%M%S'))) 
 
def get_error():
    log2.logger.error('case id={0}的元素未找到,{1}出错'.format(case_id,case_detail))
    configure1.configureApp().take_screen()
    res_flags.append('')
    real_results.append('操作未成功')       