from tkinter import *

def pop(dir):
   
    window = Tk()
    window.title("Black_Eight")
    window.geometry("350x350")
    window.resizable(width=False,height=False)
    
    text =Text(window)
    text.insert(END, '\n  < 파일 목록 >  \n\n')
    text.insert(END, dir)
    text.insert(END, '\n\n\n  총 ')
 
    text.insert(END, len(dir))
    text.insert(END, ' 개의 이미지 파일이 남아있습니다.')
    text.pack()
    button = Button(text = "Quit", command = window.quit)
    button.pack()
    
    window.mainloop()           

