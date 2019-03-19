# -*- coding:utf-8 -*-
import time
'''

题目：二叉树的下一个节点
题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class TreeParNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.par = None

class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：
        '''
        cur=args[0]

        if not root:
            return

        # 如果该节点有右子树，那么下一个节点就是它右子树中的最左节点
        elif cur.right != None:
            cur = cur.right
            while cur.left != None:
                cur = cur.left
            return cur.val

        # 如果一个节点没有右子树，并且它还是它父节点的右子节点。那么一直向上找，直到找到一个节点是它父节点的左子节点，这个节点的父节点就是下一个节点
        elif cur.par != None and cur.par.right == cur:
            while cur.par != None and cur.par.left != cur:
                cur = cur.par
            return cur.par.val
        # 如果一个节点是它父节点的左子节点，那么直接返回它的父节点
        else:
            return cur.par.val

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

    root=TreeParNode('a')
    b=TreeParNode('b')
    c=TreeParNode('c')
    root.left=b
    root.right=c
    b.par=root
    c.par=root

    d=TreeParNode('b')
    e=TreeParNode('e')
    d.par=b
    e.par=b
    b.left=b
    b.right=e

    h=TreeParNode('h')
    i=TreeParNode('i')
    h.par=e
    i.par=e
    e.left=h
    e.right=i

    f = TreeParNode('f')
    g = TreeParNode('g')
    f.par=c
    g.par=c
    c.left=f
    c.right=g

    Solution().main(i)