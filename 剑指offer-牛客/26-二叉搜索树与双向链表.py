# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while (left.right):
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while (right.left):
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        while (pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

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

    def min_order(self, tree):  # 中序遍历二叉树
        if tree is not None:
            self.min_order(tree.left)
            print tree.val,
            self.min_order(tree.right)


if __name__ == '__main__':
    bat = Solution()
    pre = [10, 6, 4, 8, 14, 12, 16]
    tin = [4, 6, 8, 10, 12, 14, 16]
    tree = bat.reConstructBinaryTree(pre, tin)
    bat.Convert(tree)
