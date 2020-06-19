# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:07:47 2020

@author: Lenovo
"""

import tkinter as tk  #frontend desigm
from tkinter import font
import os #To give filenname/ open command prompt
from tkinter import filedialog #filename input
from PIL import ImageTk,Image #display images(background)

def trainer(event):  
    os.system('python trainerj.py')
    b1.config(state=tk.NORMAL)

def training():
    print("Training is done")
    os.system('python cnnj.py')
    b2.config(state=tk.NORMAL)
    



    
def close_window():
    root.destroy()


root=tk.Tk()  #object of Tkinter
root.title("DETECTION OF DISEASE INFECTED MANGOES USING MACHINE LEARNING TECHNIQUES")
image2=Image.open(r'C:\Users\adith\.spyder-py3\FF.png') #heading mango image
image1 = ImageTk.PhotoImage(image2) #open the mango image and display
root.configure(background="white") #yellow background
root.geometry("2500x2500") #window size 
heading =tk.Label(root, text="DETECTION OF DISEASE INFECTED MANGOES USING MACHINE LEARNING TECHNIQUES", )
#img = ImageTk.PhotoImage(Image.open("bb.jpg"))


f=tk.Frame(root,width=2500,height=500) 


fnt1=font.Font(family='Helvectica', size=15,weight='bold')
fo=font.Font(family='Times New Roman',size=15,weight='bold')

fnt2=font.Font(family='Helvectica', size=10,weight='bold')
tk.Label(f,text="DETECTION OF DISEASE INFECTED MANGOES USING MACHINE LEARNING TECHNIQUES",font=fo).grid(row=1,column=2) #Frame heading



b2=tk.Button(f,text="Training",fg="#31dbcd",bg="#383a39",command=training,font=fnt2)
b2.grid(row=6,column=2,padx=10,pady=10,sticky='EWNS')
b2.bind("<Button 2>",training)

b1=tk.Button(f,text="Select a mango",fg="#31dbcd",bg="#313a39",font=fnt2,command=trainer)
b1.grid(row=9,column=2,padx=10,pady=10,sticky='EWNS')
b1.bind("<Button 1>",trainer)


b4=tk.Button(f,text="Exit",fg="#31dbcd",bg="#383a39",command=close_window,font=fnt2)
b4.grid(row=15,column=2,padx=10,pady=10,sticky='EWNS')
b4.bind("<Button 4>",close_window)

canvas = tk.Canvas(root, width = 820, height =400) #background image
canvas.pack()
img = ImageTk.PhotoImage(Image.open("FF.png"))
canvas.create_image(1,1, anchor=tk.NW, image=img)
#f.configure(background='white')
f.pack()

tk.mainloop()