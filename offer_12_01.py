# -*- coding:utf-8 -*-
import time
'''

题目：矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
'''


class Solution(object):

    def func1(self, *args, **kwargs):
        '''
        思路一：回溯法，使用递归
        '''

        def hasPathCore(matrix, rows, cols, row, col, path, pathIndex, markmatrix):
            if pathIndex == len(path):
                return True
            hasPath = False
            if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[
                pathIndex] and not markmatrix[row * cols + col]:
                pathIndex += 1
                markmatrix[row * cols + col] = True
                hasPath = hasPathCore(matrix, rows, cols, row + 1, col, path, pathIndex, markmatrix) or \
                          hasPathCore(matrix, rows, cols, row - 1, col, path, pathIndex, markmatrix) or \
                          hasPathCore(matrix, rows, cols, row, col + 1, path, pathIndex, markmatrix) or \
                          hasPathCore(matrix, rows, cols, row, col - 1, path, pathIndex, markmatrix)
                if not hasPath:
                    pathIndex -= 1
                    markmatrix[row * cols + col] = False
            return hasPath

        matrix, rows, cols, path=args[0],args[1],args[2],args[3]

        if not matrix or rows < 0 or cols < 0 or path == None:
            return False
        markmatrix = [0] * (rows * cols)
        pathIndex = 0

        for row in range(rows):
            for col in range(cols):
                if hasPathCore(matrix, rows, cols, row, col, path, pathIndex, markmatrix):
                    return True
        return False

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
    matrix='abtgcfcsjdeh'
    rows=3
    cols=4

    Solution().main(matrix, rows, cols, 'bfce')
    Solution().main(matrix, rows, cols, 'abfb')