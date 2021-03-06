# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        l = []
        if root is None:
            return l
        treelist = [root]
        while len(treelist) > 0:  # 队列非空时遍历就没有完成
            l.append(treelist[0].val)  # 输出队列最前端节点的值,加个','逗号后在console中输出的值就不会每个都跟着回车了
            if treelist[0].left is not None:  # 如果该节点有左子树,则将其加入队列
                treelist.append(treelist[0].left)
            if treelist[0].right is not None:  # 如果该节点有右子树,则将其加入队列
                treelist.append(treelist[0].right)
            del treelist[0]  # 将队列最前端的节点删除
        return l

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
    pre = [8, 6, 5, 7, 10, 9, 11]
    tin = [5, 6, 7, 8, 9, 10, 11]
    tree = bat.reConstructBinaryTree(pre, tin)
    print bat.PrintFromTopToBottom(tree)
