from tkinter import *

def pop(dir):
    ## 출력 리스트 생성
    expired = []
    plate = []
    confirmed = []
    for file in dir:
        name = file.path.split("/")[-1]
        if file.delete:
            if file.confirmed:
                expired.append(name)
            elif file.plate:
                plate.append(name)
        elif file.confirmed:
            confirmed.append(name)

    ## 창 생성
    window = Tk()
    window.title("Black_Eight")
    window.geometry("350x5000")
    window.resizable(width=False,height=False)
    
    text =Text(window)
    # text.insert(END, '\n  < 파일 목록 >  \n\n')
    text.insert(END, '\n  < 만료된 파일 목록 >  \n\n')
    for file in expired:
        text.insert(END, file)
        text.insert(END, "\n")

    text.insert(END, '\n  < 번호판 사진 목록 >  \n\n')
    for file in plate:
        text.insert(END, file)
        text.insert(END, "\n")
    text.insert(END, '\n\n  총 ')
 
    text.insert(END, len(expired) + len(plate))
    text.insert(END, ' 개의 이미지 파일이 삭제되었습니다.\n\n\n')

    text.insert(END, '\n  < 인가된 파일 목록 >  \n\n')
    for file in confirmed:
        text.insert(END, file)
        text.insert(END, "\n")
    text.insert(END, '\n\n  총 ')
 
    text.insert(END, len(confirmed))
    text.insert(END, ' 개의 이미지 파일이 남아있습니다.')


    text.pack()
    button = Button(text = "Quit", command = window.quit)
    button.pack()
    
    window.mainloop()           

