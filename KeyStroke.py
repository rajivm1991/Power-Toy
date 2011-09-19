from tkinter.tix import *
def EntryBind(win):
	w=Frame(win)
	LE=list()
	def key(x):
		l=[	x.char,
			x.keycode,
			x.keysym,
			x.keysym_num,
			x.delta,
			x.serial,
			x.state,
			x.time,
			x.type,
			"%d, %d"%(x.x,x.y),
			"%d, %d"%(x.x_root,x.y_root)	]
		LE[0].entry.delete(0,len(LE[0].entry.get()))
		for i in range(len(l)):
			LE[i+1].entry.delete(0,len(LE[i+1].entry.get()))
			LE[i+1].entry.insert(0,l[i])
	options=[	'Enter a key here',
			'Char',
			'Key Code',
			'Key Sym',
			'Key Sym Num',
			'Delta',
			'Serial',
			'State',
			'Time',
			'Type',
			'Window Mouse position',
			'Monitor Mouse Position'		]
	for i in range(len(options)):
		LE.append(LabelEntry(w,label=options[i]))
		LE[i].label.config(width=20,bg='violet',fg='white')
		LE[i].entry.config(width=20)
		LE[i].pack(pady=3)
	LE[0].entry.bind('<KeyPress>',key)
	LE[0].label.config(bg='orange',fg='white')
	w.pack(fill=X)
if (__name__=='__main__'):
	root=Tk()
	root.title("Key Stroke Analyser")
	EntryBind(root)
	mainloop()