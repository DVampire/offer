'''

拓展：不修改数组找出重复的数字。
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，
但不能修改输入的数组，例如输入长度为8的数组[2,3,5,4,3,2,6,7]，那么对应的输出是重复的数字为2或3。
'''

class Solution(object):

    '''思路一：利用哈希表，时间复杂度O(n)，空间复杂度O(n)'''
    def duplicate1(self,nums):
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
    思路二：二分查找的变形，如下，时间复杂度O(nlogn)，空间复杂度为O(1)
    '''
    def duplicate2(self, nums):
        if not nums or len(nums) <= 0:
            return False

        start = 1
        end = len(nums) - 1

        while start <= end:
            middle = (end - start) // 2 + start
            count = self.countRange(nums, len(nums), start, middle)
            if end == start:
                if count > 1:
                    return True,start
                else:
                    break
            if count > middle - start + 1:
                end = middle
            else:
                start = middle + 1
        return False

    def countRange(self, numbers, length, start, end):
        '''
        计算数组中的元素大于等于start，小于等于end的元素的个数
        '''
        if not numbers:
            return 0
        count = 0
        for i in range(length):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1
        return count

    def main(self,nums):
        print(self.duplicate1(nums))
        print(self.duplicate2(nums))

if __name__=='__main__':
    nums=[2,3,5,4,3,2,6,7]
    Solution().main(nums)