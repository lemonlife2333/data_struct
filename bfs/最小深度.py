def min_depth(root):
    if not root:
        return 0
    # 初始化结果列表和深度
    res = [root]
    depth = 1

    while res:
        for i in range(len(res)):
            cur = res.pop()
            # 判断是否到达终点
            if not cur.left and not cur.right:
                return depth
            # 将相邻节点加入
            if cur.left:
                res.append(cur.left)
            if cur.right:
                res.append(cur.right)

        depth += 1

    return depth

# 在找最短路径的时候使用 BFS，其他时候还是 DFS 使用得多一些（主要是递归代码好写）。
