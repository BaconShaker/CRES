#!/usr/bin/python

from Tkinter import *
import ttk

# The Plan:
	# 	For BOTH display details as well as for input collection
	# 	__init__ all the dicts vars and such
	# 	write a def that displays them all 



class Display_Array(object):

	def __init__(self, restaurants, *args):
		# restaurants needs to be a list of restarant names, to be used to get 
		# information later and to display. ORDER is important!!!
		self.restaurants = restaurants
		self.root = Tk()
		self.root.title("Collection Details")
		self.main = ttk.Frame(self.root, padding="3 3 12 12")
		self.main.grid(column=0, row=0, sticky=(N, W, E, S))
		self.main.columnconfigure(0, weight=1)
		self.main.rowconfigure(0, weight=1)
	


	def collect_inputs(self):
		print "Start: collect_inputs()"
		# Add a button to quit the GUI loop
		ttk.Button(text="Quit!" , command = self.root.destroy).grid(column = 0, row = 1)
		

		scol = 2
		srow = 2
		
		robby = []
		harr = [31 for r in self.restaurants]
		IntVar(value = harr)
		# harr = IntVar()
		hdep = [3 for r in self.restaurants]
		IntVar(value = hdep)
		qual = [50 for r in self.restaurants]
		IntVar(value = qual)
		dura = [1 for r in self.restaurants]
		IntVar(value = dura)
		note = [31 for r in self.restaurants]
		StringVar(value = note)

		prompt = {
					"Height (ARRIVAL)" : harr,
					"Height (DEPARTURE)" : hdep,
					"Quality (0 - 100)": qual,
					"Duration" : dura,
					"Notes" :  note  ,
				}

		
		for stop , name in enumerate(self.restaurants):
			# ttk.Label(dframe, text = "Some text").grid(column = start_col, row = start_row + stop)
			# Could probably add a radio button above this and make the inputs or info propmt appear based on checked or not... 
			ttk.Label(self.main, text =  "Inputs for " + name).grid( column = scol + 1  - stop + stop * 3 , row = srow )
		
			ttk.Label(self.main, text = "Height (ARRIVAL): ").grid(column = scol + stop* 2, row = srow  +1 , sticky = 'e' )
			ttk.Entry(self.main, textvariable = harr[stop]).grid(column = scol + 1 + stop * 2, row = srow + 1 )

			ttk.Label(self.main, text = "Height (DEPART): ").grid(column = scol + stop* 2, row = srow  + 2 , sticky = 'e' )
			ttk.Entry(self.main, textvariable = hdep[stop]).grid(column = scol + 1 + stop * 2, row = srow + 2 )

			ttk.Label(self.main, text = "Quality (0 - 100): ").grid(column = scol + stop* 2, row = srow  + 3 , sticky = 'e' )
			ttk.Entry(self.main, textvariable = qual[stop]).grid(column = scol + 1 + stop * 2, row = srow + 3 )

			ttk.Label(self.main, text = "Duration: ").grid(column = scol + stop* 2, row = srow  +4 , sticky = 'e' )
			ttk.Entry(self.main, textvariable = dura[stop]).grid(column = scol + 1 + stop * 2, row = srow + 4 )

			ttk.Label(self.main, text = "Notes: ").grid(column = scol + stop* 2, row = srow  + 5 , sticky = 'e' )
			ttk.Entry(self.main, textvariable = harr[stop]).grid(column = scol + 1 + stop * 2, row = srow + 5 )







		self.root.mainloop()


		print prompt.get()
		print "End: collect_inputs()"
		# print "Fuck yeah!" , self.restaurants
		return "Fuck yeah!" , self.restaurants



robby = Display_Array(["1","2","3"])
robby.collect_inputs()
