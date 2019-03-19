# -*- coding:utf-8 -*-
import time
'''
题目：剪绳子
题：给你一根长度为n的绳子，请把绳子剪成m段(m,n都是整数，且n>1,m>1),
每段绳子的长度记为k[0],k[1],k[2],...,k[m]。请问k[0]*k[1]*...*k[m]
可能的最大乘积是多少？例如，当绳子的长度为8时，
我们把它剪成长度分别为2，3，3的三段，此时得到的最大乘积为18。
'''

class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：基于动态规划
        '''
        n=args[0]

        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        products = [0] * (n + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max:
                    max = product
            products[i] = max

        return products[n]

    def func2(self, *args, **kwargs):
        '''
        思路二：贪婪算法
        当剩下的绳子长度大于等于5的时候，尽量剪出长度为3的段，
        当剩下的长度为4的时候，绳子剪成2*2的两段。
        '''
        n=args[0]

        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        timesOf3 = n // 3

        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timesOf2 = (n - timesOf3 * 3) // 2

        return (3 ** timesOf3) * (2 ** timesOf2)


    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.clock()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.clock()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    n=8
    Solution().main(n)