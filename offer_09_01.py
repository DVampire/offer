# -*- coding:utf-8 -*-
import time
'''
题目：用两个栈实现队列
题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class CQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    '''
    解题思路：有两个栈stackA,stackB，A为入栈，B为出栈的。
    入栈时，直接进入A即可，出栈时，先判断B中是否有元素，
    如果没有肯定不能pop()，应将A中所有元素倒压在B里面，
    再pop()最上面（后面）的元素，如果有，直接pop()就可以了。
    两个栈各自先进后出，在一起又实现了队列的先进先出。
    '''
    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()

        elif not self.stack1:
            return None

        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

class Solution(object):

    def func1(self, *args, **kwargs):
        seq = args[0]
        ctr = args[1]
        queue=CQueue()

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
    seq=[4,2,1,3]
    ctr=[True,True,True,False,False,False,True,False]
    Solution().main(seq,ctr)