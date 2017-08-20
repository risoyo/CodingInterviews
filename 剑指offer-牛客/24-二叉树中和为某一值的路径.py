# -*- coding:utf-8 -*-
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    path_list = []
    path = []

    # 返回二维列表，内部每个列表表示找到的路径
    def ConstructBinaryTreeCore(self, pre, tin):
        root = TreeNode(pre[0])  # 用pre[0]将root初始化为节点,等同于root.val=pre[0],root.left=None,root.right=None
        ltin = tin[:tin.index(root.val)]  # 分割传入的中序排列,将其以root节点的值为界分割为2段,左边为左子树ltin,右边为右子树rtin
        rtin = tin[tin.index(root.val) + 1:]
        lpre = pre[1:len(ltin) + 1]  # 分割传入的前序排列,将其以root节点的值为界分割为2段,左边为左子树lpre,右边为右子树rpre
        if len(lpre) + 1 >= len(pre):  # 因为分割右子树的前序排列时,是用[x:]的方法截取前序排列字符串,所以要保证x的值小于前序排列的长度,若大于前序排列的长度,则证明右子树为空
            rpre = []
        else:
            rpre = pre[len(lpre) + 1:]
        if len(ltin) != 0 and len(lpre) != 0:  # 左子树的前序中序排列都非空时,左子树才存在,将其递归传入函数构建
            root.left = self.ConstructBinaryTreeCore(lpre, ltin)
        if len(rpre) != 0 and len(rtin) != 0:  # 同上
            root.right = self.ConstructBinaryTreeCore(rpre, rtin)
        return root  # 返回构建好的节点

    def reConstructBinaryTree(self, pre, tin):
        if pre == 0 or tin == 0:
            return False
        return self.ConstructBinaryTreeCore(pre, tin)

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if expectNumber == root.val and not root.left and not root.right:
            return [[root.val]]
        path = []
        path_left = self.FindPath(root.left,expectNumber-root.val)
        for i in path_left:
            if i:
                path.append([root.val]+i)
        path_right = self.FindPath(root.right,expectNumber-root.val)
        for i in path_right:
            if i:
                path.append([root.val]+i)
        return path


if __name__ == '__main__':
    bat = Solution()
    pre = [10, 5, 4, 7, 12]
    tin = [4, 5, 7, 10, 12]
    tree = bat.reConstructBinaryTree(pre, tin)
    expectNumber = 22
    print bat.FindPath(tree, expectNumber)
