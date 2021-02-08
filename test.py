# モジュールのインポート
import tkinter as tk
import tkinter.filedialog
import os

def file_selection():
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

# ウインドウ
root = tk.Tk()
root.title(u"Map Plot")
root.geometry("400x300")

# データ数入力
Static1 = tk.Label(text=u'最小')
Static1.place(x=5,y=5)
EditBox1 = tk.Entry(width=5)
EditBox1.place(x=100, y=5)

Static2 = tk.Label(text=u'最大')
Static2.place(x=5,y=30)
EditBox2 = tk.Entry(width=5)
EditBox2.place(x=100, y=30)



b = tk.Button(text='ファイル選択', command=file_selection)
b.pack()

c = tk.Button(text='Plot', command=file_selection)
c.pack()

d = tk.Button(text='Save', command=file_selection)
d.pack()

root.mainloop()