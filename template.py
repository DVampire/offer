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
        tic=time.time()
        print(self.func1(*args, **kwargs))
        toc=time.time()
        print('func 1 time:%s ms'%(toc-tic))
        tic = time.time()
        print(self.func2(*args, **kwargs))
        toc = time.time()
        print('func 2 time:%s ms' % (toc - tic))

if __name__ == '__main__':
    Solution().main()