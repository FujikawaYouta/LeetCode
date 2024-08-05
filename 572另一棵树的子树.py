# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 如果两棵树相同，说明他们从根节点开始就相同
        # 从根节点如何遍历可以证明他们相同？
        # dfs同步执行匹配
        def preOrder(cur_root, sub_root):
            if cur_root.val != sub_root.val:
                return False
            if cur_root.left != None and sub_root.left != None:
                if preOrder(cur_root.left, sub_root.left) == False:
                    return False
            elif cur_root.left != None or sub_root.left != None:
                return False
            if cur_root.right != None and sub_root.right != None:
                if preOrder(cur_root.right, sub_root.right) == False:
                    return False
            elif cur_root.right != None or sub_root.right != None:
                return False
            return True
        def bfs(root, target):
            ans = []
            queue = [root]
            while len(queue):
                cur_root = queue.pop(0)
                if cur_root.val == target:
                    ans.append(cur_root)
                if cur_root.left != None:
                    queue.append(cur_root.left)
                if cur_root.right != None:
                    queue.append(cur_root.right)
            return ans
                
        # 先遍历root找到和subRoot值相同的 节点
        target = subRoot.val
        cur_roots = bfs(root, target)
        for cur_root in cur_roots:
            if preOrder(cur_root, subRoot)==True:
                return True
        return False

def treeGenerator(nodes: list) -> TreeNode:
    if len(nodes)==0:
        return None
    first_node = TreeNode(val=nodes[0])
    queue = [first_node]
    n = len(nodes)
    for i in range(1,n):
        cur_root = queue[0]
        queue.append(TreeNode(nodes[i]))
        if cur_root.left == None:
            cur_root.left = queue[-1]
        elif cur_root.right == None:
            cur_root.right = queue[-1]
        else:
            queue.pop(0)
            queue[0].left = queue[-1]
    return first_node
        

if __name__ == '__main__':
    sol = Solution()
    root = treeGenerator(nodes=[3,4,5,1,2])
    subRoot = treeGenerator(nodes=[4,1,2])
    print(sol.isSubtree(root, subRoot))
    