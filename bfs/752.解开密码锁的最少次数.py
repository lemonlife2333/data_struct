# 向上进一步
def plus_one(s, j):
    if s[j] == '9':
        s[j] = '0'
    else:
        s[j] = str(int(s[j])+1)
    return s

# 向下进一步


def minus_one(s, j):
    if s[j] == '0':
        s[j] = '9'
    else:
        s[j] = str(int(s[j])-1)

    return s


def bfs(deadends, target):
    dead = ()
    # 将终止条件放入一个元组中，去重
    for s in deadends:
        dead += (s)
    # 初始化起点、已访问点和步数
    visited = ('0000')
    q = ['0000']
    step = 0

    while q:
        size = len(q)
        for i in range(size):
            cur = q.pop()

            if cur in dead:
                continue
            if cur == target:
                return step
            # 遍历加减的策略
            for j in range(4):

                up = plus_one(cur, j)
                # 跳过已访问点
                if up not in visited:
                    q.append(up)
                    visited += (up)
                down = minus_one(cur, j)
                # 跳过已访问点
                if down not in visited:
                    q.append(down)
                    visited += (down)
        # 步数+1
        step += 1

    return step


