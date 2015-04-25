#Learning GUI.
#Source: http://sebsauvage.net/python/gui/

import Tkinter										#Step 1: Import

class HelloApp(Tkinter.Tk): 						#Step 2: Make an app class inheriting from Tkinter
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)			#Step 3: Init from parent class
		self.initialize()

	def initialize(self):							#Step 4: Intialize the app
		'''
		initialize the app
		'''
		#self.grid()									#Step 8: Makes a grid as layout manager
		self.label=Tkinter.Label(self,text="Hello World!",justify="center")
		#self.label.grid(column=0,row=0)
		self.label.pack()

if __name__=="__main__":							#Step 5: Check if run as main file and not imported
	app=HelloApp(None)								#Step 6: Make an app object
	app.title("Hello World")						#Adding title
	app.mainloop()									#Step 7: Starting main loop	