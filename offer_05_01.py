# -*- coding:utf-8 -*-
import time
'''
题目：替换空格
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：先分割，再合并
        '''
        return '%20'.join(args[0].split())

    def func2(self, *args, **kwargs):
        '''
        思路二：直接替换
        '''
        return args[0].replace(' ','%20')

    def func3(self, *args, **kwargs):
        '''
        思路三：
        ①先计算源字符串数组长度，并统计空格数量
        ②新字符串数组长度=源数组长度+2*空格数量
        ③在新字符串数组上，从后向前遍历，通过两个index移动并复制。
        '''
        str=args[0]
        str = list(str)

        count=0
        for i in str:
            if i==' ':
                count+=1
        p1=len(str)-1

        str.extend([None]*(count*2))
        p2=len(str)-1

        while p1>=0:
            if str[p1]==' ':
                for i in ['0', '2', '%']:
                    str[p2] = i
                    p2 -= 1
            else:
                str[p2] = str[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(str)

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
    str='We Are Happy'
    Solution().main(str)