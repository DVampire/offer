# -*- coding:utf-8 -*-
import time
'''
题目拓展3：矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？ 
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：循环
        考虑最左边，当竖着放是f（7）
        横着放，为f（6）
        所以f（8）=f（7）+f（6）
        '''
        number=args[0]
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        small, big = 1, 2

        for i in range(3, number + 1):
            sum_i = small + big
            small = big
            big = sum_i
        return big

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
    Solution().main(8)