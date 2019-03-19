# -*- coding:utf-8 -*-
import time
'''
题目：
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：
        '''
        pass

    def func2(self, *args, **kwargs):
        '''
        思路二：
        '''
        pass

    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.clock()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.clock()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    Solution().main()