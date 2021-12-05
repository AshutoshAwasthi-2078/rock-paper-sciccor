import json
import cv2
import numpy as np
import pyautogui
import stopwat
import concurrent.futures


def play():
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
        if stopwat.run:
            img=pyautogui.screenshot()
            frame=np.array(img)
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            out.write(frame)
            #cv2.imshow("show",frame)
        if stopwat.room:
            if stopwat.zoom:
                break
            else:
                pass
        if stopwat.zoom:
            break

play()

'''with concurrent.futures.ProcessPoolExecutor() as executor:
    f1=executor.submit(stopwat.mnn,1)
    f2=executor.submit(play,1)
    f1.result()
    f2.result()'''