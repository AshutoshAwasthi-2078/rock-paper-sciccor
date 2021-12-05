from tkinter import *
import json
import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime
from multiprocessing import Process
zoom=False
room=False
running=False
class window(Tk):
    def __init__(self):
        super(window,self).__init__()

        self.title("tkinter first")
        self.minsize(500, 400)
        #self.wm_iconbitmap("myicon.ico")
        #self.createlable()
        #self.title("screenrecord")
        #self.minsize(width=250, height=70)
        self.create_layout()


    def create_layout(self):


        #root = Tk()


        now = datetime.now().time()  # time object

        print("now =", now)

        mark = Label(self, text="Welcome!", fg="black", font="Verdana 30 bold")
        mark.pack()
        f = Frame(self)
        rn =Button(f, text='Start', width=6, command=lambda: self.Run())
        pause = Button(f, text='Stop', width=6, command=self.Pause())
        cut = Button(f, text='Reset', width=6, command=lambda: self.Cut())
        f.pack(anchor='center', pady=5)
        rn.pack(side="left")
        pause.pack(side="left")
        cut.pack(side="left")





    def Run(self):
        global running
        running = True
        #self.play()

    def Pause(self):
        global zoom
        zoom = True

    def Cut(self):
        global room
        room = True



def play():


    now = datetime.now().time()  # time object

    print("now =", now)

    with open('listfile.txt', 'r') as filehandle:
        basicList = json.load(filehandle)
        print(basicList)

    file = open('listfile.txt', "r+")
    file.truncate(0)
    file.close()

    with open('listfile.txt', 'w') as filehandle:
        json.dump(basicList + 1, filehandle)
        dp = basicList + 1
        nam = ("output {}.avi".format(dp))
        print(nam)
        print('2')

    screen_size = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    print('3')
    out = cv2.VideoWriter(nam, fourcc, 20.0, (screen_size))

    while True:
        if zoom:
            if room:
                break
            else:
                time.sleep(0.5)
        elif room:
            break
        elif running:


            now = datetime.now().time()  # time object

            print("now =", now)
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            # cv2.imshow("show",frame)


        now = datetime.now().time()  # time object

        print("now =", now)





def go():
    cl=window()
    cl.mainloop()



if __name__ == '__main__':
    Process(target=go()).start()
    if running:
        Process(target=play()).start()



    now = datetime.now().time()  # time object

    print("now =", now)

'''import json
import cv2
import numpy as np
import pyautogui


def play(zoom,room):
    with open('listfile.txt', 'r') as filehandle:
        basicList = json.load(filehandle)
        print(basicList)

    file = open('listfile.txt', "r+")
    file.truncate(0)
    file.close()

    with open('listfile.txt', 'w') as filehandle:
        json.dump(basicList+1, filehandle)
        dp=basicList+1
        nam = ("output {}.avi".format(dp))
        print(nam)
        print('2')


    screen_size=(1920,1080)
    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    print('3')
    out=cv2.VideoWriter(nam,fourcc,20.0,(screen_size))


    def ookkk():
        pass
    while True:
        img=pyautogui.screenshot()
        frame=np.array(img)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        #cv2.imshow("show",frame)
        if room:
            while True:
                1<3
        if zoom:
            break



'''