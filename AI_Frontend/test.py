import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import mysql.connector


def nhan_dien_anh(resize):
    img = resize
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(gray)
    text = ''
    for x in result:
        text = text + " " + x[1].strip()
    text = text.strip()
    print(text)

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Lam2002",
#     database="iot_thay_duc"
# )

# mycursor = mydb.cursor()
# cap = cv2.VideoCapture(0)

# while (True):
#     ret, frame = cap.read()
#     resize = cv2.resize(frame, (600, 400))
#     cv2.imshow('manhinh', resize)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         try:
#             text = nhan_dien_anh( frame)
#             print(text)
#             sql = "Select * from customers Where bien_xe = %s"

#             mycursor.execute(sql, (text,))
#             myresult = mycursor.fetchall()
#             if myresult == []:
#                 sql = "Insert into customers (bien_xe, status) values(%s , %s)"
#                 mycursor.execute(sql, (text, 1))
#                 mydb.commit()
#                 print("Xin moi vao")
#             else:
#                 status = myresult[0][2]
#                 print(status)
#                 sql = "UPDATE customers SET status = %s WHERE bien_xe = %s"
#                 if status == 1:
#                     mycursor.execute(sql , (0 , text))
#                     print('Xin moi ra')
#                 else:
#                     mycursor.execute(sql , (1 , text))
#                     print('Xin moi vao')

#                 mydb.commit()
#         except:
#             print("Chua nhan dien duoc bien so")

