from tkinter.tix import *
class PythonRajiv:
	def __init__(self,w):
		self.root=w
	def MainBook(self):
		top = self.root
		book = NoteBook(top, ipadx=5, ipady=5, options="""
		tagPadX 6
		tagPadY 4
		borderWidth 2
		""")
		book.add('rcm', label="Clock Module",
			createcmd=lambda book=book, name='rcm': ClockModule(book, name))
		book.add('ka', label="Key Analyzer",
			createcmd=lambda book=book, name='ka': KeyAnalyzer(book, name))
		book.add('rdict', label="Raj-Dictionary",
			createcmd=lambda book=book, name='rdict': RajDict(book, name))
		return book
	def build(self):
		w = self.root.winfo_toplevel()
		w.wm_title("Rajiv's Power Toy")
		w.wm_protocol("WM_DELETE_WINDOW", lambda self=self: self.quitcmd())
		book=self.MainBook()
		book.pack(side=TOP,fill=BOTH,expand=1)
		print('>>> Main Project Window builded')
	def quitcmd(self):
		print('>>> Thank you ...')
		print('>>> M.Rajiv Subramanian')
		sys.exit()
	def run(self):
		mainloop()

def ClockModule(book, name):
	w=book.page(name)
	import ClockCalenderSet
	ClockCalenderSet.RajivClock(w)

def KeyAnalyzer(book, name):
	w=book.page(name)
	from KeyStroke import EntryBind
	EntryBind(w)

def RajDict(book, name):
	w=book.page(name)
	from Dictionary import Rdict
	Rdict(w)

def main(window):
	obj=PythonRajiv(window)
	obj.build()
	obj.run()
if __name__ == '__main__':
	w=Tk()
	main(w)