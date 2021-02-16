from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)

def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%d.%m.%Y")
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Готово!", "Файлы отсортированы успешно!")
        e_path.delete(0, END)
    else:
        messagebox.showwarning("Внимание!", "Выберите папку с фотографиями!")

root = Tk()
root.geometry('500x90')
root.title('Cортировка фотографий')
root.config(bg='#C0C0C0')
root.resizable(FALSE, FALSE)

frame = Frame(root, bg="#708090", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=10)

btn_start = ttk.Button(root, text="Начать сортировку", command=f_start)
btn_start.pack(fill=X, padx=10)


root.mainloop()