#
# Move.py
# @author bulbasaur
# @description 
# @created 2019-09-30T23:08:03.488Z+08:00
# @last-modified 2019-10-02T11:10:50.617Z+08:00
#

class Move():
    def __init__(self):
        pass

    def left(self, group):
        grp = group[:]
        for each in group:
            for i in each:
                if i == 0:
                    col = each.index(i)
                    if col == 0:
                        return False
                    row = group.index(each)
                    break
        grp[row][col] = grp[row][col-1]
        grp[row][col-1] = 0
        return grp[:]

    def right(self, group):
        grp = group[:]
        for each in group:
            for i in each:
                if i == 0:
                    col = each.index(i)
                    if col == len(each)-1:
                        return False
                    row = group.index(each)
                    break
        grp[row][col] = grp[row][col+1]
        grp[row][col+1] = 0
        return grp[:]
    
    def up(self, group):
        grp = group[:]
        for each in group:
            for i in each:
                if i == 0:
                    row = group.index(each)
                    if row == 0:
                        return False
                    col = each.index(i)                    
                    break
        grp[row][col] = grp[row-1][col]
        grp[row-1][col] = 0
        return grp[:]

    def down(self, group):
        grp = group[:]
        for each in group:
            for i in each:
                if i == 0:
                    row = group.index(each)
                    if row == len(each)-1:
                        return False
                    col = each.index(i)                    
                    break
        grp[row][col] = grp[row+1][col]
        grp[row+1][col] = 0
        return grp[:]
