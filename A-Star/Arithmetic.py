#
# Arithmetic.py
# @author bulbasaur
# @description 
# @created 2019-10-01T15:41:41.408Z+08:00
# @last-modified 2019-10-04T19:02:27.620Z+08:00
#

import math

# 曼哈顿距离
class Arith1():
    def arith(self, deep, grp1, grp2):
        num = deep
        for each1 in grp1:
            for m1 in each1:
                if m1:
                    row1 = grp1.index(each1)
                    col1 = each1.index(m1)
                    for each2 in grp2:
                        flag = False
                        for m2 in each2:
                            if m1 == m2:
                                flag = True
                                row2 = grp2.index(each2)
                                col2 = each2.index(m2)
                                break
                        if flag:
                            break
                    num += int(math.fabs(row1-row2) + math.fabs(col1-col2))

        return num


class Arith2():
    def arith(self, deep, grp1, grp2):
        num = deep
        n = len(grp1)
        for i in range(n):
            for j in range(n):
                if grp1[i][j]:
                    if grp1[i][j] != grp2[i][j]:
                        num += 1
        return num