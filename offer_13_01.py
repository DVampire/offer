# -*- coding:utf-8 -*-
import time
'''

题目：机器人的运动范围
题：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：回溯法、递归
        '''

        def movingCountCore(threshold, rows, cols, row, col, markmatrix):
            value = 0
            if check(threshold, rows, cols, row, col, markmatrix):
                markmatrix[row * cols + col] = True
                value = 1 + movingCountCore(threshold, rows, cols, row - 1, col, markmatrix) + \
                        movingCountCore(threshold, rows, cols, row + 1, col, markmatrix) + \
                        movingCountCore(threshold, rows, cols, row, col - 1, markmatrix) + \
                        movingCountCore(threshold, rows, cols, row, col + 1, markmatrix)
            return value

        def check(threshold, rows, cols, row, col, markmatrix):
            if row >= 0 and row < rows and col >= 0 and col < cols and \
                    getDigitNum(row) + getDigitNum(col) <= threshold and not markmatrix[row * cols + col]:
                return True
            return False

        def getDigitNum(number):
            sum = 0
            while (number > 0):
                sum += number % 10
                number = number // 10
            return sum

        threshold, rows, cols=args[0],args[1],args[2]

        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        markmatrix = [False] * (rows * cols)
        count = movingCountCore(threshold, rows, cols, 0, 0, markmatrix)
        return count

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
    threshold=18
    rows=25
    cols=25
    Solution().main(threshold, rows, cols)