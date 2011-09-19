from tkinter.tix import *
from time import sleep,ctime
import _thread as thread
def countdown(w):
	pane = tkinter.tix.PanedWindow(w, orientation='vertical')
	pane.pack(side=tkinter.tix.TOP, expand=1, fill=BOTH)
	f1 = pane.add('cdt',size=250)
	f2 = pane.add('control')
	#~ countdown timer
	Head=Label(f1,text="CountDown")
	Head.pack(fill=X)
	CD_STATUS=dict()
	global c_id
	c_id=0
	def Go():
		#~ id for countdown
		global c_id
		if(len(CD_STATUS)>9):
			return
		c_id+=1 
		id=int(c_id)
		CD_STATUS[id]=True
		#~ build timer frame
		CD_Entry=Frame(f1)
		#~ method for close timer
		def close():
			CD_STATUS[id]='x'
			sleep(0.5)
			del(CD_STATUS[id])
			DEL.destroy()
			NOTE.destroy()
			TIMER.destroy()
			CD_Entry.destroy()
		notes=note.entry.get()
		NOTE		= Label(CD_Entry,text=notes)
		st_h, st_m, st_s, st_ms = int(h.entry.get()), int(m.entry.get()), int(s.entry.get()), 0
		TIMER	= Label(CD_Entry,text="%0.2d:%0.2d:%0.2d.%0.2d"%( st_h, st_m, st_s, st_ms ) )
		DEL		= Button(CD_Entry,text="X  ",borderwidth=0,command=close)
		NOTE.pack(side=LEFT,fill=BOTH,anchor='ne')
		TIMER.pack(side=LEFT,fill=BOTH,anchor='ne')
		DEL.pack(anchor='ne')
		CD_Entry.pack(fill=X)
		#~ action
		while(CD_STATUS[id]==True):
			if(st_ms==-1):		st_ms=99	; st_s-=1
			if(st_s==-1):		st_s=59	; st_m-=1
			if(st_m==-1):		st_m=59	; st_h-=1
			if(st_h==0 and st_m==0 and st_s==0 and st_ms==0):
				CD_STATUS[id]=False
			TIMER.config(text="%0.2d:%0.2d:%0.2d.%0.2d"% ( st_h, st_m, st_s, st_ms ))
			sleep(0.005)
			st_ms-=1
		if(not CD_STATUS[id]):
			x,CD_STATUS[id],exp=1,True,ctime().split()[3]
			while(CD_STATUS[id]==True):
				if(x):	TIMER.config(text="");x=0
				else:	TIMER.config(text="Expired @ %s"%(exp));x=1
				sleep(0.2)
	#~ controls
	entries=Frame(f2)
	h=ComboBox(entries,label='hour :',editable=1)
	h.entry.config(width=5)
	h.entry.insert(0,"00")
	m=ComboBox(entries,label='min :',editable=1)
	m.entry.config(width=5)
	m.entry.insert(0,"00")
	s=ComboBox(entries,label='sec :',editable=1)
	s.entry.config(width=5)
	s.entry.insert(0,"00")
	note=LabelEntry(f2,label='Note :')
	go=Button(f2,text="Add Countdown",command=lambda :thread.start_new_thread(Go,()) )
	for i in range(100):
		if(i<60):
			m.insert(END,'%0.2d'%(i))
			s.insert(END,'%0.2d'%(i))
		h.insert(END,'%0.2d'%(i))
	anc='ne'
	h.pack(side=LEFT,anchor=anc)
	m.pack(side=LEFT,anchor=anc)
	s.pack(side=LEFT,anchor=anc)
	entries.pack(fill=X)
	note.pack(fill=X,anchor=anc)
	go.pack(fill=X,anchor=anc)
if (__name__=='__main__'):
	root=Tk()
	countdown(root)
	mainloop()