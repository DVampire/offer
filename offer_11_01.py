# -*- coding:utf-8 -*-
import time
'''

题目：旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：二分查找，以及分情况考虑（稍显麻烦）详见
        当index1和index2和index_mid指向的数字都相同的时候，只能使用顺序查找了
        '''

        def minValue(nums, index1, index2):
            res = nums[index1]
            for i in range(index1 + 1, index2 + 1):
                if res > nums[i]:
                    res = nums[i]
            return res

        nums=args[0]

        if not nums:
            return
        if len(nums)==0:
            return 0

        index1=0
        index2=len(nums)-1
        index_mid=index1

        while(nums[index1]>=nums[index2]):
            if (index2-index1)==1:
                index_mid=index2
                break

            index_mid=(index1+index2)//2

            if nums[index1]==nums[index2] and nums[index_mid]==nums[index1]:
                return minValue(nums,index1,index2)

            if nums[index_mid]>=nums[index1]:
                index1=index_mid
            if nums[index_mid]<=nums[index2]:
                index2=index_mid

        return nums[index_mid]

    def func2(self, *args, **kwargs):
        '''
        思路二：
        '''
        pass

    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.clock()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.clock()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    nums=[3,4,5,6,7,8,9,1,1,2]
    Solution().main(nums)
    nums=[1,0,1,1,1,1]
    Solution().main(nums)