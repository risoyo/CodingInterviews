# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        self.deepth = []
        deep = 0
        self.search(pRoot, deep)
        self.deepth.sort()
        return self.deepth[-1]

    def search(self, pRoot, deep):
        deep += 1
        if pRoot.left is None and pRoot.right is None:
            self.deepth.append(deep)
            return
        if pRoot.left is not None:
            self.search(pRoot.left, deep)
        if pRoot.right is not None:
            self.search(pRoot.right, deep)


if __name__ == '__main__':
    bat = Solution()
    pre = [1, 2, 4, 5, 7, 3, 6]
    tin = [4, 2, 7, 5, 1, 3, 6]
    tree = bat.reConstructBinaryTree(pre, tin)
    print bat.TreeDepth(tree)
