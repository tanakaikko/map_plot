# モジュールのインポート
import os, tkinter.filedialog, tkinter.messagebox
from tkinter.constants import E, LEFT, W
import tkinter as tk
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

save_fig = False
min_value = 0
max_value = 10
file = ''
#txt_1.get()
def map_plot():
    global save_fig,min_value,max_value
    try:
        min_value = int(EditBox1.get())
        max_value = int(EditBox2.get())

        label_size = 24

        data = np.loadtxt(file, delimiter=',',encoding="utf-8_sig")

        fig = plt.figure(figsize=(15,15))

        ax = fig.add_subplot(1,1,1)
        #,extent=[0, 8, 0, 8]
        im1 = ax.imshow(np.log10(data),cmap='Oranges',vmin=min_value,vmax=max_value)
        #ax1.set_xlabel(r"x Length [$\rm \mu m$]", size = x_y_label_size, weight = "light")
        #ax1.set_ylabel(r"y Length [$\rm \mu m$]", size = x_y_label_size, weight = "light")
        ax.tick_params(labelsize=18)

        divider1 = make_axes_locatable(ax)
        cax1 = divider1.append_axes("right", size="5%", pad=0.1)
        cbar1=fig.colorbar(im1,cax=cax1)
        cbar1.ax.tick_params(labelsize=18)
        #cbar1.set_label(r'Electron density [$\rm m^{-2}$]',size=label_size)

        #fig.suptitle('time: %.1e [s]'%((time+1)*delta_t),fontsize=27,y=0.7)
        if save_fig:
            save_file = file.replace('.csv','.png') 
            fig.savefig(save_file)
        plt.show()
        save_fig = False
    except:
        print('err')

def save_fig_switch():
    global save_fig

    save_fig = True

def file_selection():
    global file
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

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

c = tk.Button(text='Plot', command=map_plot)
c.pack()

d = tk.Button(text='Save', command=save_fig_switch)
d.pack()

root.mainloop()