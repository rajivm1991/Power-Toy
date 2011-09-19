from tkinter.tix import *
from tkinter.ttk import Treeview
from time import ctime,sleep
import _thread as thread
from CalenderSet import CalLookUp
import sys,winsound
global sound_continueous
def play(snd,repeat=OFF):
	if(repeat):
		global sound_continueous
		sound_continueous=ON
		while(sound_continueous):
			winsound.PlaySound(snd,winsound.SND_ALIAS)
	else:	winsound.PlaySound(snd,winsound.SND_ALIAS)
def digiclock(w):
	pane = tkinter.tix.PanedWindow(w, orientation='vertical')
	pane.pack(side=tkinter.tix.TOP, expand=1, fill=BOTH)
	f1 = pane.add('time',size=190)
	f2 = pane.add('options')
	
	f2pane = tkinter.tix.PanedWindow(f2, orientation='horizontal')
	f2pane.pack(side=tkinter.tix.TOP, expand=1, fill=BOTH)
	f2f1 = f2pane.add('alarm',size=150)
	f2f2 = f2pane.add('event')
	
	global al_status,al_time,m
	m='am'
	ts_status=ON
	al_status=OFF
	al_time=str()
	colour=['orange','red','violet','pink','blue','grey']
	def ConfigEvents():
		now=ctime().split()
		year=int(now[4])
		mon=now[1].lower()
		date=int(now[2])
		notes=CalLookUp( mon )
		for each_item in Entries.get_children():
			Entries.delete(each_item)
		ordered=[]
		for memo in notes: 
			if(int(memo) >= date):
				ordered.append(memo)
		ordered.sort()
		for memo in ordered:
			for note in notes[memo]:
				Entries.insert('', 'end', values=( memo, note[0], note[1]) )
	def displayTime(st,ts):
		global al_time,m
		sleep(3)
		day={'Mon'	:	'Monday'	,
			'Tue'  	:	'Tuesday'	,
			'Wed'	:	'Wednesday',
			'Thu'	:	'Thursday',
			'Fri'	:	'Friday'	,
			'Sat'	:	'Saturday',
			'Sun'	:	'Sunday'	}
		while(st):
			ct=ctime().split(' ')
			m='AM'
			if int(ct[3].split(':')[0])>11 : 
				m='PM'
				if int(ct[3].split(':')[0])>12 :	
					ct[3]=str( int( ct[3][:2] )-12 ) + ct[3][2:]
			if (ct[3].split(':')[0] == '00' ):	
				ct[3]='12' + ct[3][2:]
				ConfigEvents()
			#~ if (not int(ct[3].split(':')[2])%10):	ts.config( bg=colour[ int( int( ct[3].split(':')[2] )/10) ] )
			mhs=ct[3].split(':')
			mode=	{
					'time&date'	:'%s-%s-%s\n%s\n%0.2d:%0.2d:%0.2d %s'%(ct[1],ct[2],ct[4],day[ct[0]],int(mhs[0]),int(mhs[1]),int(mhs[2]),m),
					'time'		:'%0.2d:%0.2d:%0.2d %s'%(int(mhs[0]),int(mhs[1]),int(mhs[2]),m)
					}
			text	=mode['time&date']
			#~ print(ct)
			ts.config(text=text)
			#~ print(al_time,mode['time'],al_time==mode['time'])
			if(al_time==mode['time']):
				set.config( text='Stop' )
				cal.config( text='Expired @ ' + al_time[:-2] )
				thread.start_new_thread(lambda snd='ringout', repeat=ON :play( snd, repeat ) ,() )
			sleep(1)
	def sett():
		global al_status,sound_continueous,al_time
		if(al_status):
			al_status = OFF
			sound_continueous = OFF
			al_time = ''
			cal.config( text='No Alarm' )
			set.config( text='Set' )
		else:
			al_status = ON
			al_time = at.entry.get()+' '+ampm.entry.get()
			cal.config( text='Set @ ' + al_time )
			set.config( text='Remove' )
	bg='orange'
	#~ time frame
	tf=Frame( f1, bg='black' )
	ts=Label(		tf
				,text="rajiv.m1991\n@\ngmail.com"
				,font='times 40'
				,bg='violet'
				,width=11
				,fg='white')
	tf.pack(fill=BOTH)
	ts.pack(fill=X)
	#~ alarm frame
	af=Frame(f2f1,bg=bg)
	al=Label(	af
			,text="$ Alarm $"
			,font='times'
			,fg='white'
			,bg='black')
	at=LabelEntry( af, label='HH:MM:SS', bg=bg )
	at.label.config( fg='white', bg=bg )
	at.entry.config( width=13, borderwidth=0 )
	at.entry.insert( 0, '00:00:00' )
	ampm=LabelEntry( af, label='AM / PM ', bg=bg )
	ampm.entry.config( borderwidth=0 )
	ampm.label.config( fg='white', bg=bg)
	if( int( ctime().split(' ')[3].split(':')[0]) > 11 ):		ampm.entry.insert( 0,'PM' )
	else:	ampm.entry.insert( 0, 'AM' )
	set=Button(af
			,text='Set'
			,command=sett
			,fg='brown')
	ast=Label(	af
			,text='Alarm status:'
			,fg='white'
			,bg=bg
			,anchor='sw')
	cal=Label(	af
			,text='No Alarm'
			,fg='white'
			,bg='black'
			,anchor='sw')
	af.pack(fill=BOTH)
	al.pack(fill=X)
	at.pack(fill=X,padx=5,pady=5)
	ampm.pack(fill=X,padx=5,pady=5)
	set.pack()
	ast.pack(fill=X)
	cal.pack(fill=X)
	#~ options
	L=Label(f2f2,text="Upcoming Events")
	L.pack(fill=X)
	tree_columns = ("Dt", "Note", "Category")
	Entries=Treeview(	f2f2,
					columns=tree_columns,
					show="headings",
					height=5)
	vsb = Scrollbar(f2f2,orient="vertical", command=Entries.yview)
	Entries.configure(yscrollcommand=vsb.set)
	for col in tree_columns:
		Entries.heading(col, text=col.title())
	Entries.column(tree_columns[0],width=20)
	Entries.column(tree_columns[1],width=75)
	Entries.column(tree_columns[2],width=75)
	vsb.pack(side=RIGHT,fill=Y)
	Entries.pack(fill=BOTH)
	#~ start clock
	ConfigEvents()
	thread.start_new_thread(lambda st=ts_status ,ts=ts : displayTime(st,ts),())
	print('Digital Clock Successfully built')
if (__name__=='__main__'):
	root=Tk()
	digiclock(root)
	mainloop()