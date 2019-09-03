'''
Created on 2018年10月12日

@author: admin
'''
import unittest
class MyClass(unittest.TestCase):
    '''
    classdocs
    '''


    def __init__(self):
#     def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        pass
        
    def equal(self,expected,actual):  
        print('比对结果')
        try:  
            self._type_equality_funcs = {}
            self.assertEqual(expected,actual)
            return 'success' 
        except AssertionError as e:
            print(e)
            pass
#             raise
            return 'fail'   