from tkinter.tix import *
from tkinter.ttk import Treeview
from time import ctime
import _thread as thread
def CalLookUp(m):
	ret={}
	months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
	CalNotes=open("vCalendar.vcs")
	def makedict(st):
		return{	"year"	: st[0:4],
				"month"	: months[int(st[4:6])-1],
				"date"	: st[6:8],
				"hour"	: st[9:11],
				"minute"	: st[11:13],
				"second"	: st[13:]}
	for l in CalNotes:
		data={}
		entry=CalNotes.readline()
		while(entry[:-1]!=''):
			if('DTSTART:' in entry)	:	data['start']	= makedict( entry[8:-1] )
			elif('DTEND:' in entry)	:	data['end']	= makedict( entry[6:-1] )
			elif('AALARM:' in entry)	:	data['alarm']	= makedict( entry[7:-1] )
			elif('CHARSET' in entry)	:	data['note']	= entry[entry.index('UTF-8')+6:-1]
			elif('CATEGORIES:' in entry):	data['category']=entry[11:-1]
			entry=CalNotes.readline()
		if(data['start']['month']==m):
			if(data['start']['date'] not in ret):
				ret[data['start']['date']]=list()
			ret[data['start']['date']].append([ data['note'], data['category']  ])
	CalNotes.close()
	return ret	
def calender(w):
	global year,mon
	date_bg	= 'white'
	date_fg	= 'black'
	date_fgb	= 'blue'
	date_bgt	= 'white'
	date_fgt	= 'red'
	day_bg	= 'orange'
	day_fg	= 'white'
	mon_bg	= 'violet'
	mon_fg	= 'white'
	Magic_Sequence="2345012356013456123460124560"
	month={	'jan' : 0	,
			'feb' : 8	,
			'mar' : 25	,
			'apr' : 5	,
			'may' : 1	,
			'jun' : 9	,
			'jul' : 5	,
			'aug' : 13	,
			'sep' : 21	,
			'oct' : 17	,
			'nov' : 25	,
			'dec' : 21	}
	months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
	day=['sun','mon','tue','wed','thu','fri','sat']
	#~ current year and month
	now=ctime().split()
	year=int(now[4])
	mon=now[1].lower()
	date=int(now[2])
	def Cal_config(modify=False):
		global year,mon
		mon_limit=[31,28,31,30,31,30,31,31,30,31,30,31]
		now=ctime().split()
		cyear=int(now[4])
		cmon=now[1].lower()
		cdate=int(now[2])
		if(modify=='go'):
			year,mon	= int(y.entry.get()), m.entry.get()
		elif(modify):
			if	(months.index(mon)+modify>11)	:	year,mon	=	year+1,	'jan'
			elif	(months.index(mon)+modify<0)	:	year,mon	=	year-1 ,	'dec'
			else:	mon = months[ months.index( mon )+modify ]
		monl.config( text = "%s - %d"%(mon.title(),year) )
		if(not year%4):	mon_limit[1]=29	# Leap year Check
		year_id			=	(year+3)%28
		Required_Sequence	=	Magic_Sequence[ month[mon]: ]+Magic_Sequence[ :month[mon] ]
		addition_factor		=	int(Required_Sequence[year_id])
		notes=CalLookUp( mon )
		d=1
		for i in range(37):
			if(i<addition_factor or d > mon_limit[ months.index( mon ) ] ):	# blank positions
				datebuttons[i].config(	text='',
								bg=date_bg,
								activebackground=date_bg)
			else:		# positions with date
				bc,fc=date_bg,date_fg
				bracket=0
				if(year==cyear and mon==cmon and d==cdate):	bc,fc,bracket=date_bgt,date_fgt,1
				if ( "%0.2d"%(d) in notes ): fc=date_fgb
				datebuttons[i].config(	text="%s%0.2d%s"%('('*bracket,d,')'*bracket),
								bg=bc,	fg=fc,
								activebackground='yellow',
								activeforeground='black')
				d+=1
		for each_item in Entries.get_children():
			Entries.delete(each_item)
		ordered=[]
		for memo in notes: ordered.append(memo)
		ordered.sort()
		for memo in ordered:
			for note in notes[memo]:
				Entries.insert('', 'end', values=( memo, note[0], note[1] ) )
		print("Cal configured to", mon, year)
	#~ main calender frame
	pane = tkinter.tix.PanedWindow(w, orientation='vertical')
	pane.pack(side=tkinter.tix.TOP, fill=BOTH)
	f1 = pane.add('top',size=190, expand='0',allowresize=0)
	f2 = pane.add('info', expand='0',allowresize=0)
	
	f1pane= tkinter.tix.PanedWindow(f1, orientation='horizontal')
	f1pane.pack(side=tkinter.tix.TOP, fill=BOTH)
	f1f1 = f1pane.add('calender',size=200,allowresize=0)
	f1f2 = f1pane.add('options',allowresize=0)
	
	#~ month heading
	calhead=Frame(f1f1,bg=date_bg)
	back=Button(calhead	,
			text='<<<'	,
			width=5	,
			bg=date_bg,
			activebackground='red',
			activeforeground='white',
			borderwidth=0,
			command=lambda modify=-1 :	Cal_config( modify ) )
	monl=Label(calhead	,
			width=15	,
			bg=mon_bg,
			fg=mon_fg)
	next=Button(calhead	,
			text='>>>'	,
			width=5	,
			bg=date_bg,
			activebackground='red',
			activeforeground='white',
			borderwidth=0,
			command=lambda modify=1 :	Cal_config( modify ) )
	back.pack(side=LEFT)
	monl.pack(side=LEFT	, padx=10)
	next.pack(side=LEFT)
	calhead.pack(fill=X)
	#~ day lables
	DayFrame=Frame(f1f1,bg=day_bg)
	daylabels=[]
	for i in range(7):
		daylabels.append( Label(DayFrame	,
						text=day[i]	,
						width=3	,
						bg=day_bg,
						fg=day_fg) )
		daylabels[i].pack( side=LEFT , padx=2 )
	DayFrame.pack(fill=X)
	#~ date buttons
	datebuttons=[]
	dfl=[]
	for i in range(6):	
		dfl.append( Frame(f1f1, bg=date_bg) )
		dfl[i].pack(fill=X)
	j=0
	for i in range(37):	
		datebuttons.append( Button( dfl[j], width=3, borderwidth=0 ) )
		datebuttons[i].pack( side=LEFT, padx=2 )
		if(not (i+1)%7 ): j+=1
	#~ information frame
	mem=Label(f2,text="Memos :")
	disp_frame=tkinter.Frame(f2)
	tree_columns = ("Date", "Note","Category")
	Entries=Treeview(	disp_frame,
					columns=tree_columns,
					show="headings",
					height=5)
	vsb = Scrollbar(disp_frame,orient="vertical", command=Entries.yview)
	Entries.configure(yscrollcommand=vsb.set)
	for col in tree_columns:
		Entries.heading(col, text=col.title())
	Entries.column("Date",width=50)
	Entries.column("Note",width=150)
	Entries.column("Category",width=100)
	vsb.pack(side=RIGHT,fill=Y)
	Entries.pack(fill=BOTH)
	mem.pack(fill=X)
	disp_frame.pack(fill=BOTH)
	#~ option frame
	L=Label(f1f2,text="More Options:")
	view=Frame(f1f2)
	y=ComboBox(view,editable=1)
	y.entry.config(width=5)
	y.entry.insert(0,year)
	m=ComboBox(view,editable=1)
	m.entry.config(width=4)
	m.entry.insert(0,mon)
	go=Button(f1f2,text="<<< Go",command=lambda  modify='go' : Cal_config(modify))
	for i in range(200):
		y.insert(END,'%d'%(i+1901))
	for i in months:
		m.insert(END,i)
	y.pack(side=LEFT)
	m.pack()
	L.pack(fill=X)
	view.pack(fill=X)
	go.pack(fill=X)
	#~ first config
	Cal_config()
if (__name__=='__main__'):
	root=Tk()
	calender(root)
	mainloop()