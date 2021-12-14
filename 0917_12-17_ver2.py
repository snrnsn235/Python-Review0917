from tkinter import *


# 변수 선언 부분
#fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif","jeju5.gif","jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif"]

# 파일 네임 리스트를 for문으로 처리하기  
fnameList=["jeju1.gif"]
for i in range(2,10):
    fnameList.append("jeju"+str(i)+".gif")

num=0

# 함수 선언 부분
def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabelText.configure(text=fnameList[num]) # 파일이름 출력하기
    
def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabelText.configure(text=fnameList[num]) # 파일이름 출력하기

def pageUp(event) :
    clickNext()

def pageDown(event) :
    clickPrev()
    
# 메인 코드 부분
window = Tk()
window.geometry("700x510")
window.title("사진 앨범 보기")
window.configure(background="#333333") # 창 배경색 지정

window.bind("<Prior>",pageUp)
window.bind("<Next>",pageDown)

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="gif/" + fnameList[0])
pLabel= Label(window, image=photo)

pLabelText=Label(window, text=fnameList[0]) # 파일이름 출력하기

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)
pLabelText.place(x=330, y=10) #파일이름 출력하기



window.mainloop()
