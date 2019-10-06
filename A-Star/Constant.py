#
# Constant.py
# @author bulbasaur
# @description 
# @created 2019-10-04T14:19:09.937Z+08:00
# @last-modified 2019-10-05T23:20:36.132Z+08:00
#

class Constant():
    def __init__(self):
        self.options = [" 8 数码", "15 数码"]
        self.options1 = ["曼哈顿距离", "不在位数码个数"]
        self.list_A = [" A*算法流程", \
                "（1）把 S 放入 OPEN 表中，记 f=h，令 CLOSE 为空表", \
                "（2）若 OPEN 表为空表，则宣告失败并退出", \
                "（3）选取 OPEN 表中未设置过的具有最小 f 值的节点为最佳节点 BESTNODE，并把它放入 CLOSE 表中", \
                "（4）若 BESTNODE 为一目标节点，则成功求得一解并退出", \
                "（5）若 BESTNODE 不是目标节点，则扩展之，产生后继节点 SUCCSSOR", \
                "（6）对每个 SUCCSSOR 进行下列过程：", \
                "    （a）建立从 SUCCSSOR 返回 BESTNODE 的指针", \
                "    （b）若 SUCCSSOR 在 CLOSE 表中，则停止扩展此节点", \
                "    （c）若 SUCCSSOR 在 OPEN 表中且新 g(n) 值较小，则将旧节点更新", \
                "    （d）若 SUCCSSOR 在 OPEN 表中但新 g(n) 值较大或相等，则停止扩展此节点", \
                "    （e）若 SUCCSSOR 既不在 OPEN 表中也不在 CLOSE 表中，则将此节点加入 OPEN 表中", \
                "（7）若还有其他扩展节点，转第（6）步；若无其他扩展节点，转第（2）步"]
        self.init_8 = [[7,1,2],[8,5,3],[6,0,4]]
        self.goal_8 = [[1,2,3],[8,0,4],[7,6,5]]
        self.init_15 = [[2,3,4,8],[0,6,15,7],[1,5,10,12],[9,13,11,14]]
        self.goal_15 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]