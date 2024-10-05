import random
from tkinter import *
import time
class REZA:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-1
        self.height=500
        self.width=500

        self.hit_bottom = False

    def TNT(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=2
        if pos[3]>=self.height:

            self.hit_bottom = True
            self.canvas.create_text(250,200, text='Game Over',font=(None,20))
            
            
        if self.hit_paddle(pos)==True:
            self.y = -2
        if pos[0]<=0:
            self.x=2
        if pos[2] >= self.width:
            self.x=-2

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
class reza:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.width=500
        self.canvas.bind_all('<KeyPress-Left>',self.left)
        self.canvas.bind_all('<KeyPress-Right>',self.Right)
    def A1391(self):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 and self.x < 0:
            self.x = 0
        if pos[2] >= self.width and self.x >0:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    def left(self, evt):
        self.x = -2
    def Right(self, evt):
        self.x = 2

S = Tk()
S.geometry('500x500')
S.title('Game')
S.resizable(0,0)
W = 500
H = 320
S.wm_attributes('-topmost', -1)

cv = Canvas(S, width=500, height=500, bg='white', highlightthickness= 0)
cv.pack()

Y1394=reza(cv,'blue')
ob=REZA(cv,Y1394,'red')

while 1:
    if ob.hit_bottom == False:
        ob.TNT()
        Y1394.A1391()
    S.update_idletasks()
    S.update()
    time.sleep(0.01)
