from time import sleep,ctime
from tkinter.ttk import Treeview
from tkinter.tix import *
from time import sleep
import _thread as thread
global sound_continueous
sound_continueous=OFF
class RajivClock:
	def __init__(self,top):
		self.root=top
		self.build()
	def MainBook(self):
		top = self.root
		book = NoteBook(top, ipadx=5, ipady=5, options="""
		tagPadX 6
		tagPadY 4
		borderWidth 2
		""")
		book.add('clk', label='Digital Clock',
			createcmd=lambda book=book, name='clk': Digital(book, name))
		book.add('cal', label='Calender',
			createcmd=lambda book=book, name='cal': Calender(book, name))
		book.add('stc', label='Stop Watch',
			createcmd=lambda book=book, name='stc': StopWatch(book, name))
		book.add('cdn', label='Count Down',
			createcmd=lambda book=book, name='cdn': CountDown(book, name))
		return book
	def winbuild(self):
		root=self.root
		win=root.winfo_toplevel()
		win.wm_title("Rajiv's Clock module set")
		win.wm_protocol("WM_DELETE_WINDOW",self.quit)
		win.iconbitmap(default='r.ico')
		win.iconposition(x=50,y=10)
		win.iconmask()
		#~ win.maxsize(570,250)
		#~ win.minsize(570,250)
	def build(self):
		book=self.MainBook()
		book.pack(side=TOP,fill=BOTH,expand=1)
	def begin(self):
		print('Project Started')
		mainloop()
	def quit(self):
		sys.exit('Project Terminated')

#~ - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) 

def Digital(book, name):
	w=book.page(name)
	from DigiClock import digiclock
	digiclock(w)

#~ - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) 

def Calender(book, name):
	w=book.page(name)
	from CalenderSet import calender
	calender(w)
	print('Calender Successfully built')

#~ - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) 
	
def StopWatch(book, name):
	w=book.page(name)
	from StopClock import stopclock
	stopclock(w)
	print('Stop Watch Successfully built')
	
#~ - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) 

def CountDown(book, name):
	w=book.page(name)
	w.config(bg='violet')
	from CountDown import countdown
	countdown(w)
	print('Count Down Timer Successfully built')
	
#~ - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) - :D - :) 

def main(root):
	Pearl=RajivClock(root)
	Pearl.winbuild()
	Pearl.begin()
if (__name__=='__main__'):
	root=Tk()
	main(root)