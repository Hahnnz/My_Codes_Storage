from Tkinter import *
import Tkinter
import ttk
import cv2
import PIL
import os
import glob
import numpy as np
import argparse
from PIL import ImageTk, Image

Dataset_root="./MET Data Set"

def get_filename(fulllocation):
    i=1
    while True:
        if fulllocation[-i] is not "/":i += 1
        else:
            name=fulllocation[-(i-1):]
            break
    return name

def explore_dir(dir,count=0):
    if count==0:
        global n_dir, n_file, filenames, filelocations
        n_dir=n_file=0
        filenames=filelocations=np.array([])
    for img_path in sorted(glob.glob(os.path.join(dir,'*'))):
        if os.path.isdir(img_path):
            n_dir +=1
            explore_dir(img_path,count+1)
        elif os.path.isfile(img_path):
            n_file += 1
            loc=np.array([img_path])
            name=np.array([get_filename(img_path)])
            filelocations=np.concatenate((filelocations, loc), axis=0)
            filenames=np.concatenate((filenames, name), axis=0)
    return np.array([filenames,filelocations])

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        self.scale("all",0,0,wscale,hscale)

def create_canvas(name):
	dataset=explore_dir(Dataset_root,0)
	myshare=[["" for cols in range(20)]for rows in range(2)]
	max_size=np.array([0,0])

	count=0

	if name=="jsw": count = 1
	elif name=="ksy": count = 2
	elif name=="jwj": count = 3
	elif name=="pyj": count = 4
	elif name=="yyg": count = 5
	elif name=="pbr": count = 6
	elif name=="cej": count = 7
	elif name=="hjh": count = 8

	start = (count * 20)- 20
	end = (count * 20) - 1

	print start,end

	for i in range(2):
		for j in range(20):
			myshare[i][j]=dataset[i][j+start]
	for i in range(20):
		testimg=cv2.imread(myshare[1][i])
		if testimg.shape[0]>max_size[0]: max_size[0]=testimg.shape[0]
		if testimg.shape[1]>max_size[1]: max_size[1]=testimg.shape[1]



	root = Tk()

	buttonframe=Frame(root)
	canvasframe=Frame(root)
	clearbuttonframe=Frame(root)

 	buttonframe.pack(ipadx=0,ipady=0,side="left")
 	canvasframe.pack(ipadx=0,ipady=0,side="left")

 	coor=StringVar(root,value='')
 	coor_entry=ttk.Entry(root,textvariable=coor,width=20)
 	coor_entry.pack(side="left")

	canvas = Canvas(canvasframe,width=max_size[1],heigh=max_size[0])
	canvas.pack()

	def imgimg(canvas,imgimg_name):
		canvas.delete("all")
		img1=cv2.imread(imgimg_name)
		HEIGHT,WIDTH = img1.shape[:-1]
		canvas = Canvas(canvas,width=WIDTH,heigh=HEIGHT)
		canvas.place(x=0,y=0)
		img2=ImageTk.PhotoImage(file=imgimg_name)
		canvas.create_image(0,0,image=img2,anchor="nw")

		def down(event):
		  global x0,y0;
		  x0, y0 = event.x, event.y
		  if(x0,y0) == (event.x,event.y):
		    canvas.create_oval(x0-2,y0-2,event.x+2,event.y+2,outline="red",fill="red",width=2)
		def up(event):
		  global x0, y0
		  if(x0,y0) == (event.x,event.y):
		    canvas.create_oval(x0-2,y0-2,event.x+2,event.y+2,outline="red",fill="red",width=2)
		  coor_entry.delete(0,"end")
		  coor_entry.insert("end","("+str(x0)+","+str(y0)+")")
		  print ("("+str(x0)+","+str(y0)+")")
		canvas.bind("<Button-1>",down) 
		canvas.bind("<ButtonRelease>",up) 
		root.mainloop()

	b_1=Button(buttonframe,text=myshare[0][0],command= lambda: imgimg(canvas,myshare[1][0])).pack(side="bottom",anchor="nw")
	b_2=Button(buttonframe,text=myshare[0][1],command= lambda: imgimg(canvas,myshare[1][1])).pack(side="bottom",anchor="nw")
	b_3=Button(buttonframe,text=myshare[0][2],command= lambda: imgimg(canvas,myshare[1][2])).pack(side="bottom",anchor="nw")
	b_4=Button(buttonframe,text=myshare[0][3],command= lambda: imgimg(canvas,myshare[1][3])).pack(side="bottom",anchor="nw")
	b_5=Button(buttonframe,text=myshare[0][4],command= lambda: imgimg(canvas,myshare[1][4])).pack(side="bottom",anchor="nw")
	b_6=Button(buttonframe,text=myshare[0][5],command= lambda: imgimg(canvas,myshare[1][5])).pack(side="bottom",anchor="nw")
	b_7=Button(buttonframe,text=myshare[0][6],command= lambda: imgimg(canvas,myshare[1][6])).pack(side="bottom",anchor="nw")
	b_8=Button(buttonframe,text=myshare[0][7],command= lambda: imgimg(canvas,myshare[1][7])).pack(side="bottom",anchor="nw")
	b_9=Button(buttonframe,text=myshare[0][8],command= lambda: imgimg(canvas,myshare[1][8])).pack(side="bottom",anchor="nw")
	b_10=Button(buttonframe,text=myshare[0][9],command= lambda: imgimg(canvas,myshare[1][9])).pack(side="bottom",anchor="nw")
	b_11=Button(buttonframe,text=myshare[0][10],command= lambda: imgimg(canvas,myshare[1][10])).pack(side="bottom",anchor="nw")
	b_12=Button(buttonframe,text=myshare[0][11],command= lambda: imgimg(canvas,myshare[1][11])).pack(side="bottom",anchor="nw")
	b_13=Button(buttonframe,text=myshare[0][12],command= lambda: imgimg(canvas,myshare[1][12])).pack(side="bottom",anchor="nw")
	b_14=Button(buttonframe,text=myshare[0][13],command= lambda: imgimg(canvas,myshare[1][13])).pack(side="bottom",anchor="nw")
	b_15=Button(buttonframe,text=myshare[0][14],command= lambda: imgimg(canvas,myshare[1][14])).pack(side="bottom",anchor="nw")
	b_16=Button(buttonframe,text=myshare[0][15],command= lambda: imgimg(canvas,myshare[1][15])).pack(side="bottom",anchor="nw")
	b_17=Button(buttonframe,text=myshare[0][16],command= lambda: imgimg(canvas,myshare[1][16])).pack(side="bottom",anchor="nw")
	b_18=Button(buttonframe,text=myshare[0][17],command= lambda: imgimg(canvas,myshare[1][17])).pack(side="bottom",anchor="nw")
	b_19=Button(buttonframe,text=myshare[0][18],command= lambda: imgimg(canvas,myshare[1][18])).pack(side="bottom",anchor="nw")
	b_20=Button(buttonframe,text=myshare[0][19],command= lambda: imgimg(canvas,myshare[1][19])).pack(side="bottom",anchor="nw")

	root.mainloop()

def get_yourname():
	parser = argparse.ArgumentParser()
	parser.add_argument("name",type=str,help="insert your name.")
	return parser.parse_args().name

if __name__ == '__main__':
	create_canvas(get_yourname())

	#open_window(3,"init")