# -*- coding:utf-8 -*-
'''

题目：二维数组中的查找
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution(object):

    def func1(self,*args,**kwargs):
        '''
        思路一：二层遍历，时间并不是最优
        '''
        nums=args[0]
        target=args[1]

        for row in nums:
            for col in row:
                if col==target:
                    return True
        else:
            return False

    def func2(self,*args,**kwargs):
        '''
        思路二：从右上角或者左下角开始。假如从右上角，如果右上角元素正好是target，则查找结束
        ；如果小于target，剔除这一行，继续重复；如果大于target，则剔除这一列，继续重复
        '''
        nums = args[0]
        target = args[1]

        m, n = len(nums), len(nums[0])
        row = 0
        col = n - 1
        while (row < m and col >= 0):
            if nums[row][col] < target:
                row += 1
            elif nums[row][col] > target:
                col -= 1
            else:
                return True
        return False

    def main(self,*args,**kwargs):
        print(self.func1(*args,**kwargs))
        print(self.func2(*args, **kwargs))


if __name__=='__main__':
    nums = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 7
    Solution().main(nums,target)