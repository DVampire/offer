# -*- coding:utf-8 -*-
import time
import numpy as np
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

    def func5(self, *args, **kwargs):
        '''
        思路五：归并排序(mergeSort)
        思想: 基本过程：假设初始序列含有n个记录，则可以看成是n个有序的子序列，每个子序列的长度为1，
        然后两两归并，得到n/2个长度为2或1的有序子序列，再两两归并，最终得到一个长度为n的有序序列为止，
        这称为2路归并排序。
        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(nlogn)
        空间复杂度：O(n)
        稳定性：稳定
        '''

        def merge(left, right):
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):  # 比较传入的两个子序列，对两个子序列进行排序
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])  # 将排好序的子序列合并
            result.extend(right[j:])
            return result

        nums=args[0]

        if len(nums) <= 1:
            return nums  # 从递归中返回长度为1的序列

        middle = len(nums) // 2
        left = self.func5(nums[:middle])  # 通过不断递归，将原始序列拆分成n个小序列
        right = self.func5(nums[middle:])
        return merge(left, right)

    def func6(self, *args, **kwargs):
        '''
        思路六：快速排序(quickSort)
        思想: 首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
        一趟快速排序的算法是：
        1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
        2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
        3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
        4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
        5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，
        使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。
        另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。
        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(n^2)
        空间复杂度：O(logn)
        稳定性：不稳定
        '''
        def sub_sort(array, low, high):
            key = array[low]
            while low < high:
                while low < high and array[high] >= key:
                    high -= 1
                while low < high and array[high] < key:
                    array[low] = array[high]
                    low += 1
                    array[high] = array[low]
            array[low] = key
            return low

        def quick_sort(array, low, high):
            if low < high:
                key_index = sub_sort(array, low, high)
                quick_sort(array, low, key_index)
                quick_sort(array, key_index + 1, high)

        nums = args[0]
        quick_sort(nums,0,len(nums)-1)

        return nums

    def func7(self, *args, **kwargs):
        '''
        思路七：堆排序(heapSort)
        1.从len(L)/2 到1开始，建立大根堆。这里需要注意的是：这里的元素并不是一次就能移动到最终的位置的。只有迭代到第一个元素，才能建立一个大根堆。
        2.将堆顶元素与无序区最后一个元素交换位置，破坏了大根堆，则重新建立大根堆。
        3.迭代第二步，直到只剩下一个元素。

        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(nlogn)
        空间复杂度：O(1)
        稳定性：不稳定
        '''

        def heap_adjust(L, start, end):
            temp = L[start]

            i = start
            j = 2 * i

            while j <= end:
                if (j < end) and (L[j] < L[j + 1]):
                    j += 1
                if temp < L[j]:
                    L[i] = L[j]
                    i = j
                    j = 2 * i
                else:
                    break
            L[i] = temp

        def swap_param(L, i, j):
            L[i], L[j] = L[j], L[i]
            return L

        nums=args[0]
        length = len(nums) - 1

        first_sort_count = length // 2
        for i in range(first_sort_count):
            heap_adjust(nums, first_sort_count - i, length)

        for i in range(length - 1):
            nums = swap_param(nums, 1, length - i)
            heap_adjust(nums, 1, length - i - 1)

        return nums

    def func8(self, *args, **kwargs):
        '''
        思路八：计数排序(countSort)
        思想: 统计每个数比列表其他数大于的次数, 次数越多说明, 这个数越大,
        反之, 大于的次数越少, 说明这个数就越小
        平均时间复杂度：O(n+k)
        最好情况：O(n+k)
        最坏情况：O(n+k)
        空间复杂度：O(k)
        稳定性：稳定
        '''
        nums=args[0]

        n = len(nums)
        res = [None] * n

        # 首次循环遍历, 每个列表的数都统计
        for i in range(n):
            # p 表示 a[i] 大于列表其他数 的次数
            p = 0
            # q 表示 等于 a[i] 的次数
            q = 0
            # 二次循环遍历, 列表中的每个数都和首次循环的数比较
            for j in range(n):
                if nums[i] > nums[j]:
                    p += 1
                elif nums[i] == nums[j]:
                    q += 1
            for k in range(p, p + q):  # q表示 相等的次数,就表示, 从 P 开始索引后, 连续 q 次,都是同样的 数
                res[k] = nums[i]
        return res

    def func9(self, *args, **kwargs):
        '''
        思路九：桶排序(bucketSort)
        思想: 如果有一个数组A，包含N个整数，值从1到M，我们可以得到一种非常快速的排序，桶排序（bucket sort）。
        留置一个数组S，里面含有M个桶，初始化为0。然后遍历数组A，
        读入Ai时，S[Ai]增一。所有输入被读进后，扫描数组S得出排好序的表。该算法时间花费O(M+N)，空间上不能原地排序。
        平均时间复杂度：O(n+k)
        最好情况：O(n+k)
        最坏情况：O(n^2)
        空间复杂度：O(n+k)
        稳定性：稳定
        '''
        nums=args[0]

        # 选择一个最大的数
        max_num = max(nums)
        # 创建一个元素全是0的列表, 当做桶
        bucket = [0] * (max_num + 1)
        # 把所有元素放入桶中, 即把对应元素个数加一
        for i in nums:
            bucket[i] += 1

        # 存储排序好的元素
        sort_nums = []
        # 取出桶中的元素
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(bucket[j]):
                    sort_nums.append(j)

        return sort_nums

    def func10(self, *args, **kwargs):
        '''
        思路十：基数排序(radixSort)
        思想: 基数排序一般用于长度相同的元素组成的数组。首先按照最低有效数字进行排序，然后由低位向高位进行。
        基数排序可以看做是进行多趟桶排序。每个有效数字都在0-9之间，很适合桶排序，建10个桶很方便。
        平均时间复杂度：O(n*k)
        最好情况：O(n*k)
        最坏情况：O(n*k)
        空间复杂度：O(n+k)
        稳定性：稳定
        '''
        nums=args[0]

        i = 0  # 初始为个位排序
        n = 1  # 最小的位数置为1（包含0）
        max = np.max(nums)  # 得到带排序数组中最大数
        while max / (10 ** n) > 0:  # 得到最大数是几位数
            n += 1

        while i < n:
            bucket = {}  # 用字典构建桶
            for x in range(0, 10):
                bucket.setdefault(x, [])  # 将每个桶置空
            for x in nums:  # 对每一位进行排序
                radix = (x // (10 ** i)) % 10  # 得到每位的基数
                bucket[radix].append(x)  # 将对应的数组元素加入到相应位基数的桶中
            j = 0
            for k in range(0, 10):
                if len(bucket[k]) != 0:  # 若桶不为空
                    for y in bucket[k]:  # 将该桶中每个元素
                        nums[j] = y  # 放回到数组中
                        j += 1
            i += 1

        return nums

    def main(self, *args, **kwargs):
        func_list=[i for i in self.__dir__() if 'func' in i]

        for func in func_list:
            tic=time.clock()
            print(getattr(self,func)(*args,**kwargs))
            toc=time.clock()
            print('%s time:%s ms'%(func,toc-tic))

if __name__ == '__main__':
    nums=[4,6,3,1,5,8,7,9,0,2]
    Solution().main(nums)