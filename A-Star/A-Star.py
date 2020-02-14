#
# A-Star.py
# @author bulbasaur
# @description 
# @created 2019-09-28T20:44:02.614Z+08:00
# @last-modified 2020-02-14T17:41:55.890Z+08:00
#

# import pdb
import Arithmetic
import Constant
import Digital
import Move
import time
import math
import random
import threading
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("A-Star 算法")

MOVE = Move.Move()
ARIT1 = Arithmetic.Arith1()
ARIT2 = Arithmetic.Arith2()
CONSTANT = Constant.Constant()

# 存放初始、目标布局矩阵
group_init = []
group_goal = []

# 存放初始布局到目标布局的移动过程
group_course = []

# 存放 OPEN、CLOSE表内容
group_open = []
group_close = []

# 使用过的所有节点数
COUNT1 = 0

# 终止运行标志
STOP = False

# 生成随机 N 数码数组
def range_create(num):
    group = []
    grp = []
    m = int(math.sqrt(num+1))
    for i in range(m):
        grp1 = []
        for i in range(m):
            n = random.randint(0, num)
            while n in grp:
                n = random.randint(0, num)
            grp.append(n)
            grp1.append(n)
        group.append(grp1)
    return group

# 数组转换成字符串
def grp_tran(group):
    st = " "
    for each in group:
        for n in each:
            if n == 0:
                st += "        "
            elif n < 10:
                st += " " + str(n) + "     "
            else:
                st += str(n) + "    "
        st = st[:len(st)-3]
        st += "\n\n "
    st = st[:len(st)-3]
    return st

# 获取数码显示字体大小
def get_bold1():
    st = variable.get()
    num = int(math.sqrt(int(st[:len(st)-3])+1))
    num = str(24 - (num - 3) * 5)
    st = 'Helvetica -' + num + ' bold'
    return st

def get_bold2():
    st = variable.get()
    num = int(math.sqrt(int(st[:len(st)-3])+1))
    num = str(16 - (num - 3) * 3)
    st = 'Helvetica -' + num + ' bold'
    return st

# 初始布局缺省生成
def default_init():
    lab2['font'] = get_bold1()
    st = variable.get()
    num = int(st[:len(st)-3])
    if num == 8:
        group_init[:] = CONSTANT.init_8
    elif num == 15:
        group_init[:] = CONSTANT.init_15
    sv_init.set(grp_tran(group_init))

# 目标布局缺省生成
def default_goal():
    lab4['font'] = get_bold1()
    st = variable.get()
    num = int(st[:len(st)-3])
    if num == 8:
        group_goal[:] = CONSTANT.goal_8
    elif num == 15:
        group_goal[:] = CONSTANT.goal_15
    sv_goal.set(grp_tran(group_goal))

# 初始布局随机生成
def range_init():
    lab2['font'] = get_bold1()
    st = variable.get()
    num = int(st[:len(st)-3])
    group_init[:] = range_create(num)
    sv_init.set(grp_tran(group_init))

# 目标布局随机生成
def range_goal():
    lab4['font'] = get_bold1()
    st = variable.get()
    num = int(st[:len(st)-3])
    group_goal[:] = range_create(num)
    sv_goal.set(grp_tran(group_goal))

# 初始、目标布局自定义
def own_init_goal(lab, var, group):
    lab['font'] = get_bold1()
    top = Toplevel()
    top.title("自定义布局")
    st = variable.get()
    num = int(math.sqrt(int(st[:len(st)-3])+1))
    columns = []
    text = []
    for i in range(num):
        columns.append(str(i+1))
        text.append('-\n')
    treeview = ttk.Treeview(top, height=num, show='headings', columns=columns)
    for i in range(num):
        treeview.column(columns[i], width=55, anchor='center')
        treeview.heading(columns[i], text='<' + str(i+1) + '>')
    if group and (num == len(group)):
        for i in range(num):
            text1 = []
            for m in group[i]:
                text1.append(str(m) + '\n')
            treeview.insert('', i, values=text1)
    else:
        for i in range(num):
            treeview.insert('', i, values=text)
    treeview.grid(row=0, column=0, columnspan=2)
 
    # 双击进入编辑状态
    def set_cell_value(event):
        item = treeview.selection()[0]

        column= treeview.identify_column(event.x)   # 列
        row = treeview.identify_row(event.y)        # 行
        cn = int(str(column).replace('#',''))
        rn = int(str(row).replace('I',''))
        # 保存文本，销毁输入框
        def saveedit(event):
            treeview.set(row, column=column, value=entryedit.get(0.0, "end"))
            entryedit.destroy()

        entryedit = Text(top, width=4, height=1)
        # 回车键保存文本
        entryedit.bind('<Return>', saveedit)
        entryedit.place(x=10+(cn-1)*55, y=6+rn*20)

    def set_ok(var):
        grp1 = []
        grp2 = []
        for each in treeview.get_children(''):
            m = treeview.item(each, "values")
            grp = []
            for i in m:
                try:
                    n = int(i[:len(i)-1])
                    if (n in grp2) or (n<0 or n>=num*num):
                        messagebox.showinfo(parent=root, title="A-Star算法", \
                                message="输入的数字有误，请修改！！！")
                        return
                    grp.append(n)
                    grp2.append(n)
                except:
                    messagebox.showinfo(parent=root, title="A-Star算法", \
                            message="输入有误，请修改！！！")
                    return
            grp1.append(grp)
        group[:] = grp1[:]
        var.set(grp_tran(group))
        top.destroy()
        
    treeview.bind('<Double-1>', set_cell_value) # 双击左键进入编辑
    
    label = Label(top, fg='red', text="空位置请用 “0” 代替")
    label.grid(row=1, column=0, columnspan=2)
    
    bt1 = Button(top, text='确定', width=8, command=lambda:set_ok(var))
    bt1.grid(row=2, column=0, pady=10)

    bt2 = Button(top, text='取消', width=8, command=lambda:top.destroy())
    bt2.grid(row=2, column=1)


# 检查初始布局到目标布局的可行性
def check_yesno(init, goal):
    st = variable.get()
    num = int(st[:len(st)-3])
    row = int(math.sqrt(num+1))
    grp1 = []
    grp2 = []
    # 零所在行数
    zero_init = 0
    zero_goal = 0
    for each in init:
        for i in each:
            if i:
                grp1.append(i)
            else:
                zero_init = init.index(each)
    for each in goal:
        for i in each:
            if i:
                grp2.append(i)
            else:
                zero_goal = goal.index(each)
    # 统计逆序数
    inver_init = 0
    inver_goal = 0
    for m in range(num):
        for n in range(m+1, num):
            if grp1[m] > grp1[n]:
                inver_init += 1
    for m in range(num):
        for n in range(m+1, num):
            if grp2[m] > grp2[n]:
                inver_goal += 1
    # 矩阵为偶数行，加上零到终点位置的行数之差
    if row % 2 == 0:
        inver_init += int(math.fabs(zero_init - zero_goal))
    # 奇偶性相同，返回 True，否则返回 False
    if (inver_init % 2) == (inver_goal % 2):
        return True
    else:
        return False

# 检查 扩展节点是否在 open、close表中
def repeat_open(grp):
    for i in group_open:
        if grp == i.group:
            return True
    return False

def repeat_colse(grp):
    for i in group_close:
        if grp == i.group:
            return True
    return False

# 返回 open 表中 fn 值最小的下标
def min_open():
    m = group_open[0].fn
    inde = 0
    for n in range(len(group_open)):
        # n = len(group_open) - n - 1
        if group_open[n].fn < m:
            inde = n
            m = group_open[n].fn
    return int(inde)

# 连续运行按钮调用函数
def continuous_run(sec, num, arit):
    if (not group_init) or (not group_goal):
        messagebox.showinfo(parent=root, title="A-Star算法", \
                message="请先输入初始布局或目标布局！！！")
        return
    # 判断是否有解
    if not check_yesno(group_init, group_goal):
        messagebox.showerror(parent=root, title=\
            "A-Star 算法", message="此布局无解！！！")
        return
    
    continuous_head(sec)    
    # 使用过的所有节点数
    global COUNT1
    COUNT1 = 0
    group_open[:] = []
    group_close[:] = []

    # 重新生成 Treeview
    global sb1, sb2, tree1, tree2
    sb1, sb2, tree1, tree2 = create_tree()

    sv_time.set('用时:')
    sv_num.set('生成节点数：')
    sv_step.set('移动步数：')

    # 将初始节点加入 OPEN表中
    group_open.append(Digital.Digital('', 'S'+str(COUNT1), \
            group_init[:], arit.arith(0, group_init, group_goal)))
    COUNT1 += 1
    
    if sec:
        list_A.select_set(1)
        tree1.insert("", END, values=(group_open[0].name, '', 0, group_open[0].fn))
        tree1.selection_set('I001')
        sv_open.set(grp_tran(group_init))
    
        second = 1.0 + float(1-sca.get())
        # 检查是否按下终止按钮
        if check_stop(sec):
            return
        time.sleep(second)
        event.wait()
        list_A.select_clear(0, END)
    else:
        second = 0

    # 计时
    time_start = time.time()
    while group_open:        
        # 从 OPEN 表中选取 fn 值最小的节点移到 CLOSE 表中
        group_open[min_open()].set_num(len(group_close))
        group_close.append(group_open[min_open()])

        num1 = int(group_open[min_open()].name[1:])
        st = 'I' + str(hex(num1+1))[2:].upper().zfill(3)

        if sec:
            in1 = group_open[min_open()]
            list_A.select_set(3)
            tree1.yview_moveto(min_open()/len(group_open))
            tree1.selection_set(st)
            sv_open.set(grp_tran(in1.group))
            second = 1.0 + float(1-sca.get())
            # 检查是否按下终止按钮
            if check_stop(sec):
                return
            time.sleep(second*1.2)
            event.wait()
            
            tree1.delete(st)
            tree2.insert("", END, values=(in1.num, in1.name, in1.prev.num, in1.deep, in1.fn))
            tree2.yview_moveto(1)

            st = 'I' + str(hex(in1.num+1))[2:].upper().zfill(3)
            tree2.selection_set(st)
            sv_close.set(grp_tran(in1.group))
            second = 1.0 + float(1-sca.get())
            # 检查是否按下终止按钮
            if check_stop(sec):
                return
            time.sleep(second*0.3)
            event.wait()
            list_A.select_clear(0, END)
        
        group_open.pop(min_open())

        # 检查是否找到目标解        
        if group_close[len(group_close)-1].group == group_goal:
            time_end = time.time()
            st = "%*.*f" % (12, 6, time_end-time_start)                
            sv_time.set('用时:' + str(st))
            sv_num.set('生成节点数：' + str(COUNT1))
            sv_step.set('移动步数：' + str(group_close[len(group_close)-1].deep))
            if sec:
                list_A.select_set(4)
            continuous_end(sec)
            messagebox.showinfo(parent=root, title="A-Star 算法", message="求解成功！！！")
            return

        if sec:
            list_A.select_set(5)
            second = 1.0 + float(1-sca.get())
            # 检查是否按下终止按钮
            if check_stop(sec):
                return
            time.sleep(second*0.5)
            event.wait()
            list_A.select_clear(0, END)

        # 扩展新节点
        clo = group_close[len(group_close)-1]
        grp_clo = clo.group
        deep1 = clo.deep + 1
        # 左移
        grp2 = get_clo_end(grp_clo)
        grp1 = MOVE.left(grp2)
        if open_expand(grp1, deep1, arit, clo, second):
            return
        # 右移
        grp2 = get_clo_end(grp_clo)
        grp1 = MOVE.right(grp2)
        if open_expand(grp1, deep1, arit, clo, second):
            return
        # 上移
        grp2 = get_clo_end(grp_clo)
        grp1 = MOVE.up(grp2)
        if open_expand(grp1, deep1, arit, clo, second):
            return
        # 下移
        grp2 = get_clo_end(grp_clo)
        grp1 = MOVE.down(grp2)
        if open_expand(grp1, deep1, arit, clo, second):
            return

        # 若 OPEN表为空，退出，宣告失败
        if not group_open:
            if sec:
                list_A.select_set(2)
            messagebox.showerror(parent=root, title="A-Star 算法", message="求解失败！！！")
            continuous_end(sec)
            return
        
    continuous_end(sec)


def get_clo_end(grp_clo):
    grp = []
    for i in grp_clo:
        grp.append(i[:])
    return grp[:]

def open_expand(grp1, deep1, arit, clo, second):
    # 检查是否按下终止按钮
    if check_stop(second):
        return True
    global COUNT1
    if grp1:
        if second:
            sv_open.set(grp_tran(grp1))
            list_A.select_set(7)
            second = 1.0 + float(1-sca.get())
            # 检查是否按下终止按钮
            if check_stop(second):
                return True
            time.sleep(second*0.5)
            event.wait()
            list_A.select_clear(0, END)
        # 不在 close表中
        if not repeat_colse(grp1):
            # 在 open表中
            if repeat_open(grp1):
                for i in group_open:
                    if i.group == grp1:
                        inde = group_open.index(i)
                        break
                # 新路径比原路径短，更新父节点及 f(n)值
                if group_open[inde].deep > deep1:
                    group_open[inde].fn -= (group_open[inde].deep - deep1)
                    group_open[inde].deep = deep1
                    group_open[inde].prev = clo

                    if second:
                        list_A.select_set(9)
                        num1 = int(group_open[inde].name[1:])
                        st = 'I' + str(hex(num1+1))[2:].upper().zfill(3)
                        tree1.selection_set(st)
                        tree1.yview_moveto(inde/len(group_open))
                        second = 1.0 + float(1-sca.get())
                        # 检查是否按下终止按钮
                        if check_stop(second):
                            return True
                        time.sleep(second)
                        event.wait()
                        
                        tree1.set(st, '2', clo.num)
                        tree1.set(st, '3', deep1)
                        tree1.set(st, '4', group_open[inde].fn)

                        second = 1.0 + float(1-sca.get())
                        # 检查是否按下终止按钮
                        if check_stop(second):
                            return True
                        time.sleep(second)
                        event.wait()
                        list_A.select_clear(0, END)
                        list_A.select_set(12)
                        second = 1.0 + float(1-sca.get())
                        # 检查是否按下终止按钮
                        if check_stop(second):
                            return True
                        time.sleep(second)
                        event.wait()
                        list_A.select_clear(0, END)
                else:   # 新路径较长或相等
                    if second:
                        list_A.select_set(10)
                        second = 1.0 + float(1-sca.get())
                        # 检查是否按下终止按钮
                        if check_stop(second):
                            return True
                        time.sleep(second)
                        event.wait()
                        list_A.select_clear(0, END)
            else:   # 既不在 close表中，也不在 open表中，则加入 open表中
                group_open.append(Digital.Digital(clo, 'S'+str(COUNT1), \
                            grp1[:], arit.arith(deep1, grp1, group_goal)))

                if second:
                    list_A.select_set(11)
                    tree1.insert("", END, values=('S'+str(COUNT1), clo.num, deep1, \
                                    group_open[len(group_open)-1].fn))
                    tree1.yview_moveto(1)
                    num1 = int(group_open[len(group_open)-1].name[1:])
                    st = 'I' + str(hex(num1+1))[2:].upper().zfill(3)
                    tree1.selection_set(st)
                    second = 1.0 + float(1-sca.get())
                    # 检查是否按下终止按钮
                    if check_stop(second):
                        return True
                    time.sleep(second)
                    event.wait()
                    list_A.select_clear(0, END)
                COUNT1 += 1
        else:   # 在 CLOSE表中
            if second:
                list_A.select_set(8)
                second = 1.0 + float(1-sca.get())
                # 检查是否按下终止按钮
                if check_stop(second):
                    return True
                time.sleep(second)
                event.wait()
                list_A.select_clear(0, END)
        if second:
            list_A.select_set(12)
            second = 1.0 + float(1-sca.get())
            # 检查是否按下终止按钮
            if check_stop(second):
                return True
            time.sleep(second*0.5)
            event.wait()
            list_A.select_clear(0, END)

    return False

def continuous_head(sec):
    if sec:
        bt_pause['state'] = 'active'
        bt_start['text'] = '运行中'
    else:
        bt_fast['text'] = '运行中'
    lab7['font'] = get_bold2()
    lab8['font'] = get_bold2()
    bt1['state'] = 'disabled'
    bt2['state'] = 'disabled'
    bt3['state'] = 'disabled'
    bt4['state'] = 'disabled'
    bt5['state'] = 'disabled'
    bt6['state'] = 'disabled'
    opt['state'] = 'disabled'
    opt1['state'] = 'disabled'
    if not sec:
        sca['state'] = 'disabled'
    bt_start['state'] = 'disabled'
    bt_show['state'] = 'disabled'
    bt_fast['state'] = 'disabled'
    bt_show_co['state'] = 'disabled'
    bt_stop['state'] = 'active'
    lab2['font'] = get_bold1()
    lab4['font'] = get_bold1()
    list_A.select_clear(0, END)
    global sb1, sb2, tree1, tree2
    sb1.destroy()
    sb2.destroy()
    tree1.destroy()
    tree2.destroy()
    sv_open.set("\t       \n\n\n\n")
    sv_close.set("\t       \n\n\n\n")

def continuous_end(sec):
    bt1['state'] = 'active'
    bt2['state'] = 'active'
    bt3['state'] = 'active'
    bt4['state'] = 'active'
    bt5['state'] = 'active'
    bt6['state'] = 'active'
    opt['state'] = 'active'
    opt1['state'] = 'active'
    sca['state'] = 'active'
    bt_start['state'] = 'active'
    bt_start['text'] = '连续运行'
    bt_pause['state'] = 'disabled'
    bt_continue['state'] = 'disabled'
    bt_show['state'] = 'active'
    bt_fast['state'] = 'active'
    bt_fast['text'] = '快速运行'
    bt_stop['state'] = 'disabled'
    if not sec:
        bt_show_co['state'] = 'active'


event = threading.Event()
# 连续运行按钮响应函数
def call_start(sec):
    st = variable.get()
    num = int(st[:len(st)-3])
    if variable1.get() == CONSTANT.options1[0]:
        arit = ARIT1
    elif variable1.get() == CONSTANT.options1[1]:
        arit = ARIT2
    event.set()
    thread = threading.Thread(target=lambda:continuous_run(sec, num, arit))
    thread.setDaemon(True)
    thread.start()

# 暂停按钮响应函数
def call_pause():
    bt_pause['state'] = 'disabled'
    bt_continue['state'] = 'active'
    bt_stop['state'] = 'disabled'
    event.clear()

# 继续按钮响应函数
def call_continue():
    bt_continue['state'] = 'disabled'
    bt_pause['state'] = 'active'
    bt_stop['state'] = 'active'
    event.set()

# 终止按钮响应函数
def call_stop():
    global STOP
    STOP = True
    bt_stop['state'] = 'disabled'

# 检查是否按下终止按钮
def check_stop(sec):
    global STOP
    if STOP:
        STOP = False
        continuous_end(sec)
        bt_show['state'] = 'disabled'
        return True
    return False

# 结果展示调用函数
def result_show():
    lab2['font'] = get_bold1()
    bt_show['state'] = 'disabled'
    st = variable.get()
    num = int(st[:len(st)-3])
    group_course[:] = []
    node = group_close[len(group_close)-1]
    while node.prev != node:
        group_course.insert(0, node)
        node = node.prev
    group_course.insert(0, node)
    m = 0
    for i in group_course:
        sv_init.set(grp_tran(i.group))
        sv_step.set('移动步数：' + str(m))
        time.sleep(0.3)
        event1.wait()
        m += 1
    time.sleep(2)
    sv_init.set(grp_tran(group_init))
    bt_show['state'] = 'active'

event1 = threading.Event()

# 结果演示按钮响应事件
def call_result():
    event1.set()
    thread = threading.Thread(target=result_show)
    thread.setDaemon(True)
    thread.start()

# 展示OPEN/CLOSE表按钮响应事件
def call_result_co():
    bt_show_co['text'] = '添加中'

    for i in group_open:
        tree1.insert("", END, values=(i.name, i.prev.num, i.deep, i.fn))
    sv_open.set(grp_tran(group_goal))
    for i in group_close:
        tree2.insert("", END, values=(i.num, i.name, i.prev.num, i.deep, i.fn))
    sv_close.set(grp_tran(group_goal))
    
    bt_show_co['text'] = '展示OPEN/CLOSE表'
    bt_show_co['state'] = 'disabled'

# Treeview 鼠标左键单击事件
def call_tree1(event):
    lab7['font'] = get_bold2()
    try:
        item1 = tree1.selection()[0]
        st = tree1.item(item1, "values")[0]
        for i in group_open:
            if i.name == st:
                sv_open.set(grp_tran(i.group))  
    except:
        return

def call_tree2(event):
    lab8['font'] = get_bold2()
    try:
        item1 = tree2.selection()[0]
        num = int(tree2.item(item1, "values")[0])
        sv_close.set(grp_tran(group_close[num].group))
    except:
        return

# 添加 Treeview
def create_tree():
    # OPEN 表 Treeview
    sb1 = Scrollbar(frame1)
    sb1.pack(side=RIGHT, fill=Y)

    tree1 = ttk.Treeview(frame1, height=8, show='headings', yscrollcommand=sb1.set)
    tree1['columns'] = ["1", "2", "3", "4"]
    tree1.column("1", width=45, anchor='center')
    tree1.column("2", width=45, anchor='center')
    tree1.column("3", width=40, anchor='center')
    tree1.column("4", width=42, anchor='center')
    tree1.heading("1", text="节点")
    tree1.heading("2", text="父节点")
    tree1.heading("3", text="层数")
    tree1.heading("4", text="f(n)")

    tree1.bind("<ButtonRelease-1>", call_tree1)
    tree1.pack(side=LEFT, fill=BOTH)
    sb1.config(command=tree1.yview)

    # CLOSE 表 Treeview
    sb2 = Scrollbar(frame2)
    sb2.pack(side=RIGHT, fill=Y)

    tree2 = ttk.Treeview(frame2, height=8, show='headings', yscrollcommand=sb2.set)
    tree2['columns'] = ["1", "2", "3", "4", "5"]
    tree2.column("1", width=38, anchor='center')
    tree2.column("2", width=45, anchor='center')
    tree2.column("3", width=45, anchor='center')
    tree2.column("4", width=38, anchor='center')
    tree2.column("5", width=40, anchor='center')
    tree2.heading("1", text="编号")
    tree2.heading("2", text="节点")
    tree2.heading("3", text="父节点")
    tree2.heading("4", text="层数")
    tree2.heading("5", text="f(n)")

    tree2.bind("<ButtonRelease-1>", call_tree2)
    tree2.pack(side=LEFT, fill=BOTH)
    sb2.config(command=tree2.yview)

    return sb1, sb2, tree1, tree2


lab1 = Label(root, text='初始布局')
lab1.grid(row=0, column=0, columnspan=3, pady=10)

bt1 = Button(root, text="缺省布局", width=8, command=default_init)
bt1.grid(row=1, column=0, padx=25)

bt2 = Button(root, text="随机生成", width=8, command=range_init)
bt2.grid(row=2, column=0)

bt3 = Button(root, text="自定义", width=8, command=lambda:own_init_goal(lab2, sv_init, group_init))
bt3.grid(row=3, column=0)

sv_init = StringVar()
sv_init.set("\t       \n\n\n\n")
lab2 = Label(root, fg='#0000CD', bg='gray', \
        compound='center', textvariable=sv_init, font='Helvetica -24 bold')
lab2.grid(row=1, column=1, rowspan=3, columnspan=2, pady=20)

lab3 = Label(root, text='目标布局')
lab3.grid(row=4, column=0, columnspan=3, pady=15)

bt4 = Button(root, text="缺省布局", width=8, command=default_goal)
bt4.grid(row=5, column=0)

bt5 = Button(root, text="随机生成", width=8, command=range_goal)
bt5.grid(row=6, column=0)

bt6 = Button(root, text="自定义", width=8, command=lambda:own_init_goal(lab4, sv_goal, group_goal))
bt6.grid(row=7, column=0)

lab_open = Label(root, text='OPEN 表')
lab_open.grid(row=0, column=4)

lab_close = Label(root, text='CLOSE 表')
lab_close.grid(row=0, column=6, columnspan=2)

sv_goal = StringVar()
sv_goal.set("\t       \n\n\n\n")
lab4 = Label(root, fg='#0000CD', bg='gray', \
        compound='center', textvariable=sv_goal, font='Helvetica -24 bold')
lab4.grid(row=5, column=1, rowspan=3, columnspan=2, pady=20)

lab5 = Label(root, text='选择数码：', anchor='e')
lab5.grid(row=8, column=0, pady=25, sticky=E)

variable = StringVar(value=CONSTANT.options[0])
# 通过 * 来实现传递多个参数
opt = OptionMenu(root, variable, *CONSTANT.options)
opt.grid(row=8, column=1, columnspan=2)

lab6 = Label(root, text='运行速度：')
lab6.grid(row=9, column=0, sticky=E)

sca = Scale(root, from_=0, to=1.95, resolution=0.05, showvalue=0, length=100, orient=HORIZONTAL)
sca.set(1)
sca.grid(row=9, column=1, columnspan=2, pady=30)

# OPEN 表 Frame
frame1 = Frame(root)
frame1.grid(row=1, column=3, rowspan=3, columnspan=2)

# CLOSE 表 Frame
frame2 = Frame(root)
frame2.grid(row=1, column=6, rowspan=3, columnspan=2, padx=20)

sb1, sb2, tree1, tree2 = create_tree()

sv_open = StringVar()
sv_open.set("\t       \n\n\n\n")
lab7 = Label(root, fg='#0000CD', bg='gray', \
        compound='center', textvariable=sv_open, font='Helvetica -16 bold')
lab7.grid(row=1, column=5, rowspan=3, padx=15)

sv_close = StringVar()
sv_close.set("\t       \n\n\n\n")
lab8 = Label(root, fg='#0000CD', bg='gray', \
        compound='center', textvariable=sv_close, font='Helvetica -16 bold')
lab8.grid(row=1, column=8, rowspan=3, padx=15, sticky=W)

# A*算法流程框
list_sv3 = StringVar()
list_sv3.set(CONSTANT.list_A)
list_A = Listbox(root, listvariable=list_sv3, width=85, height=15, selectmode=SINGLE)
list_A.grid(row=4, column=3, rowspan=5, columnspan=5, padx=20)

# 按钮
bt_start = Button(root, text="连续运行", width=12, command=lambda:call_start(1))
bt_start.grid(row=9, column=3, padx=50)

bt_pause = Button(root, text="暂停", width=9, state='disabled', command=call_pause)
bt_pause.grid(row=9, column=4)

bt_continue = Button(root, text="继续", width=9, state='disabled', command=call_continue)
bt_continue.grid(row=9, column=5)

bt_stop = Button(root, text="终止", width=9, state='disabled', command=call_stop)
bt_stop.grid(row=9, column=6)

bt_show_co = Button(root, text="展示OPEN/CLOSE表", width=18, state='disabled', command=call_result_co)
bt_show_co.grid(row=8, column=8)

bt_show = Button(root, text="结果演示", width=13, state='disabled', command=call_result)
bt_show.grid(row=9, column=8)

bt_fast = Button(root, text="快速运行", width=12, command=lambda:call_start(0))
bt_fast.grid(row=9, column=7)

variable1 = StringVar(value=CONSTANT.options1[0])
opt1 = OptionMenu(root, variable1, *CONSTANT.options1)
opt1.grid(row=4, column=8)

sv_num = StringVar(value='生成节点数：')
ent2 = Entry(root, width=16, bd=2, fg='blue', textvariable=sv_num, state="readonly")
ent2.grid(row=5, column=8)

sv_time = StringVar(value='用时:')
ent1 = Entry(root, width=16, bd=2, fg='blue', textvariable=sv_time, state="readonly")
ent1.grid(row=6, column=8, padx=30)

sv_step = StringVar(value='移动步数：')
ent3 = Entry(root, width=13, bd=2, fg='blue', textvariable=sv_step, state="readonly")
ent3.grid(row=7, column=8)


mainloop()
