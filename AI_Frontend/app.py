
from tkinter import *
import cv2
from PIL import Image, ImageTk
import serial
import time



from test import *
# khai bao video
vid = cv2.VideoCapture(0)


width, height = 600, 400
#ket net arduino

arduino = serial.Serial(port='COM5' , baudrate=115200 ,timeout=.1)
arduino.readline()

# Set width and height

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# tao gui
app = Tk()
# app.attributes('-fullscreen', True)
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())

frameHeder = Frame(app)
frameHeder.pack()

frameCamera = Frame(frameHeder)
frameCamera.pack(side=LEFT , anchor=NW)

label_widget = Label(frameCamera)
label_widget.pack(fill=BOTH, expand=True)



#camera
def open_camera():
    global frame
    # Capture the video frame by frame
    _, frame = vid.read()

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)

    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)

    # Displaying photoimage in the label
    label_widget.photo_image = photo_image

    # Configure image in the label
    label_widget.configure(image=photo_image)
    # Repeat the same process after every 10 seconds
    label_widget.after(10, open_camera)
#write
def write_arduino(x):
    s = x +"\r"
    arduino.write(str(s).encode())
    data = arduino.readline()
    print(data)
#mo
def mo():
    write_arduino('mo')
    
#dong
def dong():
    write_arduino('dong')
#Tu Dong
check = False
def tuDong():
        if check:
            pass
        



#open_camera
open_camera()

# vi tri trang thai cac xe
frameViTri = Frame(frameHeder,width=80, height=40, background="red")
frameViTri.pack(side=RIGHT , anchor=NE )

frameViTri1 = Label (frameViTri ,text='1', height=12, width=40 , font=('Times', 9))
frameViTri1.grid(column=0 , row=0 )


frameViTri2 = Label(frameViTri,text='2' , height=12, width=40 , background="green", font=('Times', 9))
frameViTri2.grid(column=1 , row=0 )


frameViTri3 = Label(frameViTri,text='3' , height=12, width=40 , background="yellow", font=('Times', 9))
frameViTri3.grid(column=0 , row=1 )


frameViTri4 = Label(frameViTri ,text='4', height=12, width=40 , background="blue", font=('Times', 9))
frameViTri4.grid(column=1 , row=1 )


frameLichSu = Frame(app , background='blue')
frameLichSu.pack(side=RIGHT , expand=True , fill=BOTH)

#frameTinhNang
frameTinhNang = Frame(app, background='red')
frameTinhNang.pack(side=LEFT , expand=True , fill=BOTH)

trangThai = Label(frameTinhNang , text='Hello World',font=('Times' , 16))
trangThai.pack()
#Nut Bam
frameNut = Frame(frameTinhNang)
frameNut.pack()
buttonMo = Button(frameNut, text='Mo', height=4 , width=10 , command=mo)
buttonMo.grid(row=0 , column=0 ,sticky='w',padx=5 ,pady=5)
buttonDong = Button(frameNut, text='Dong' , height=4 , width=10, command=dong)
buttonDong.grid(row=0 , column=1 , sticky='n',padx=5 ,pady=5)
buttonTuDong = Button(frameNut, text='Tu Dong' , height=4 , width=10, command=lambda:nhan_dien_anh(frame))
buttonTuDong.grid(row=0 , column=2 , sticky='e',padx=5 ,pady=5)
frameViTri1.configure(text= "Da co xe")

# check vi tri
def checkVitri():
    doc = arduino.readline().decode().strip().strip('\n')
    if (doc == 'Mo1'):
        print(doc)
        frameViTri1.configure(text= "Da co xe o vi tri 1")
    if (doc == 'Tat1'):
        frameViTri1.configure(text= "Chua co xe o vi tri 1")
    
    if (doc == 'Mo2'):
        print(doc)
        frameViTri1.configure(text= "Da co xe o vi tri 2")
    if (doc == 'Tat2'):
        frameViTri1.configure(text= "Chua co xe o vi tri 2")
    
    if (doc == 'Mo3'):
        print(doc)
        frameViTri1.configure(text= "Da co xe o vi tri 3")
    if (doc == 'Tat3'):
        frameViTri1.configure(text= "Chua co xe o vi tri 3")

    if (doc == 'Mo4'):
        print(doc)
        frameViTri1.configure(text= "Da co xe o vi tri 4")
    if (doc == 'Tat4'):
        frameViTri1.configure(text= "Chua co xe o vi tri 4")
    frameViTri.after(100, checkVitri)
     
checkVitri()


app.mainloop()
