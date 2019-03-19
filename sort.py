# -*- coding:utf-8 -*-
import time
'''
题目：排序
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：冒泡排序(bubbleSort)
        思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
        平均时间复杂度：O(n^2)
        最好情况：O(n)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        稳定性：稳定
        '''
        nums=args[0]

        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j]>nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def func2(self, *args, **kwargs):
        '''
        思路二：选择排序（selectSort）
        工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        然后，再从剩余的未排序的元素中继续寻找最小（大）元素，
        然后放到已排序的末尾。直到所有元素均排序完毕。
        平均时间复杂度：O(n^2)
        最好情况：O(n^2)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        稳定性：不稳定
        '''
        nums = args[0]
        for i in range(len(nums) - 1):
            index = i
            for j in range(i + 1, len(nums)):
                if nums[index] > nums[j]:
                    index = j
            nums[i], nums[index] = nums[index], nums[i]

        return nums

    def func3(self, *args, **kwargs):
        '''
        思路三：插入排序（insertSort）
        工作原理：插入排序的主要思想是每次取一个列表元素与列表中已经排序好的列表段进行比较，
        然后插入从而得到新的排序好的列表段，最终获得排序好的列表。
        平均时间复杂度：O(n^2)
        最好情况：O(n)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        稳定性：稳定
        '''
        nums = args[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                temp = nums[i]  # 当前需要排序的元素
                index = i  # 用来记录排序元素需要插入的位置
                while index > 0 and nums[index - 1] > temp:
                    nums[index] = nums[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                    index -= 1
                nums[index] = temp  # 把需要排序的元素，插入到指定位置

        return nums

    def func4(self, *args, **kwargs):
        '''
        思路四：希尔排序（shellSort）
        工作原理：希尔排序(Shell Sort)是插入排序的一种。
        也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本,
        该方法的基本思想是：先将整个待排元素序列分割成若干个子序列
        （由相隔某个“增量”的元素组成的）分别进行直接插入排序，
        然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，
        再对全体元素进行一次直接插入排序。因为直接插入排序在元素基本有序的情况下（接近最好情况），
        效率是很高的，因此希尔排序在时间效率比直接插入排序有较大提高。
        平均时间复杂度：O(nlogn)
        最好情况：O(n^1.3)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        稳定性：不稳定
        '''
        nums = args[0]
        step = len(nums)//2
        while step > 0:
            for i in range(step, len(nums)):
                # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
                while i >= step and nums[i-step] > nums[i]:
                    nums[i], nums[i-step] = nums[i-step], nums[i]
                    i -= step
            step = step//2
        return nums

    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.time()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.time()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    nums=[4,6,3,1,5,8,7,9,0,2]
    Solution().main(nums)