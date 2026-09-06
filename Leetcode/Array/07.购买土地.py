"""
在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，
代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市
区域的土地。现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。
然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且
每个子区域都必须包含一个或多个区块。为了确保公平竞争，你需要找到一种分配方式，
使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。

注意：区块不可再分。

【输入描述】

第一行输入两个正整数，代表 n 和 m。

接下来的 n 行，每行输出 m 个正整数。

输出描述

请输出一个整数，代表两个子区域内土地总价值之间的最小差距。

【输入示例】

3 3
1 2 3
2 1 3
1 2 3
【输出示例】

0

【提示信息】

如果将区域按照如下方式划分：

1 2 | 3
2 1 | 3
1 2 | 3
两个子区域内土地总价值之间的最小差距可以达到 0。

【数据范围】：

1 <= n, m <= 100；
n 和 m 不同时为 1。
"""
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(grid)

total = sum(sum(row) for row in grid)

ans = float('inf')

# 横向划分：在第 k 行下方切（k 从 0 到 n-2，即第 1~n-1 行之后）
row_sum = [sum(row) for row in grid]      # 每行之和
prefix = 0
for k in range(n - 1):
    prefix += row_sum[k]                  # 前 k+1 行之和（前缀和）
    ans = min(ans, abs(total - 2 * prefix))

# 纵向划分：在第 k 列右侧切
col_sum = [sum(grid[i][j] for i in range(n)) for j in range(m)]  # 每列之和
prefix = 0
for k in range(m - 1):
    prefix += col_sum[k]                  # 前 k+1 列之和（前缀和）
    ans = min(ans, abs(total - 2 * prefix))

print(ans)