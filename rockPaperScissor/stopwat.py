import tkinter as Tkinter
from datetime import datetime


counter = 66600
running = False
zoom =False
room = False
run=False

def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the intial delay.
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            label['text'] = display
            label.after(1000,count)
            counter += 1
# Triggering the start of the counter.
    count()
#screen_record.play()

# start function of the stopwatch
def Start(label):
    global zoom
    zoom = False
    global room
    room = False
    global running
    running = True
    global run
    run =True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'disabled'


# Stop function of the stopwatch
def Stop():
    global running
    global zoom
    zoom = False
    global room
    room=True
    global run
    run = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# Reset function of the stopwatch
def Reset(label):
    global zoom
    zoom = True
    global room
    room = False
    global counter
    counter = 66600
    global run
    run = False
    # If rest is pressed after pressing stop.
    if running == False:
        start['state'] = 'normal'
        label['text'] = 'Welcome!'
        print('na')

    # If reset is pressed while the stopwatch is running.

    else:
        running == False
        label['text'] = 'Welcome!'
        reset['state'] = 'disabled'
        start['state'] = 'normal'
        stop['state'] = 'disabled'
        print('ha')
        ok()

def ok():
    global running
    running == False



root = Tkinter.Tk()
root.title("screenrecord")
root.minsize(width=250, height=70)
mark = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
mark.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(mark))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda:Reset(mark))
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
def mnn():
    root.mainloop()

mnn()