import tkinter, PIL, os, glob, argparse, math
import numpy as np
from PIL import ImageTk, Image
from tkinter import ttk

Dataset_root="./Image Data Set"

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

def create_canvas(name):
	share = 120

	dataset=explore_dir(Dataset_root,0)
	myshare=[["" for cols in range(share)]for rows in range(2)]
	max_size=np.array([0,0])

	if name=="jsw": count = 1
	elif name=="ksy": count = 2
	elif name=="jwj": count = 3
	elif name=="pjy": count = 4
	elif name=="yyg": count = 5
	elif name=="pbr": count = 6
	elif name=="cej": count = 7
	elif name=="cyj": count = 8
	elif name=="hjh": count = 9

	start = (count * share) - share
	end = (count * share) - 1

	print(start,end)

	for i in range(2):
		for j in range(share):
			myshare[i][j]=dataset[i][j+start]
	for i in range(share):
		img = Image.open(myshare[1][i])
		[WIDTH, HEIGHT] = img.size
		if img is None: continue
		if img.size[0]>max_size[0]: max_size[0]=img.size[0]
		if img.size[1]>max_size[1]: max_size[1]=img.size[1]



	root = tkinter.Tk()

	buttonframe=tkinter.Frame(root)
	canvasframe=tkinter.Frame(root)
	clearbuttonframe=tkinter.Frame(root)

	buttonframe.pack(ipadx=0, ipady=0, side="top")

	coor=tkinter.StringVar(root,value='')
	coor_entry=ttk.Entry(root,textvariable=coor,width=100)
	coor_entry.pack(side="top")

	full_path=tkinter.StringVar(root,value='')
	filefullpath=ttk.Entry(root,textvariable=full_path,width=80)
	filefullpath.pack(side="top")

	canvasframe.pack(ipadx=0,ipady=0,side="top")
	canvas = tkinter.Canvas(canvasframe,width=max_size[1],heigh=max_size[0])
	canvas.pack()

	def imgimg(canvas,imgimg_name):
		canvas.delete("all")
		resized=False

		img = Image.open(imgimg_name)
		OLD_W, OLD_H = img.size
		NEW_W, NEW_H = 800, 750
		print(img.size , OLD_W/NEW_W, OLD_H/OLD_H)

		if OLD_W>NEW_W or OLD_H>NEW_H: 
			img = img.resize((NEW_W, NEW_H), Image.ANTIALIAS)
			resized=True

		canvas = tkinter.Canvas(canvas, width=NEW_W, heigh=NEW_H)
		canvas.place(x=0,y=0)

		img = ImageTk.PhotoImage(img)
		canvas.create_image(0,0,image=img,anchor="nw")
		filefullpath.delete(0,"end")
		filefullpath.insert("end",imgimg_name)

		def down(event):
			global x0,y0;
			x0, y0 = event.x, event.y	  

			if(x0,y0) == (event.x,event.y):
				canvas.create_oval(x0-2,y0-2,event.x+2,event.y+2,outline="red",fill="red",width=2)
		def up(event):
			global x0, y0
			if(x0,y0) == (event.x,event.y):
				canvas.create_oval(x0-2,y0-2,event.x+2,event.y+2,outline="red",fill="red",width=2)

			if resized : 
				x0*=OLD_W/NEW_W
				y0*=OLD_H/NEW_H
			#coor_entry.delete(0,"end")
			coor_entry.insert("end",str(int(x0))+","+str(int(y0))+",")
			print ("("+str(int(x0))+","+str(int(y0))+")")

		canvas.bind("<Button-1>",down) 
		canvas.bind("<ButtonRelease>",up) 
		root.mainloop()
	buttonlist=list()
	for i in range(share):
		buttonlist.append(tkinter.Button(buttonframe, text=myshare[0][i],command=lambda i=i: imgimg(canvas,myshare[1][i])))

	count_num=0
	for row in range(int(math.ceil(share/20))):
		for col in range(20):
			buttonlist[count_num].grid(column=col, row=row)
			count_num+=1

	root.mainloop()

def get_yourname():
	parser = argparse.ArgumentParser()
	parser.add_argument("name",type=str,help="insert your name.")
	return parser.parse_args().name

if __name__ == '__main__':
	create_canvas(get_yourname())

	#open_window(3,"init")