import tkinter
import tkinter.ttk
from typing import Text
import tkinter.messagebox

#class inven_list():
#    def __init__(self)

cur_inven_label=None
cur_inven_line=-1
fo = open(".\\data\\store.txt", "r", encoding="utf8")
file_str = fo.readlines()


add_list_info = ""
# 처음 제품 목록 불러오기
def loading_file():
    root_geometry = ""
    for i in file_str[0]:
        if i == '\n':
            break
        root_geometry+=i
    root.geometry(root_geometry)
    for line in file_str:
        string = ""
        i = ""
        for i in line:
            if i == '=':
                pro_list.insert("end", string)
                pro_list.bind('<Double-Button-1>', load_inven)
                break
            string += i


class add_inven():
# 제품 인벤 추가
    def __init__(self):
        if cur_inven_line == -1:
            return
        self.add_inven_window = tkinter.Tk()
        self.add_inven_window.title("인벤 추가")
        self.add_inven_window.geometry('350x150+{}+{}'.format(root.winfo_rootx() + root.winfo_width() // 4, root.winfo_rooty() + root.winfo_height() // 4))
        self.add_inven_window.resizable(False, False)
        
        tkinter.Label(self.add_inven_window).pack()

        self.win_fra = tkinter.Frame(self.add_inven_window)
        self.add_inven_entry_name = tkinter.Entry(self.win_fra, width=10)
        self.add_inven_entry_num2 = tkinter.Entry(self.win_fra, width=5)
        self.add_inven_entry_name.bind('<Return>', self.add_inven_ch2)
        self.add_inven_entry_num2.bind('<Return>', self.add_inven_ch2)

        tkinter.Label(self.win_fra, text="이름 ").pack(side="left")
        self.add_inven_entry_name.pack(side="left")

        tkinter.Label(self.win_fra, text="    현재 ").pack(side="left")
        self.add_inven_entry_num2.pack(side="left")

        tkinter.Label(self.win_fra, text=" 개수").pack(side="left")
        self.add_inven_btn = tkinter.Button(self.add_inven_window, command=self.add_inven_ch1, text='▶')

        self.win_fra.pack()
        tkinter.Label(self.add_inven_window).pack()

        self.add_inven_btn.pack()
    
    def add_inven_ch1(self):
        data = self.add_inven_entry_name.get().strip()
        num2 = self.add_inven_entry_num2.get().strip()
        print(file_str)
        if (not data) | (not num2):
            return

        if file_str[cur_inven_line].find(data + ":") != -1:
            tkinter.messagebox.showerror("중복 오류", "제품명의 중복을 허용하지 않습니다.")
            self.add_inven_window.destroy()
            return

        pro_str = data + ":" + num2 + ";"
        file_str[cur_inven_line] = file_str[cur_inven_line].replace('\n', pro_str + '\n')
        inven_list.insert("end", data + "      " + num2)
        self.add_inven_window.destroy()
        print(file_str)
        save_file()

    def add_inven_ch2(self, entry):
        data = self.add_inven_entry_name.get().strip()
        num2 = self.add_inven_entry_num2.get().strip()

        if (not data) | (not num2):
            return
        
        if file_str[cur_inven_line].find(data + ":") != -1:
            tkinter.messagebox.showerror("중복 오류", "제품명의 중복을 허용하지 않습니다.")
            self.add_inven_window.destroy()
            return

        pro_str = data + ":" + num2 + ";"
        file_str[cur_inven_line] = file_str[cur_inven_line].replace('\n', pro_str + '\n')
        inven_list.insert("end", data + "      " + num2)
        self.add_inven_window.destroy()
        save_file()

class add_li():
# 제품 리스트 추가
    def __init__(self):
        self.add_list_window = tkinter.Tk()
        self.add_list_window.title("제품 추가")
        self.add_list_window.geometry('300x150+{}+{}'.format(root.winfo_rootx() + root.winfo_width() // 4, root.winfo_rooty() + root.winfo_height() // 4))
        self.add_list_window.resizable(False, False)
        
        self.add_list_entry = tkinter.Entry(self.add_list_window)
        tkinter.Label(self.add_list_window).pack()
        tkinter.Label(self.add_list_window, text="제품명").pack()
        self.add_list_entry.bind('<Return>', self.add_list_ch2)
        self.add_list_entry.pack()
        self.add_list_btn = tkinter.Button(self.add_list_window, command=self.add_list_ch1, text='▶')

        tkinter.Label(self.add_list_window).pack()
        self.add_list_btn.pack()

    def add_list_ch1(self):
        data = self.add_list_entry.get().strip()
        if not data:
            return
        pro_str = ""
        for line in range(len(file_str)):
            for i in file_str[line]:
                if i == "=" or i == "\n" or i == "#":
                    break
                else:
                    pro_str += i
            if pro_str == data:
                tkinter.messagebox.showerror("중복 오류", "제품명의 중복을 허용하지 않습니다.")
                self.add_list_window.destroy()
                return
            else:
                pro_str = ""
        file_str.append(data + '=' + '\n')
        pro_list.insert("end", data)
        pro_list.bind('<Double-Button-1>', load_inven)
        self.add_list_window.destroy()
        save_file()

    def add_list_ch2(self, entry):
        data = self.add_list_entry.get()
        if not data:
            return
        pro_str = ""
        for line in range(len(file_str)):
            for i in file_str[line]:
                if i == "=" or i == "\n" or i == "#":
                    break
                else:
                    pro_str += i
            if pro_str == data:
                tkinter.messagebox.showerror("중복 오류", "제품명의 중복을 허용하지 않습니다.")
                self.add_list_window.destroy()
                return
            else:
                pro_str = ""
        file_str.append(data + '=' + '\n')
        pro_list.insert("end", data)
        pro_list.bind('<Double-Button-1>', load_inven)
        self.add_list_window.destroy()
        save_file()

class inven_title():
    def __init__(self):
        self.text = tkinter.StringVar()
        self.text.set("제품을 선택해 주세요.")
        self.inven_title_label = tkinter.Label(root, textvariable=self.text).pack(side="top")
    def change(self, data):
        data = pro_list.get(data)
        self.text.set(data)
        global cur_inven_label
        cur_inven_label = data
        pro_str = ""
        for k in range(len(file_str)):
            for i in file_str[k]:
                if i == "=" or i == "\n" or i == "#":
                    break
                else:
                    pro_str += i
            if pro_str == cur_inven_label:
                break
            else:
                pro_str = ""
        global cur_inven_line
        cur_inven_line = k

class edit_inven_li():
# 제품 리스트 삭제
    def __init__(self, n):
        self.edit_inven_window = tkinter.Tk()
        self.edit_inven_window.title("인벤 편집")
        self.edit_inven_window.geometry('300x150+{}+{}'.format(root.winfo_rootx() + root.winfo_width() // 4, root.winfo_rooty() + root.winfo_height() // 4))
        self.edit_inven_window.resizable(False, False)
        
        self.data = inven_list.get(inven_list.curselection())
        k = len(self.data) - 1
        i = self.data[k]
        self.num = ""
        while i != ' ':
            self.num = i + self.num
            k -= 1
            i = self.data[k]
        tkinter.Label(self.edit_inven_window).pack()
        self.edit_inven_entry = tkinter.Entry(self.edit_inven_window)
        self.edit_inven_entry.insert(0, self.num)
        self.edit_inven_entry.bind('<Return>', self.edit_inven_ch2)
        self.edit_inven_entry.pack()
        self.edit_inven_btn = tkinter.Button(self.edit_inven_window, command=self.edit_inven_ch1, text='▶')

        tkinter.Label(self.edit_inven_window).pack()
        self.edit_inven_btn.pack()

    def edit_inven_ch1(self):
        self.data = self.data.replace("      ", ":")
        af_data = self.data.replace(":" + self.num, ":" + self.edit_inven_entry.get().strip())
        file_str[cur_inven_line] = file_str[cur_inven_line].replace(self.data, af_data)
        
        self.edit_inven_window.destroy()

        fistr = file_str[cur_inven_line]
        lastr = ""
        num = 0
        i = None
        inven_list.delete(0, 'end')
        while i != '=':
            i = fistr[num]
            num += 1
        while i != '\n':
            i = fistr[num]
            if i == ';':
                inven_list.insert("end", lastr)
                lastr = ""
            elif i == ':':
                lastr += '      '
            else:
                lastr += i
            num += 1
        inven_list.pack(fill="both", expand=True)
        inven_list.bind('<Double-Button-1>', edit_inven_li)

        save_file()

    def edit_inven_ch2(self, entry):
        self.data = self.data.replace("      ", ":")
        af_data = self.data.replace(":" + self.num, ":" + self.edit_inven_entry.get().strip())
        file_str[cur_inven_line] = file_str[cur_inven_line].replace(self.data, af_data)
        
        self.edit_inven_window.destroy()

        fistr = file_str[cur_inven_line]
        lastr = ""
        num = 0
        i = None
        inven_list.delete(0, 'end')
        while i != '=':
            i = fistr[num]
            num += 1
        while i != '\n':
            i = fistr[num]
            if i == ';':
                inven_list.insert("end", lastr)
                lastr = ""
            elif i == ':':
                lastr += '      '
            else:
                lastr += i
            num += 1
        inven_list.pack(fill="both", expand=True)
        inven_list.bind('<Double-Button-1>', edit_inven_li)

        save_file()

def edit_pro():
    data = pro_list.get(pro_list.curselection())
    pro_list.delete(pro_list.curselection())
    
    for line in range(len(file_str)):
        string = ""
        i = ""
        for i in file_str[line]:
            if i == '=':
                if data == string:
                    del file_str[line]
                    save_file()
                    return
                else:
                    break
            string += i

# 인벤 불러오기
def load_inven(data):
    i_title.change(pro_list.curselection())
    fistr = file_str[cur_inven_line]
    lastr = ""
    num = 0
    i = None
    inven_list.delete(0, 'end')
    while i != '=':
        i = fistr[num]
        num += 1
    try:
        while i != '\n':
            i = fistr[num]
            if i == ';':
                inven_list.insert("end", lastr)
                lastr = ""
            elif i == ':':
                lastr += '      '
            else:
                lastr += i
            num += 1
    except:
        return
    inven_list.pack(fill="both", expand=True)
    inven_list.bind('<Double-Button-1>', edit_inven_li)

# 인벤 편집
def edit_inven():
    data = inven_list.get(inven_list.curselection()).replace("      ", ":") + ';'
    inven_list.delete(inven_list.curselection())
    file_str[cur_inven_line] = file_str[cur_inven_line].replace(data, "")
    save_file()
    
# 인벤 +-1
p_m_index = -1

def inven_plus():
    try:
        index = min(inven_list.curselection())
    except:
        index = None
    global p_m_index
    if index == None:
        index = p_m_index
    else:
        p_m_index = index

    data = inven_list.get(index).replace("      ", ":")
    k = len(data) - 1
    i = data[k]
    num = ""
    while i != ':':
        num = i + num
        k -= 1
        i = data[k]
    af_num = str(int(num) + 1)
    af_data = data.replace(":" + num, ":" + af_num)
    file_str[cur_inven_line] = file_str[cur_inven_line].replace(data, af_data)

    fistr = file_str[cur_inven_line]
    lastr = ""
    num = 0
    i = None
    inven_list.delete(0, 'end')
    while i != '=':
        i = fistr[num]
        num += 1
    while i != '\n':
        i = fistr[num]
        if i == ';':
            inven_list.insert("end", lastr)
            lastr = ""
        elif i == ':':
            lastr += '      '
        else:
            lastr += i
        num += 1
    inven_list.pack(fill="both", expand=True)
    inven_list.bind('<Double-Button-1>', edit_inven_li)
    inven_list.activate(index)

    save_file()

def inven_minus():
    try:
        index = min(inven_list.curselection())
    except:
        index = None
    global p_m_index
    if index == None:
        index = p_m_index
    else:
        p_m_index = index

    data = inven_list.get(index).replace("      ", ":")
    k = len(data) - 1
    i = data[k]
    num = ""
    while i != ':':
        num = i + num
        k -= 1
        i = data[k]
    af_num = str(int(num) - 1)
    af_data = data.replace(":" + num, ":" + af_num)
    file_str[cur_inven_line] = file_str[cur_inven_line].replace(data, af_data)

    fistr = file_str[cur_inven_line]
    lastr = ""
    num = 0
    i = None
    inven_list.delete(0, 'end')
    while i != '=':
        i = fistr[num]
        num += 1
    while i != '\n':
        i = fistr[num]
        if i == ';':
            inven_list.insert("end", lastr)
            lastr = ""
        elif i == ':':
            lastr += '      '
        else:
            lastr += i
        num += 1
    inven_list.pack(fill="both", expand=True)
    inven_list.bind('<Double-Button-1>', edit_inven_li)
    inven_list.activate(index)

    save_file()

def save_file():
    save_string = ""
    for i in file_str:
        save_string += i
    fw = open(".\\data\\store.txt", "w", encoding="utf8")
    fw.write(save_string)

# gui 시작
root = tkinter.Tk()                 
root.title("재고 처리")


##########################################################

# 선택된 제품 라벨
i_title = inven_title()

# 제품 리스트
pro_frame = tkinter.Frame(root, borderwidth=1)
pro_frame.pack(side="left", fill="both", expand=True)

pro_bar = tkinter.Scrollbar(pro_frame)
pro_bar.pack(side="right", fill="y")

pro_list = tkinter.Listbox(pro_frame, yscrollcommand=pro_bar.set)
pro_list.pack(fill="both", expand=True)
pro_bar["command"]=pro_list.yview

loading_file()


# 오른쪽 재고
inven_frame = tkinter.Frame(root, borderwidth=1)
inven_frame.pack(side="left", fill="both", expand=True)

inven_bar = tkinter.Scrollbar(inven_frame)
inven_bar.pack(side="right", fill="y")

inven_list = tkinter.Listbox(inven_frame, yscrollcommand=inven_bar.set)
inven_list.pack(fill="both", expand=True)
inven_bar["command"]=inven_list.yview
#########################################################

# 제품 추가 버튼 프레임
file_frame = tkinter.Frame(pro_frame)                    
file_frame.pack(fill="both")

add_list_btn = tkinter.Button(file_frame, padx = 5, pady = 5, width = 12, text="제품 추가", command=add_li)
add_list_btn.pack(side="left")

# 제품 삭제 버튼
add_list_btn = tkinter.Button(file_frame, padx = 5, pady = 5, width = 12, text="제품 삭제", command=edit_pro)
add_list_btn.pack(side="left")

# inven 추가 버튼
add_inven_btn = tkinter.Button(inven_frame, padx = 5, pady = 5, width = 12, text="인벤 추가", command=add_inven)
add_inven_btn.pack(side="left")

del_inven_btn = tkinter.Button(inven_frame, padx = 5, pady = 5, width = 12, text="인벤 삭제", command=edit_inven)
del_inven_btn.pack(side="left")

del_inven_btn = tkinter.Button(inven_frame, padx = 5, pady = 5, width = 3, text="▲", command=inven_plus)
del_inven_btn.pack(side="left")

del_inven_btn = tkinter.Button(inven_frame, padx = 5, pady = 5, width = 3, text="▼", command=inven_minus)
del_inven_btn.pack(side="left")

root.mainloop()