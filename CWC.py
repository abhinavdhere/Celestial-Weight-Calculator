#!/usr/bin/env Python
#------------------------------------------------------------------------------------------------------
#Implementation of Celestial Weight Calculator in GUI
#Date: 5 May 2015
#
#This source code has been provided solely for reference purposes.
#(c) Abhinav Dhere. All rights reserved.
#
#------------------------------------------------------------------------------------------------------

import Tkinter

class CWC_app(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

	def initialize(self):
		'''
		initialize the CWC_app
		'''
		welcome=Tkinter.Label(anchor="center", text="\t\tWelcome to Celestial Weight Calculator!\t\t\t\t")
		welcome.pack()
		nameLabel=Tkinter.Label(anchor="w",text="Your name:  ")
		nameLabel.pack(anchor="w",side="top",pady=10)
		self.name=Tkinter.StringVar()	
		nameEntry=Tkinter.Entry(textvariable=self.name,width=30)
		nameEntry.pack(anchor="w")
		self.weight=Tkinter.StringVar()
		weightLabel=Tkinter.Label(text="Your weight on Earth:  ")
		weightLabel.pack(anchor="w",side="top",pady=10)
		weightEntry=Tkinter.Entry(textvariable=self.weight,width=30)
		weightEntry.pack(anchor="w")
		planetLabel=Tkinter.Label(text="Select Celestial body:  ")
		planetLabel.pack(anchor="w",side="top",pady=10)

		self.planets=self.getPlanetData()
		planetList=self.planets.keys()
		self.selection=Tkinter.StringVar()
		self.selection.set(planetList[0])
		options=apply(Tkinter.OptionMenu, (self,self.selection) + tuple(planetList))
		options.pack(anchor="w")

		button=Tkinter.Button(self,text=u"Compute Weight",command=self.OnClick)
		button.pack(side="top",pady=10)
		self.result=Tkinter.StringVar() 
		result=Tkinter.Label(textvariable=self.result)
		result.pack()
		blank=Tkinter.Label(text="")
		blank.pack()

		menuBar= Tkinter.Menu(self, relief="flat")
		FileMenu=Tkinter.Menu(menuBar, tearoff=0)
		FileMenu.add_command(label="Save Data",command=self.save)
		FileMenu.add_separator()
		FileMenu.add_command(label="Exit",command=self.quit)
		HelpMenu=Tkinter.Menu(menuBar,tearoff=0)
		HelpMenu.add_command(label="About",command=self.about)
		menuBar.add_cascade(label="File", menu=FileMenu)
		menuBar.add_cascade(label="Help", menu=HelpMenu)
		self.config(menu=menuBar)
		self.resizable(False,False)

	def save(self):
		try:
			records=open("record.txt",'a')
			records.write("\n"+self.name.get()+"'s weight on "+self.selection.get()+" is "+str(self.NW))
			records.close()
			popUp=Tkinter.Toplevel()
			popUp.geometry("500x25+0+0")
			popUp.title("Save Successful")
			saveNotif=Tkinter.Label(popUp,text="Results saved to record.txt")
			saveNotif.pack(fill="x")
			popUp.resizable(False,False)
		except AttributeError:
			popUp=Tkinter.Toplevel()
			popUp.title("Error")
			popUp.geometry("500x25+0+0")
			saveNotif=Tkinter.Label(popUp,text="Invalid or no input given")
			saveNotif.pack(fill="x")
			popUp.resizable(False,False)

	def about(self):
		AboutText="""
About

Celestial Weight Calculator v2.0
Written by Abhinav Dhere.
(c)Abhinav Dhere. All rights reserved.
		
Disclaimer

This software is provided "as is" and without any warranty whatsoever.
All computations are based on data available in public domain.
The developer does not take any guarantee for accuracy of results.
"""
		
		newWin=Tkinter.Toplevel()
		newWin.title("About")
		newWin.geometry("480x240",)
		aboutlab=Tkinter.Label(newWin,text=AboutText)
		aboutlab.pack()

	def getPlanetData(self):
		'''
		holds data for planets 
		'''
		dataFile=open("Planet Data.txt",'r')
		planets={}
		for line in dataFile:
			if line[0]=="#":
				pass
			else:
				line.strip("\n")
				data=line.split()
				planets[data[0]]=(float(data[1]),float(data[2]))
		return planets

	def OnClick(self):
		try:
			planetName=self.selection.get()
			weight=float(self.weight.get())
			user=User(self.name.get(),weight)
			planet=Planet(planetName,self.planets[planetName][1],self.planets[planetName][0])
			self.NW=user.getNewWeight(planet)
			self.result.set(user.getName()+", your weight on "+planet.getName()+" is "+str(self.NW))
		except ValueError:
			self.result.set("Invalid Input")

class User(object):
	'''
	class for user details
	'''
	def __init__(self,name,weight):
		self.name=name
		self.weight=weight

	def getName(self):
		return self.name

	def getMass(self):
		return (self.weight/9.8)

	def getNewWeight(self, planet):
		'''
		planet is an instance of planet class
		'''
		g=planet.getG()
		NewWeight=self.getMass()*g
		return NewWeight

class Planet(User):
	'''
	each instance is a planet
	'''
	def __init__(self,name,mass,radius):
		User.__init__(self,name,mass)
		self.radius=radius

	def getMass(self):
		return self.weight

	def getG(self):
		'''
		calculates acceleration due to gravity
		'''
		G=6.67259*(10**(-11))
		g=(G*self.getMass())/self.radius**2
		return g


if __name__=="__main__":
	app=CWC_app(None)
	app.title("Celestial Weight Calculator v2.0")
	app.mainloop()

