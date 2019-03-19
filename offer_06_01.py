# -*- coding:utf-8 -*-
import time
'''

题目：从尾到头打印链表
输入一个链表，从尾到头打印链表每个节点的值。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：使用栈实现
        '''
        if not args[0]:
            return []

        res=[]
        p=args[0]
        while p:
            res.append(p.val)
            p=p.next
        return res[::-1]

    def main(self, *args, **kwargs):
        tic=time.time()
        print(self.func1(*args, **kwargs))
        toc=time.time()
        print('func 1 time:%s ms'%(toc-tic))

if __name__ == '__main__':
    p=head=ListNode(0)
    for i in range(1,10):
        tmp=ListNode(i)
        p.next=tmp
        p=p.next
    p.next=None

    Solution().main(head)