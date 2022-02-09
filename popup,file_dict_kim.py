from pickle import FRAME
from tkinter import *
from tkinter import messagebox
import os,cv2

window = Tk()
window.title("SKB")
window.geometry("600x300")

# 디렉토리 파일들 딕셔너리로 가져오기

def print_file(dir):
    file_list = []

    for path, dirs, files in os.walk(dir):
        for item in files:

            filename, fileExtension = os.path.splitext(item)
            b_filename = str(filename+fileExtension)
            b_hash_name = "".join(b_filename)
            file_list.append(b_hash_name)
    
    x = {'filename': file_list}
    return x
    

#팝업창

def Click ():
    messagebox.showinfo("알림창","알림이다")

listbox = Label(window, text =print_file(r'address'), bg="magenta", width=100, height=15,anchor=NW, wraplength=1500)
listbox.pack()

window.mainloop()



