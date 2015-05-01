#!/usr/bin/env python
#Simple app to interact with user
#Calculates area of a rectangle
import Tkinter

class AreaApp(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

	def initialize(self):
		"""
		initialize the app
		"""
		self.grid()		#layout manager
		
		label1=Tkinter.Label(anchor="w", text="Enter length(m):")
		label1.grid(column=0,row=0)
		self.lengthVar= Tkinter.StringVar()
		self.entry1=Tkinter.Entry(self, textvariable=self.lengthVar)				#Add a text field by using Entry
		self.entry1.grid(column=1,row=0,sticky="EW")
		label2=Tkinter.Label(anchor="w", text="Enter breadth(m):")
		label2.grid(column=0,row=1)
		self.breadthVar=Tkinter.StringVar()
		self.entry2=Tkinter.Entry(self, textvariable=self.breadthVar)
		self.entry2.grid(column=1,row=1,sticky="EW")
		
		button=Tkinter.Button(self,text=u"Compute", command=self.OnClick)	#Add a button
		button.grid(column=0,row=2,sticky="EW")

		self.result=Tkinter.StringVar()
		label3=Tkinter.Label(anchor="w", textvariable=self.result)						#Add a label (text display), anchor is for allignment 
		label3.grid(column=0,row=3,columnspan=1,sticky="EW")	#columnspan specifies how many columns it spans
		self.grid_columnconfigure(0,weight=1)				#column 0 resizes automatically on maximizing. 
		self.resizable(False,False)							#disable resizing

	def OnClick(self):
		"""
		action to be taken on on Click
		"""
		try:
			length=float(self.lengthVar.get())
			breadth=float(self.breadthVar.get())
			if length<0 or breadth<0:
				raise ValueError
			area=self.area(length,breadth)
			self.result.set("Area: "+area)
		except ValueError:
			self.result.set("Invalid Input")

	def area(self,length,breadth):
		return str(length*breadth)

if __name__=="__main__":
	app = AreaApp(None)
	app.title("Area of Rectangle")
	app.mainloop()
