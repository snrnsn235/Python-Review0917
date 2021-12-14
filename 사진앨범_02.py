from tkinter import*
from time import*

#변수 선언 부분
fnameList=["jeju1.gif"]
for i in range(2, 10):
    fnameList.append("jeju"+str(i)+".gif")
num=0

#함수 선언 부분
def clickNext():
    global num
    num+=1
    if num>8:
        num=0
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabelText.configure(text=fnameList[num]) #파일이름 출력하기 

def clickPrev():
    global num
    num-=1
    if num<0:
        num=8
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabelText.configure(text=fnameList[num]) #파일이름 출력하기 

def pageUp(event):
    clickNext()
    
def pageDown(event):
    clickPrev()

#메인 코드 부분
window=Tk()
window.geometry("850x700")
window.title("사진 앨범 보기")
window.configure(background="#333333")
#window 속성을 바꾸겠다는 뜻
#실무에선 다크그레이를 많이 사용한다고 한다.

#배경이미지 출력
bgphoto=PhotoImage(file="album_bg.png") #배경 이미지 준비
bg_Image=Label(window, image=bgphoto) #이미지 생성
bg_Image.place(x=-2, y=-2)#이미지 디스플레이 

window.bind("<Prior>", pageUp)
window.bind("<Next>", pageDown)

#버튼에 입힐 이미지 준비
btnImgPrev=PhotoImage(file="album_butprev.png")
btnImgNext=PhotoImage(file="album_butnext.png")

#버튼에 이미지 적용
btnPrev=Button(window, image=btnImgPrev, command=clickPrev, bd=0, highlightthickness=0)
btnNext=Button(window, image=btnImgNext, command=clickNext, bd=0, highlightthickness=0)

'''
btnPrev=Button(window, image=photoList"<< 이전", command=clickPrev)
btnNext=Button(window, image=photoList"다음 >>", command=clickNext)
'''
photo=PhotoImage(file="gif/"+fnameList[0])
pLabel=Label(window, image=photo)

pLabelText=Label(window, text=fnameList[0]) #파일이름 출력하기 

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)
pLabelText.place(x=330, y=10) #파일이름 출력하기 

window.mainloop()
