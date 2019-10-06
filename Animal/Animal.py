#
# System.py
# @author JRB
# @description 
# @created 2019-09-21T20:13:31.213Z+08:00
# @last-modified 2019-10-03T21:55:54.957Z+08:00
#

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk


group_o_animal = []     # 存放动物文件原始数据
group_o_cond = []       # 存放条件文件原始数据
group_o_rule = []       # 存放规则文件原始数据
group_animal = []       # 存放所有动物种类
group_database = []     # 存放动态数据库内容
group_all_rule = []     # 存放所有规则
group_test_rule = []    # 存放待测试规则
group_use_rule = []     # 存放推理过程使用规则
group_con_anim = []     # 存放条件加动物
group1 = []             # 存放条件

root = Tk()
root.title("产生式规则--动物识别系统")

# 读取所有动物种类
sv_anm = StringVar()
def read_animal():
    group_o_animal[:] = []
    group_animal[:] = []
    animal_file = open("files/animal.txt")
    for each_line in animal_file:
        group_o_animal.append(each_line)
        (each_str1, each_str2) = each_line.split("；")
        group_animal.append(each_str1)
    animal_file.close()
    sv_anm.set(group_animal)

read_animal()

# 读取所有规则
def read_rule():
    group_o_rule[:] = []
    group_all_rule[:] = []
    all_rule_file = open("files/rule.txt")
    for each_line in all_rule_file:
        group_o_rule.append(each_line)
        (str1, str2) = each_line.split(' --> ')
        (str3, str4) = str2.split('；')
        str5 = str1.split('，')
        grp1 = []
        grp2 = [str3]
        for i in str5:
            grp1.append(i)
        grp2.insert(0, grp1)
        group_all_rule.append(grp2)
    all_rule_file.close()

read_rule()

# 条件选项
frame1 = Frame(root)
frame1.grid(row=0, column=0, columnspan=2, padx=30, pady=35)
sb1 = Scrollbar(frame1)
sb1.pack(side=RIGHT, fill=Y)

v1 = StringVar(value=group1)

def read_cond():
    group_o_cond[:] = []
    group1[:] = []
    con_file = open("files/condition.txt")
    for each_line in con_file:
        group_o_cond.append(each_line)
        (each_str1, each_str2) = each_line.split("；")
        group1.append(each_str1)
    con_file.close()
    v1.set(group1)

read_cond()

lb1 = Listbox(frame1, listvariable=v1, width=23, selectmode=EXTENDED, yscrollcommand=sb1.set)

lb1.pack(side=LEFT, fill=BOTH)
sb1.config(command=lb1.yview)   # 设置为鼠标可拖拽

# 更新条件加动物集合
ca_sv = StringVar()
def update_con_anim():
    group_con_anim[:] = group1[:]
    for i in group_animal:
        group_con_anim.append(i)
    ca_sv.set(group_con_anim)

update_con_anim()
ca_sv.set(group_con_anim)

# 使用规则
frame2 = Frame(root)
frame2.grid(row=0, column=2, padx=30, pady=35)
sb2 = Scrollbar(frame2, orient=HORIZONTAL)
sb2.pack(side=BOTTOM, fill=X)
sb2_1 = Scrollbar(frame2)
sb2_1.pack(side=RIGHT, fill=Y)

group2 = ["使用规则："]
v2 = StringVar(value=group2)

lb2 = Listbox(frame2, listvariable=v2, width=35, xscrollcommand=sb2.set, yscrollcommand=sb2_1.set)

lb2.pack(side=LEFT, fill=BOTH)
sb2.config(command=lb2.xview)
sb2_1.config(command=lb2.yview)

# 添加按钮响应函数
def callback1_1():
    # 获取用户选中的条件的索引值
    curselection1_1 = lb1.curselection()
    # 将用户选中的规则添加到“已添加规则”里
    for i in curselection1_1:
        lb1.select_clear(i)
        if group1[i] not in group4:
            group4.append(group1[i])
            v4.set(group4)

# 添加按钮
button1_1 = Button(root, text="添加", width=7, command=callback1_1)
button1_1.grid(row=1, column=0, padx=18)

# 删除按钮响应函数
def callback1_2():
    # 获取用户选中的条件的索引值
    curselection1_2 = lb4.curselection()
    # 将索引值下标顺序反序，删除时从后往前删除
    curselection1_3 = []
    for i in curselection1_2:
        curselection1_3.insert(0,i)
    # 将用户选中的规则添加到“已添加规则”里
    for i in curselection1_3:
        lb4.select_clear(i)
        group4.pop(i)
        v4.set(group4)

# 删除按钮
button1_2 = Button(root, text="删除", width=7, command=callback1_2)
button1_2.grid(row=1, column=1, sticky=W)

# 已添加条件
frame4 = Frame(root)
frame4.grid(row=2, column=0, rowspan=5, columnspan=2, padx=30, pady=35)
sb4 = Scrollbar(frame4)
sb4.pack(side=RIGHT, fill=Y)

group4 = []
v4 = StringVar(value=group4)
lb4 = Listbox(frame4, fg="blue", listvariable=v4, width=23, selectmode=EXTENDED, yscrollcommand=sb4.set)

lb4.pack(side=LEFT, fill=BOTH)
sb4.config(command=lb4.yview)

# 动态数据库
frame5 = Frame(root)
frame5.grid(row=2, column=2, rowspan=5, padx=30, pady=35)
sb5 = Scrollbar(frame5, orient=HORIZONTAL)
sb5.pack(side=BOTTOM, fill=X)
sb5_1 = Scrollbar(frame5)
sb5_1.pack(side=RIGHT, fill=Y)

group5 = ["动态数据库："]
v5 = StringVar(value=group5)

lb5 = Listbox(frame5, listvariable=v5, width=35, xscrollcommand=sb5.set, yscrollcommand=sb5_1.set)

lb5.pack(side=LEFT, fill=BOTH)
sb5.config(command=lb5.xview)
sb5_1.config(command=lb5.yview)

# 图片显示
frame6 = Frame(root)

path = StringVar()

# 更换图片函数
def image_change(file_name):
    path.set(file_name)
    try:
        img_open = Image.open(e6.get())
    except:
        img_open = Image.open("images/blank.gif")
    img = ImageTk.PhotoImage(img_open)
    imageLabel.config(image=img)
    imageLabel.image=img

# e6用来存储图片路径，没有显示出来
e6=Entry(frame6, state="readonly", text=path)

imageLabel = Label(frame6)
image_change("images/start.gif")
imageLabel.pack(side=RIGHT)
frame6.grid(row=0, column=3, columnspan=6, padx=30, pady=35)

# 推理结果 Label
textLabel = Label(root, text="推理结果：")
textLabel.grid(row=1, column=3, columnspan=2, sticky=E)

# 显示推理结果
v8 = StringVar()
v8.set("")
e8 = Entry(root, width=13, bd=5, fg="blue", textvariable=v8, state="readonly")
e8.grid(row=1, column=5, columnspan=4)

# 存放推理规则
group11 = []
v11 = StringVar(value=group11)

def update_group11():
    group11[:] = []
    num = 1
    for each in group_all_rule:
        (str1, str2) = each
        str3 = ""
        str3 += str(num) + "、"
        for i in str1:
            str3 += i + "  "
        str3 += "-->  " + str2 + "  "
        group11.append(str3)
        num += 1
    v11.set(group11)    

update_group11()

# 判断是否已经推理成功
def result_check(group_data):
    for each in group_animal:
        if each in group_data:
            v8.set(each)
            image_change("images/"+ each +".gif")
            return True
    return False

# 自动推理按钮响应函数
def callback9():

    if not group4:
        messagebox.showinfo("动物识别系统", "请先添加条件！！！")
        return
    # 初始化动态数据库、待测试、已使用规则库
    group_database = group4[:]
    group_test_rule = group_all_rule[:]
    group_use_rule = []
    # 先重置 listbox
    group2[1:] = []
    group5[1:] = []
    v2.set(group2)
    v5.set(group5)
    v8.set("")

    while True:
        if result_check(group_database):
            v2.set(group2)
            v5.set(group5)
            messagebox.showinfo("动物识别系统", "推理成功！！！")
            return
        # 依次将待测试规则集与动态数据库匹配
        flag1 = True
        con_num = 0
        rule = []
        result = ""
        for each_t in group_test_rule:
            (t_rule, t_result) = each_t
            # 判断是否满足该规则
            flag2 = True
            for i in t_rule:
                if i not in group_database:
                    flag2 = False
                    break
            # 匹配成功
            if flag2 and (t_result not in group_database):
                flag1 = False
                # 推理成功，退出循环
                if t_result in group_animal:
                    rule[:] = each_t[:]
                    result = t_result
                    break
                # 满足条件多的规则替换满足条件少的规则
                if con_num < len(t_rule):
                    con_num = len(t_rule)
                    rule[:] = each_t[:]
                    result = t_result
        
        if flag1:
            v2.set(group2)
            v5.set(group5)
            
            image_change("images/unsuccessful.gif")
            messagebox.showerror("动物识别系统", "推理失败！！！")
            return

        group_database.append(result)                    
        group_use_rule.append(rule)
        group_test_rule.remove(rule)

        group2[1:] = []
        for each in group_use_rule:
            (str_u, str_r) = each
            st = ""
            for i in str_u:
                st += i + " "        
            st += " --> " + str_r + " （第"
            st += str(group_all_rule.index(each) + 1) + "条）"
            group2.append(st)
            
        group5.append(group_database[:])

# 自动推理按钮
button9 = Button(root, text="自动推理", width=15, command=callback9)
button9.grid(row=2, column=3, rowspan=2, columnspan=6)

# 重置按钮响应函数
def callback10():
    bool10 = messagebox.askokcancel(parent=root, title="动物识别系统", message="确定要重置吗？")
    if not bool10:
        return
    group4[:] = []
    group2[1:] = []
    group5[1:] = []
    v4.set(group4)
    v2.set(group2)
    v5.set(group5)
    v8.set("")
    # 更换图片
    image_change("images/start.gif")

# 重置按钮
button10 = Button(root, text="重置", width=12, command=callback10)
button10.grid(row=1, column=2)

# 增删条件/动物按钮响应函数
def edit():
    top = Toplevel()
    top.title("增删条件")

    lab1 = Label(top, text="条件", justify=LEFT)
    lab1.grid(row=0, column=0, columnspan=2, pady=5)

    frame1 = Frame(top)
    frame1.grid(row=1, column=0, rowspan=4, padx=30, pady=10)
    sb1 = Scrollbar(frame1, orient=HORIZONTAL)
    sb1.pack(side=BOTTOM, fill=X)
    sb2 = Scrollbar(frame1)
    sb2.pack(side=RIGHT, fill=Y)

    lb1 = Listbox(frame1, listvariable=v1, width=20, height=15, \
            selectmode=EXTENDED, xscrollcommand=sb1.set, yscrollcommand=sb2.set)

    lb1.pack(side=LEFT, fill=BOTH)
    sb1.config(command=lb1.xview)
    sb2.config(command=lb1.yview)

    et1 = Entry(top, width=12, bd=2, fg="blue")
    et1.grid(row=1, column=1, padx=10, sticky=S)

    but1 = Button(top, text="添加", width=10, command=lambda:edit_add1(top, lb1, et1))
    but1.grid(row=2, column=1)

    but2 = Button(top, text="删除", width=10, command=lambda:edit_del1(top, lb1))
    but2.grid(row=3, column=1, sticky=S)

    lab2 = Label(top, text="动物", justify=LEFT)
    lab2.grid(row=0, column=2, columnspan=2, pady=5)

    frame2 = Frame(top)
    frame2.grid(row=1, column=2, rowspan=4, padx=30, pady=30)
    sb3 = Scrollbar(frame2, orient=HORIZONTAL)
    sb3.pack(side=BOTTOM, fill=X)
    sb4 = Scrollbar(frame2)
    sb4.pack(side=RIGHT, fill=Y)

    lb2 = Listbox(frame2, listvariable=sv_anm, width=20, height=15, \
            selectmode=EXTENDED, xscrollcommand=sb3.set, yscrollcommand=sb4.set)

    lb2.pack(side=LEFT, fill=BOTH)
    sb3.config(command=lb2.xview)
    sb4.config(command=lb2.yview)

    et2 = Entry(top, width=12, bd=2, fg="blue")
    et2.grid(row=1, column=3, padx=20, sticky=S)

    but3 = Button(top, text="添加", width=10, command=lambda:edit_add2(top, lb2, et2))
    but3.grid(row=2, column=3)

    but4 = Button(top, text="删除", width=10, command=lambda:edit_del2(top, lb2))
    but4.grid(row=3, column=3, sticky=S)

def edit_add1(top, lb, et):
    if (not et.get()):
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先输入要添加的条件！！！")
        return

    st = et.get() + "；\n"
    # 判断要添加的条件是否已经存在
    if group_o_cond.count(st):
        lb.select_clear(0, END)
        lb.select_set(group_o_cond.index(st))
        messagebox.showerror(parent=top, title="动物识别系统", message="此条件已存在！！！")
        return
    group_o_cond.insert(0, st)
    fil = open("files/condition.txt", 'w')
    fil.writelines(group_o_cond)
    fil.close()
    read_cond()
    update_con_anim()

    lb.select_clear(0, END)
    lb.select_set(0)

    messagebox.showinfo(parent=top, title="动物识别系统", message="添加成功！！！")

def edit_del1(top, lb):
    cur = lb.curselection()

    if not cur:
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先选择要删除的条件！！！")
        return
    
    messbox = messagebox.askokcancel(parent=top, title="动物识别系统", message="确定要删除选中的条件吗？")
    if not messbox:
        return
    
    cur1 = []
    for i in cur:
        cur1.insert(0,i)
    for i in cur1:
        lb.select_clear(i)
        group_o_cond.pop(i)
    fil = open("files/condition.txt", 'w')
    fil.writelines(group_o_cond)
    fil.close()
    read_cond()
    update_con_anim()

def edit_add2(top, lb, et):
    if (not et.get()):
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先输入要添加的动物！！！")
        return

    st = et.get() + "；\n"
    # 判断要添加的动物是否已经存在
    if group_o_animal.count(st):
        lb.select_clear(0, END)
        lb.select_set(group_o_animal.index(st))
        messagebox.showerror(parent=top, title="动物识别系统", message="此动物已存在！！！")
        return
    group_o_animal.insert(0, st)
    fil = open("files/animal.txt", 'w')
    fil.writelines(group_o_animal)
    fil.close()
    read_animal()
    update_con_anim()

    lb.select_clear(0, END)
    lb.select_set(0)

    messagebox.showinfo(parent=top, title="动物识别系统", message="添加成功！！！")

def edit_del2(top, lb):
    cur = lb.curselection()

    if not cur:
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先选择要删除的动物！！！")
        return
    
    messbox = messagebox.askokcancel(parent=top, title="动物识别系统", message="确定要删除选中的动物吗？")
    if not messbox:
        return
    
    cur1 = []
    for i in cur:
        cur1.insert(0,i)
    for i in cur1:
        lb.select_clear(i)
        group_o_animal.pop(i)
    fil = open("files/animal.txt", 'w')
    fil.writelines(group_o_animal)
    fil.close()
    read_animal()
    update_con_anim()

# 增删条件/动物按钮
butt1 = Button(root, text="增删条件/动物", width=12, command=edit)
butt1.grid(row=5, column=3, columnspan=3)

# 添加规则位置序号
sv3 = StringVar()
sv_lab = StringVar()
def update_num():
    st = "添加位置序号（1~"
    st += str(len(group_all_rule) + 1) + "）:"
    sv_lab.set(st)
    sv3.set(len(group_all_rule) + 1)
update_num()

# 添加规则弹出对话框
def callback12():
    top = Toplevel()
    top.title("添加规则")

    lab1 = Label(top, text="条件", justify=LEFT)
    lab1.grid(row=0, column=0, columnspan=2, pady=5)
    lab2 = Label(top, text="结论", justify=LEFT)
    lab2.grid(row=0, column=2, columnspan=2, pady=5)

    sv1 = StringVar()
    et1 = Entry(top, width=30, bd=2, fg="blue", textvariable=sv1, state="readonly")
    et1.grid(row=1, column=0, columnspan=2)

    sv2 = StringVar()
    et2 = Entry(top, width=20, bd=2, fg="blue", textvariable=sv2, state="readonly")
    et2.grid(row=1, column=2, columnspan=2)

    but1 = Button(top, text="选择", width=10, command=lambda:ad_con(lb1, sv1))
    but1.grid(row=2, column=0, columnspan=2, pady=12)

    but2 = Button(top, text="选择", width=10, command=lambda:ad_res(lb2, sv2))
    but2.grid(row=2, column=2, columnspan=2, pady=12)

    frame1 = Frame(top)
    frame1.grid(row=3, column=0, columnspan=2, padx=30, pady=5, sticky=S)
    sb1 = Scrollbar(frame1, orient=HORIZONTAL)
    sb1.pack(side=BOTTOM, fill=X)
    sb2 = Scrollbar(frame1)
    sb2.pack(side=RIGHT, fill=Y)

    lb1 = Listbox(frame1, listvariable=v1, width=30, height=10, \
            selectmode=EXTENDED, xscrollcommand=sb1.set, yscrollcommand=sb2.set)

    lb1.pack(side=LEFT, fill=BOTH)
    sb1.config(command=lb1.xview)
    sb2.config(command=lb1.yview)

    frame2 = Frame(top)
    frame2.grid(row=3, column=2, columnspan=2, padx=30, pady=5, sticky=S)
    sb3 = Scrollbar(frame2, orient=HORIZONTAL)
    sb3.pack(side=BOTTOM, fill=X)
    sb4 = Scrollbar(frame2)
    sb4.pack(side=RIGHT, fill=Y)

    lb2 = Listbox(frame2, listvariable=ca_sv, width=20, height=10, \
            xscrollcommand=sb3.set, yscrollcommand=sb4.set)

    lb2.pack(side=LEFT, fill=BOTH)
    sb3.config(command=lb2.xview)
    sb4.config(command=lb2.yview)

    lab = Label(top, textvariable=sv_lab, justify=LEFT)
    lab.grid(row=4, column=0)

    e1 = Entry(top, width=10, textvariable=sv3)
    e1.grid(row=4, column=1, sticky=W)

    but3 = Button(top, text="清空", width=8, command=lambda:del_call(sv1, sv2, e1))
    but3.grid(row=4, column=2, pady=10)

    but4 = Button(top, text="添加", width=8, command=lambda:add_call(top, sv1, sv2, e1.get()))
    but4.grid(row=4, column=3, pady=10)

# 添加：选择条件按钮响应函数
def ad_con(lb, sv):
    concu = lb.curselection()
    str = ""
    for i in concu:
        str += group1[i] + "，"
    str = str[:len(str)-1]
    sv.set(str)

# 添加：选择结果按钮响应函数
def ad_res(lb, sv):
    concu = lb.curselection()
    for i in concu:
        sv.set(group_con_anim[i])

# 添加：清空按钮响应函数
def del_call(sv1, sv2, e1):
    sv1.set("")
    sv2.set("")
    e1.delete(0, END)

# 添加规则按钮响应函数
def add_call(top, sv1, sv2, num):
    if (not sv1.get()) or (not sv2.get()):
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先选择条件或结果！！！")
        return

    if num.isdigit():
        if (int(num) <= 0) or (int(num) > (len(group_all_rule) + 1)):
            messagebox.showwarning(parent=top, title="动物识别系统", message="添加位置超出范围！！！")
            return
    else:
        messagebox.showinfo(parent=top, title="动物识别系统", message="请在添加位置处输入数字！！！")
        return
        
    st = sv1.get() + " --> " + sv2.get() + "；\n"
    # 判断要添加的规则是否已经存在
    for each in group_all_rule:
        (e1, e2) = each
        if e2 == sv2.get():
            flag = True
            grp = sv1.get().split("，")
            for i in grp:
                if i not in e1:
                    flag = False
                    break
            for i in e1:
                if i not in grp:
                    flag = False
                    break
            if flag:
                st = "此规则已存在（第 "
                st += str(group_all_rule.index(each) + 1) + " 条）！！！"
                messagebox.showerror(parent=top, title="动物识别系统", message=st)
                return
    
    group_o_rule.insert(int(num)-1, st)
    add_file = open("files/rule.txt", 'w')
    add_file.writelines(group_o_rule)
    add_file.close()
    read_rule()
    update_group11()
    update_num()

    messagebox.showinfo(parent=top, title="动物识别系统", message="添加成功！！！")

# 删除规则弹出对话框
def callback11():
    top = Toplevel()
    top.title("删除规则")

    frame = Frame(top)
    frame.grid(row=0, column=0, columnspan=2, padx=30, pady=30, sticky=S)
    sb1 = Scrollbar(frame, orient=HORIZONTAL)
    sb1.pack(side=BOTTOM, fill=X)
    sb2 = Scrollbar(frame)
    sb2.pack(side=RIGHT, fill=Y)

    lb1 = Listbox(frame, listvariable=v11, width=50, height=10, \
            selectmode=EXTENDED, xscrollcommand=sb1.set, yscrollcommand=sb2.set)

    lb1.pack(side=LEFT, fill=BOTH)
    sb1.config(command=lb1.xview)
    sb2.config(command=lb1.yview)

    but1 = Button(top, text="删除", width=10, command=lambda:delete_call(top, lb1))
    but1.grid(row=1, column=0, pady=15, sticky=N)

    but2 = Button(top, text="取消", width=10, command=lambda:top.destroy())
    but2.grid(row=1, column=1, pady=15)

# 删除规则按钮响应函数
def delete_call(top, lb):
    cur = lb.curselection()

    if not cur:
        messagebox.showinfo(parent=top, title="动物识别系统", message="请先选择要删除的规则！！！")
        return
    
    messbox = messagebox.askokcancel(parent=top, title="动物识别系统", message="确定要删除选中的规则吗？")
    if not messbox:
        return
    
    cur1 = []
    for i in cur:
        cur1.insert(0,i)
    for i in cur1:
        lb.select_clear(i)
        group_o_rule.pop(i)
    add_file = open("files/rule.txt", 'w')
    add_file.writelines(group_o_rule)
    add_file.close()
    read_rule()
    update_group11()
    update_num()

# 添加规则按钮
button12 = Button(root, text="添加规则", width=12, command=callback12)
button12.grid(row=4, column=3, columnspan=3)
# 删除规则按钮
button11 = Button(root, text="删除规则", width=12, command=callback11)
button11.grid(row=4, column=6, columnspan=3)
# 退出系统按钮
button13 = Button(root, text="退出系统", width=12, command=lambda:root.quit())
button13.grid(row=5, column=6, columnspan=3)

mainloop()
