#
# Digital.py
# @author bulbasaur
# @description 
# @created 2019-09-30T22:45:59.485Z+08:00
# @last-modified 2019-10-02T15:36:13.698Z+08:00
#

class Digital():
    def __init__(self, prev, name, group, fn):
        if prev:
            self.prev = prev    # 父节点
        else:
            self.prev = self
        self.name = name        # 节点名称
        self.group = group[:]   # 数码矩阵
        self.fn = fn            # f(n)值
        if prev == '':
            self.deep = 0
        else:
            self.deep = prev.deep + 1
    
    # 设置节点在 CLOSE 表中的编号
    def set_num(self, num):
        self.num = num
