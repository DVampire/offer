# -*- coding:utf-8 -*-
import time
'''
题目：用两个队列实现一个栈
'''

class CStack(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue1.insert(0, x)

    def pop(self):
        if not self.queue1:
            return None

        while len(self.queue1) != 1:
            self.queue2.insert(0, self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()

class Solution(object):

    def func1(self, *args, **kwargs):
        seq = args[0]
        ctr = args[1]
        queue=CStack()

        res=[]

        i=0
        for j in range(len(ctr)):
            if ctr[j]:
                queue.push(seq[i])
                i+=1
            else:
                res.append(queue.pop())
        return res

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
    seq=[1,2,3,4]
    ctr=[True,True,True,False,False,False,True,False]
    Solution().main(seq,ctr)