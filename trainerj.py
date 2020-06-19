
"""
Created on Thu May  7 09:09:15 2020

@author: Lenovo
"""

import numpy as np
import tkinter as tk
from tkinter import font
import subprocess

import os

from PIL import Image, ImageTk

from tkinter import filedialog  # Will be used to open the file from the user
import tkinter
from tflearn.layers.estimator import regression
#import tensorflow as tf
#import argparse
#import imutils 
from keras.models import load_model

import cv2 
from tkinter import messagebox


root = tk.Tk()
# global filename
root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\adith\.spyder-py3\dataset\Test",
                                           title="Select a file")


selectedimage = ImageTk.PhotoImage(Image.open(root.filename))
x= selectedimage
label1=tk.Label(image=selectedimage,text="1").pack()



def GraySclaedImage():
    print("GraySclaedImage")
    print(root.filename)
    image1 = cv2.imread(root.filename,1) 
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  #Conversion to gray scale
    cv2.imshow('Gray Scaled Image',img) #display the gray scale image
    b5.config(state=tk.NORMAL) 
    
    
    
def BinaryImage():
    print("BinaryImage")
    print(root.filename)
    img = cv2.imread(root.filename,1) 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_val = np.array([0,0,0])
    upper_val = np.array([179,255,127])
    # Threshold the HSV image to get only black colors
    mask = cv2.inRange(hsv, lower_val, upper_val) #All dark colors
    # invert mask to get black symbols on white backgr
    mask_inv = cv2.bitwise_not(mask) #Convert 
    # display image
    cv2.imshow("Binary Image", mask_inv)
    b3.config(state=tk.NORMAL)
    

    
    
    
def blackDotCount():
    '''print("Black dot counter")
    import subprocess
    result=subprocess.run(['python', 'dotCounter.py'],stdout=subprocess.PIPE)
    print(result.stdout)'''
    
    gray = cv2.imread(root.filename, 0)
    
    th, threshed = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU) #Getting gray scaled image to count black dot
    cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)[-2] #List of pixels having more than threshold value
# filter by area
    s1 = 3 #dimension of image s1 and s2
    s2 = 20
    xcnts = [] 
    for cnt in cnts: 
        if s1<cv2.contourArea(cnt) <s2: #Size of black dot to be considered
            xcnts.append(cnt) 
    print("\n             Number: of black dots in this mango : {}".format(len(xcnts)))
    messagebox.showinfo("Black dots", len(xcnts))
    b2.config(state=tk.NORMAL)

   
def testNow():
   
    print("Testing Mango")
    print(root.filename)
        
    result=subprocess.run(['python', 'predictj.py', '-i', root.filename ],stdout=subprocess.PIPE)
        #to call predictj.py file
    print(result.stdout)
    x=result.stdout[-11:-1]
        
    messagebox.showinfo("Mango Catogory",x)
   
    b4.config(state=tk.NORMAL)
    root.destroy()

    
    

root.title("SELECTED MANGO")
root.configure(background="black")
root.geometry("2500x2500")
heading = tk.Label(root, text="SELECTED MANGO")
f = tk.Frame(root, width=2500, height=500)



fnt2 = font.Font(family='Helvectica', size=10, weight='bold')
tk.Label(f, text="Selected Mango Picture", font=fnt2).grid(row=1, column=2)









b5 = tk.Button(f, text="Get Gray Scaled Image", fg="#31dbcd", bg="#313a39", font=fnt2,command=GraySclaedImage)
b5.grid(row=6, column=2, padx=10, pady=10, sticky='EWNS')
b5.bind("<Button 5>", GraySclaedImage)

b3=tk.Button(f,text="Get Binary Image",fg="#31dbcd",bg="#383a39",font=fnt2,command=BinaryImage)
b3.grid(row=12,column=2,padx=10,pady=10,sticky='EWNS')
b3.bind("<Button 3>",BinaryImage)

b2=tk.Button(f,text="Get Black Dot Count",fg="#31dbcd",bg="#383a39",font=fnt2,command=blackDotCount)
b2.grid(row=18,column=2,padx=10,pady=10,sticky='EWNS')
b2.bind("<Button 2>",blackDotCount)



b4=tk.Button(f,text="Test Now",fg="#31dbcd",bg="#383a39",font=fnt2,command=testNow)
b4.grid(row=24,column=2,padx=10,pady=10,sticky='EWNS')
b4.bind("<Button 4>",testNow)







f.pack()
tk.mainloop()


  
# using convert method for img2 """
"""img2 = selectedimage.convert("1") 
img2.show()"""