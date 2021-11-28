# -*- coding = utf-8 -*-
# 谢光耀

""" -----------------------        策略是针对rollout的优化           ---------------------"""

from random import choice

"""----------------------------  N 个 棋子连成一排的返回下一步的move  for AI  ------------"""
"""----------------------------  1 for AI,   2 for Human  -----------------------------"""
diag_1 = [i for i in range(0, 64, 9)]  # 左斜向上
diag_2 = [i for i in range(7, 57, 7)]  # 右斜向上


def NN_in_row(Availables, Player, Node):
    moved = list(set(range(64)) - set(Availables))
    for m in moved:
        row = m // 8
        col = m % 8

        """---------------------- 4 个 棋子连成一排---------------"""
        '''---------------------  AI 选择自己的最优解--------------'''
        if (Player, Node[m]) == (1, 1):
            if col in range(5) and len(set(Node[i] for i in range(m, m + 4))) == 1:  # ( m, m +1, m+2, m+3 )
                if 0 < col and Node[m - 1] == 0:
                    return m - 1
                if col < 4 and Node[m + 4] == 0:
                    return m + 4

            if row in range(5) and len(set(Node[i] for i in range(m, m + 32, 8))) == 1:  # ( m, m+8, m+16, m+24 )
                if 0 < row and Node[m - 8] == 0:
                    return m - 8
                if row < 4 and Node[m + 32] == 0:
                    return m + 32

            if m in diag_1 and col in range(5) and len(
                    set(Node[i] for i in range(m, 36, 9))) == 1:  # ( m, m+9, m+18, m+27 )
                if 0 < row and Node[m - 9] == 0:
                    return m - 9
                if row < 4 and Node[m + 36] == 0:
                    return m + 36

            if m in diag_2 and row in range(5) and len(
                    set(Node[i] for i in range(m, 28, 7))) == 1:  # ( m, m+7, m+14, m+21 )
                if 0 < row and Node[m - 7] == 0:
                    return m - 7
                if row < 4 and Node[m + 28] == 0:
                    return m + 28

        """------------------------    AI 进行 block （  默认对手不是很智能，四个连成一排时不会下第五个  ）------------------------"""
        if (Player, Node[m]) == (1, -1):
            if col in range(5) and len(set(Node[i] for i in range(m, m + 4))) == 1:  # ( m, m +1, m+2, m+3 )
                if 0 < col and Node[m - 1] == 0:
                    return m - 1
                if col < 4 and Node[m + 4] == 0:
                    return m + 4

            if row in range(5) and len(set(Node[i] for i in range(m, m + 32, 8))) == 1:  # ( m, m+8, m+16, m+24 )
                if 0 < row and Node[m - 8] == 0:
                    return m - 8
                if row < 4 and Node[m + 32] == 0:
                    return m + 32

            if m in diag_1 and col in range(5) and len(
                    set(Node[i] for i in range(m, 36, 9))) == 1:  # ( m, m+9, m+18, m+27 )
                if 0 < row and Node[m - 9] == 0:
                    return m - 9
                if row < 4 and Node[m + 36] == 0:
                    return m + 36

            if m in diag_2 and row in range(5) and len(
                    set(Node[i] for i in range(m, 28, 7))) == 1:  # ( m, m+7, m+14, m+21 )
                if 0 < row and Node[m - 7] == 0:
                    return m - 7
                if row < 4 and Node[m + 28] == 0:
                    return m + 28

        """---------------------- 3 个棋子连成一排---------------------"""
        '''----------------------- AI 选择自己的最优解------------------'''
        if (Player, Node[m]) == (1, 1):  # 有三个连成一排的时候， 先判断是否两边有 两个空位， 一端有两个空位则优先选择
            if col in range(1, 5) and len(set(Node[i] for i in range(m, m + 3))) == 1:  # ( m, m + 1, m + 2 )
                if 1 < col and Node[m - 1] == 0 and Node[m - 2] == 0 and Node[m + 3] == 0:
                    return m - 1
                if col < 4 and Node[m - 1] == 0 and Node[m + 3] == 0 and Node[m + 4] == 0:
                    return m + 3
                if (Node[m - 1], Node[m + 3]) == (0, 0):
                    return choice([m - 1, m + 3])

            if row in range(1, 5) and len(set(Node[i] for i in range(m, m + 24, 8))) == 1:  # ( m, m + 8, m + 16 )
                if 1 < row and Node[m - 8] == 0 and Node[m - 16] == 0 and Node[m + 24] == 0:
                    return m - 8
                if row < 4 and Node[m - 8] == 0 and Node[m + 24] == 0 and Node[m + 32] == 0:
                    return m + 32
                if (Node[m - 8], Node[m + 24]) == (0, 0):
                    return choice([m - 8, m + 24])

            if m in diag_1 and col in range(1, 5) and len(
                    set(Node[i] for i in range(m, m + 27, 9))) == 1:  # ( m, m + 9, m + 18 )
                if 1 < row and Node[m - 9] == 0 and Node[m - 18] == 0 and Node[m + 27] == 0:
                    return m - 9
                if row < 4 and Node[m - 9] == 0 and Node[m + 27] == 0 and Node[m + 36] == 0:
                    return m + 27
                if (Node[m - 9], Node[m + 27]) == (0, 0):
                    return choice([m - 9, m + 27])

            if m in diag_2 and row in range(1, 5) and len(
                    set(Node[i] for i in range(m, m + 21, 7))) == 1:  # (m, m + 7, m + 14 )
                if 1 < row and Node[m - 7] == 0 and Node[m - 14] == 0 and Node[m + 21] == 0:
                    return m - 7
                if row < 4 and Node[m - 7] == 0 and Node[m + 21] == 0 and Node[m + 28] == 0:
                    return m + 21
                if (Node[m - 7], Node[m + 21]) == (0, 0):
                    return choice([m - 7, m + 21])

        """-------------------- AI 选择 block 对手方的棋子--------------------------"""
        """-------------------- 只有在 一端出现 两个空位置的时候会进行 block ------------------"""
        if (Player, Node[m]) == (1, -1):
            if col in range(1, 5) and len(set(Node[i] for i in range(m, m + 3))) == 1:  # ( m, m + 1, m + 2 )
                if 1 < col and Node[m - 1] == 0 and Node[m - 2] == 0 and Node[m + 3] == 0:
                    return m - 1
                if col < 4 and Node[m - 1] == 0 and Node[m + 3] == 0 and Node[m + 4] == 0:
                    return m + 3

            if row in range(1, 5) and len(set(Node[i] for i in range(m, m + 24, 8))) == 1:  # ( m, m + 8, m + 16 )
                if 1 < row and Node[m - 8] == 0 and Node[m - 16] == 0 and Node[m + 24] == 0:
                    return m - 8
                if row < 4 and Node[m - 8] == 0 and Node[m + 24] == 0 and Node[m + 32] == 0:
                    return m + 32

            if m in diag_1 and col in range(1, 5) and len(
                    set(Node[i] for i in range(m, m + 27, 9))) == 1:  # ( m, m + 9, m + 18 )
                if 1 < row and Node[m - 9] == 0 and Node[m - 18] == 0 and Node[m + 27] == 0:
                    return m - 9
                if row < 4 and Node[m - 9] == 0 and Node[m + 27] == 0 and Node[m + 36] == 0:
                    return m + 27

            if m in diag_2 and row in range(1, 5) and len(
                    set(Node[i] for i in range(m, m + 21, 7))) == 1:  # (m, m + 7, m + 14 )
                if 1 < row and Node[m - 7] == 0 and Node[m - 14] == 0 and Node[m + 21] == 0:
                    return m - 7
                if row < 4 and Node[m - 7] == 0 and Node[m + 21] == 0 and Node[m + 28] == 0:
                    return m + 21


"""------------------------- AI 走的第一步 -------------------------------"""


def the_first_step_for_AI(Node, Player=1):
    """ ------------------------- 条件可以放在函数之外，在使用的时候给定条件 ---------------------"""
    if Player == 1 and len(Node.availables) >= 63:
        moved = list(set(range(64)) - set(Node.availables))
        return choice(moved)
    else:
        return False


"""------------------------- 对临近的点优先rollout --------------------------"""
'''--------------------------当 len(adgecents) 不为空的时候优先rollout， 若为空，则对avalaibles进行随机rollout --------------'''

def adgecents(Node):
    adgecents = set()
    moved = list(set(range(64)) - set(Node.availables))
    for m in moved:
        row = m // 8
        col = m % 8
        if 0 < col:
            adgecents.add(m - 1)        # 添加棋子的左方位置
        if col < 7:
            adgecents.add(m + 1)        # 添加棋子的右方位置
        if 0 < row:
            adgecents.add(m - 8)        # 添加棋子的下方位置
        if row < 7:
            adgecents.add(m + 8)        # 添加棋子的上方位置
        if 0 < col and row < 7:
            adgecents.add(m + 7)        # 添加棋子的左上方位置
        if col < 7 and row < 7:
            adgecents.add(m + 9)        # 添加棋子的右上方位置
        if 0 < col and 0 < row:
            adgecents.add(m - 9)        # 添加棋子的左下方位置
        if col < 7 and 0 < row:
            adgecents.add(m - 7)        # 添加棋子的右下方位置

    adgecents = list(set(adgecents) - set(moved))
    return adgecents


height, width = 8, 8
nodes1 = [i for i in range(9, 15)]
better_choices = []
for i in range(len(nodes1)):
    better_choices += [i * 8 + j for j in nodes1]
bad_choice = list(set(range(64)) - set(better_choices))


""" --------------------- 开始的几步（ 自定义 judge value ） 不选择边缘点，或者在rollout的前几步中直接剔除边缘点 -----------------------------"""

# 返回的是 better_choices == better  availables
# 或者直接返回一个 next move, 注释的部分
def not_choose_edges(Node, Player=1):
    judge_value = 6
    # 条件可以放在函数外，需要时写入条件，调用
    if Player == 1 and len(Node.availables) < 64 - judge_value:
        availables = better_choices
        return availables
    else:
        return Node.availables

    # if Player == 1 and len(Node.availables) < 64 - judge_value:
    #     return choice(better_choices)
    # else:
    #     return choice(Node.availables)










