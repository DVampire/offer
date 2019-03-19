# -*- coding:utf-8 -*-
import time
'''
题目拓展1：跳台阶(斐波那契数列)
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
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