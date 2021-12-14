from tkinter import*
from time import*

#변수 선언 부분
fnameList=["movie1.png"]
for i in range(2, 6):
    fnameList.append("movie"+str(i)+".png")
num=0

#함수 선언 부분
def clickNext():
    global num
    num+=1
    if num>4:
        num=0
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabelText.configure(text=fnameList[num]) #파일이름 출력하기 

def clickPrev():
    global num
    num-=1
    if num<0:
        num=4
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
window.geometry("1920x1080")
window.title("사진 앨범 보기")
window.configure(background="#333333")
#window 속성을 바꾸겠다는 뜻
#실무에선 다크그레이를 많이 사용한다고 한다.

#배경이미지 출력
bgphoto=PhotoImage(file="black2.png") #배경 이미지 준비
bg_Image=Label(window, image=bgphoto) #이미지 생성
bg_Image.place(x=-1, y=-1)#이미지 디스플레이 

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

btnPrev.place(x=500, y=650)
btnNext.place(x=1000, y=650)
pLabel.place(x=433, y=160)
pLabelText.place(x=743, y=650) #파일이름 출력하기 

window.mainloop()
