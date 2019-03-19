# -*- coding:utf-8 -*-

'''

题：数组中重复的数字
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
'''

class Solution(object):

    '''思路一：先把输入数组排序，然后从排序后的数组中从前往后找。'''
    def duplicate1(self,nums):
        if nums == None or len(nums) <= 1:
            return False
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums) - 1:
                return False

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True,nums[i]
        return False

    '''思路二：使用辅助空间:哈希表。时间复杂度为O(n)，空间复杂度为O(n)'''
    def duplicate2(self,nums):
        if nums == None or len(nums) <= 1:
            return False
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums) - 1:
                return False

        usedDic = set()  # 集合
        for i in range(len(nums)):
            if nums[i] not in usedDic:
                usedDic.add(nums[i])
            else:
                return True,nums[i]
        return False

    '''
    解题思路三：重排数组：从头到尾扫描数组的每个数字，当扫描到下标为i的数字时，
    首先比较这个数字（假设为m）是否等于i,如果是，接着扫描下一个数字；
    如果不是，那么再将它和下标为m的数字对比，如果两者不相等，就把它和第m个数字交换，
    把m放到属于它的位置，如果两者相等，那么就找到了一个重复的数字。重复这个过程，
    直到发现一个重复的数字。

    解题代码：(根据代码分析复杂度：所有操作都在输入数组上进行，不需要额外分配空间，
    因此空间复杂度为O(1);尽管代码中有一个两重循环，
    但是每个数字最多只要交换两次就能找到它自己的位置，因为总的时间复杂度为O(n))
    '''

    def duplicate3(self, nums):
        if nums == None or len(nums) <= 1:
            return False

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums) - 1:
                return False

        for i in range(len(nums)):
            while (nums[i] != i):
                if nums[i] == nums[nums[i]]:
                    return True,nums[i]
                else:
                    nums[i],nums[nums[i]]=nums[nums[i]],nums[i]
        return False

    def main(self,nums):
        print(self.duplicate1(nums))
        print(self.duplicate2(nums))
        print(self.duplicate3(nums))

if __name__=='__main__':
    nums=[2,3,1,0,2,5,3]
    Solution().main(nums)