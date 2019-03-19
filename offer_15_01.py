# -*- coding:utf-8 -*-
import time
'''
题目：二进制中1的个数
题：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        解题思路一：
        最佳方法：把一个整数减去1，再和原整数做“与运算”，会把该整数最右边的1变成0。
        那么一个整数的二进制中表示中有多少个1，就可以进行多少次这样的操作。
        '''
        n=args[0]

        count = 0

        if n < 0:
            n = n & 0xffffffff

        while (n):
            n= (n - 1) & n
            count += 1
        return count


    def func2(self, *args, **kwargs):
        '''
        思路二：利用Python特性
        '''
        n = args[0]
        return bin(n & 0xffffffff).count("1")

    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.clock()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.clock()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    Solution().main(100)
    Solution().main(-100)