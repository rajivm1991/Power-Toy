from tkinter.tix import *
from tkinter.ttk import Treeview
from time import sleep
import _thread as thread
def stopclock(w):
	pane = tkinter.tix.PanedWindow(w, orientation='vertical')
	pane.pack(side=tkinter.tix.TOP, expand=1, fill=BOTH)
	f1 = pane.add('stc')
	f2 = pane.add('laplist')
	f3 = pane.add('control')
	#~ stop clock screen
	STC=Label(f1,text="00:00:00.00",font='times 50')
	STC.pack(fill=BOTH)
	#~ Lap list
	L=Label(f2,text="Lapped Time")
	L.pack(fill=X)
	tree_columns = ("No", "Time")
	Entries=Treeview(	f2,
					columns=tree_columns,
					show="headings",
					height=8)
	vsb = Scrollbar(f2,orient="vertical", command=Entries.yview)
	Entries.configure(yscrollcommand=vsb.set)
	for col in tree_columns:
		Entries.heading(col, text=col.title())
	Entries.column(tree_columns[0],width=20)
	Entries.column(tree_columns[1],width=75)
	vsb.pack(side=RIGHT,fill=Y)
	Entries.pack(fill=BOTH)
	#~ action
	global SWITCH,LapCount, st_h, st_m, st_s, st_ms 
	Off	=0
	On	=1
	Pause=2
	SWITCH=Off
	LapCount=0
	def go():
		global SWITCH,st_h,st_m,st_s,st_ms
		print("timer running")
		st_h,st_m,st_s,st_ms=0,0,0,0
		while(SWITCH==On):
			st_ms+=1
			if(st_ms==100):		st_ms=0	; st_s+=1
			if(st_s==60):		st_s=0	; st_m+=1
			if(st_m==60):		st_m=0	; st_h+=1
			if(st_h==99):		st_h=0
			STC.config(text="%0.2d:%0.2d:%0.2d.%0.2d"% ( st_h, st_m, st_s, st_ms ))
			sleep(0.005)
			while(SWITCH==Pause):	None
		print("timer stopped")
	def lap():
		global LapCount,st_h,st_m,st_s,st_ms
		LapCount+=1
		SWITCH==Pause
		Entries.insert('', 'end', values=( LapCount, "%0.2d:%0.2d:%0.2d.%0.2d"%( st_h, st_m, st_s, st_ms ) ) )
		print("lap : %0.2d:%0.2d:%0.2d.%0.2d"%( st_h, st_m, st_s, st_ms ))
		SWITCH==On
	def resume():
		global SWITCH
		print("resumed")
		SWITCH=On
		B1.config(text="Stop",command=stop)
		B2.config(text="Lap",command=lap)
	def reset():
		global SWITCH
		print("sending stop signal")
		SWITCH=Off
		LapCount=0
		STC.config(text="00:00:00.00")
		for each_item in Entries.get_children():
			Entries.delete(each_item)
		B2.forget()
		B1.config(text="Start",command=start)
	def stop():
		global SWITCH
		print("paused")
		SWITCH=Pause
		B1.config(text="Reset",command=reset)
		B2.config(text="Resume",command=resume)
	def start():
		global SWITCH
		print("sending start signal")
		SWITCH=On
		thread.start_new_thread(go,())
		B1.config(text="Stop",command=stop)
		B2.config(text="Lap",command=lap)
		B2.pack(fill=X)
	#~ control
	B1=Button(f3,text="Start",command=start)
	B2=Button(f3)
	B1.pack(fill=X)
if (__name__=='__main__'):
	root=Tk()
	root.title("Stop Clock")
	stopclock(root)
	mainloop()