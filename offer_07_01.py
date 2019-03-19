# -*- coding:utf-8 -*-
import time
'''

题目：重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：递归实现
        '''
        pre_seq = args[0]
        in_seq = args[1]

        if not pre_seq or not in_seq:
            return None

        root = TreeNode(pre_seq[0])
        val = in_seq.index(pre_seq[0])

        root.left = self.func1(pre_seq[1:val + 1], in_seq[:val])
        root.right = self.func1(pre_seq[val + 1:], in_seq[val + 1:])
        return root

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
    pre_seq=[1,2,4,7,3,5,6,8]
    in_seq=[4,7,2,1,5,3,8,6]

    Solution().main(pre_seq,in_seq)