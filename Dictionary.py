from tkinter.tix import *
def Rdict(win):
	w=Frame(win)
	def key(catch):
		WORD = ( word.entry.get()[ 0 : len( word.entry.get() ) - (catch.keycode == 8) ] + (catch.keycode != 8) * catch.char ).lower()
		if(len(WORD) > 2):
			f=open('words.txt')
			text1="Some Entries with '%s' :\n"%(WORD.upper())
			text2="Details About '%s' :\n"%(WORD.upper())
			for l in f:
				if(WORD in l.split(':')[0].lower()):
					text1+='* %s\n'%(l.split(':')[0])
					if(WORD == l.split(':')[0].lower()):
						l=l.split()
						l.reverse()
						text=''
						while(l):
							text+=l.pop()+' '
							if(len(text) >40):
								text2+=text[:-1]+'\n'
								text=''
						if(text):
							text2+=text[:-1]
			f.close()
			suggest.config(text = text1)
			disp.config(text = text2)
		else:
			suggest.config(text = "")
			disp.config(text = "")
	word=LabelEntry(w,label='Word')
	word.entry.bind('<KeyPress>',key)
	word.label.config(width=10,bg='orange',fg='white')
	word.entry.config(width=15)
	word.pack(fill=X,pady=3)
	disp=Label(w,text='Hai welcome to Raj-Dict',bg='orange',fg='white')
	disp.pack(fill=BOTH,pady=3)
	suggest=Label(w,text='Say Hello to Dictionary',bg='violet',fg='white')
	suggest.pack(fill=BOTH,pady=3)
	w.pack(fill=X)
if (__name__=='__main__'):
	root=Tk()
	root.title("Rajiv's Dictionary")
	Rdict(root)
	mainloop()