# -*- coding:utf-8 -*-
# row 行
# col 列
class Solution:
    # matrix类型为二维列表，需要返回列表
    def print_number(self, num):
        print '%d,' % num

    # def printMatrixCircle(self, matrix, start):
    #     matrixX = len(matrix[0]) - start
    #     matrixY = len(matrix) - start
    #     for i in range(start, matrixX):
    #         self.print_number(matrix[start][i])
    #        # print matrix[start][i],
    #     for i in range(start + 1, matrixY):
    #         print matrix[i][matrixX - 1],
    #     for i in range(matrixX - 2, start - 1, -1):
    #         print matrix[matrixY - 1][i],
    #     for i in range(matrixY - 2, start, -1):
    #         print matrix[i][start],
    #
    #     return

    def printMatrix(self, matrix):
        result = []
        if len(matrix) == 0 or matrix is None:
            return
        start = 0
        while len(matrix) > start * 2 and len(matrix[0]) > start * 2:
            matrixX = len(matrix[0]) - start
            matrixY = len(matrix) - start
            for i in range(start, matrixX):
                result.append(matrix[start][i])
                # self.print_number(matrix[start][i])
                # print matrix[start][i],
            for i in range(start + 1, matrixY):
                result.append(matrix[i][matrixX - 1])
                # print matrix[i][matrixX - 1],
            if start < matrixX - 1 and start < matrixY - 1:
                for i in range(matrixX - 2, start - 1, -1):
                    result.append(matrix[matrixY - 1][i])
                    # print matrix[matrixY - 1][i],
            if start < matrixX - 1 and start < matrixY - 2:
                for i in range(matrixY - 2, start, -1):
                    result.append(matrix[i][start])
                    # print matrix[i][start],
            start += 1
        return result


if __name__ == '__main__':
    bat = Solution()
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix2 = [[1]]
    matrix3 = [[1], [2], [3], [4], [5]]
    matrix4 = [[1, 2, 3, 4, 5]]
    result = bat.printMatrix(matrix4)
    print result
