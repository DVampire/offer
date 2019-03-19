# -*- coding:utf-8 -*-
import time
import numpy as np
'''

题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
 n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：循环
        '''
        n=args[0]

        small = 0
        big = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1

        for i in range(2, n + 1):
            sum_i = small + big
            small = big
            big = sum_i
        return big

    def func2(self, *args, **kwargs):
        '''
        思路二：递归
        '''
        n=args[0]

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self.func2(n - 1) + self.func2(n - 2)

    def func3(self,*args,**kwargs):
        '''
        思路三：矩阵乘方
        '''
        n = args[0]

        if n <= 0:
            return 0
        elif n <= 2:
            return 1

        base=np.array([[1,1],[1,0]])
        res=base

        for i in range(n-2):
            res=np.dot(res,base)

        return res[0][0]

    def main(self, *args, **kwargs):
        tic=time.time()
        print(self.func1(*args, **kwargs))
        toc=time.time()
        print('func 1 time:%s ms'%(toc-tic))
        tic = time.time()
        print(self.func2(*args, **kwargs))
        toc = time.time()
        print('func 2 time:%s ms' % (toc - tic))
        tic = time.time()
        print(self.func3(*args, **kwargs))
        toc = time.time()
        print('func 3 time:%s ms' % (toc - tic))

if __name__ == '__main__':
    n=30
    Solution().main(n)