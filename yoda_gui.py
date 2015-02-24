#!/usr/bin/python

from Tkinter import *
import ttk

def calculate(*args):
    try:
        value = float(arrive.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


def inches_to_gallons(*args):
	value = float(depart.get())
	v2 = float(arrive.get())
	volume.set( value * v2 )
	print "hello!"
	return gallons


class Collect():
	def __init__(self):
		self.r = 'Smith'
		print "This is the class working"

	def run_pick(self):
		print self.r

def jibs():
	print var.get()


jayne = Collect()

    
root = Tk()
root.title("Collection Details")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# set up the variables, these should match what's in the answers list
arrive = StringVar()
depart =StringVar()
duration = StringVar()
qual = StringVar()
volume = StringVar()

# iniches_entry = ttk.Entry(mainframe, width = 7, textvariable = inches)
# iniches_entry.grid(column = 2, row = 10)

# ttk.Label(mainframe, width = 7, textvariable = gallons).grid(column = 3, row = 10)
# ttk.Button(mainframe, text = "Do Me!", command = inches_to_gallons).grid(column = 3, row = 11)

# prompts = {}
# prompts['Arrivial'] = arrive
# prompts['Departure'] = depart
# prompts['Duration'] = duration
# prompts['Quality'] = qual 

# r = 0 
# for key in prompts:
# 	ttk.Label(mainframe, text = key).grid(column = 1, row = r)
# 	r += 1

questions = [
	'Arrivial (in):' ,
	'Departure (in):' ,
	"Duration (hrs)" , 
	"Quality (0-100)"
]

answers = [ 
	arrive , 
	depart , 
	duration , 
	qual
]

# Make rows

var = StringVar(root)
var.set('Robby')
choices = ['Robby' , 'Jason' , 'Mike' , 'Steph']
option = OptionMenu(mainframe, var, *choices)
option.grid(column = 1,  row = 0)
ttk.Button(mainframe, text = 'Button', command = jibs).grid(column = 3, row = 0)



for i , q in enumerate(questions):
	ttk.Label(mainframe, text = q).grid(column = 1, row = i+1)
	ttk.Entry(mainframe, width = 7, textvariable = answers[i] ).grid(column = 2, row = i+1)


# Put a button to do the calculations
ttk.Button(mainframe, text = 'Collect IT!', command = inches_to_gallons).grid(column = 3, row = len(answers) + 1)
ttk.Label(mainframe, textvariable = arrive).grid(column = 1, row = len(answers) + 1 )
ttk.Label(mainframe, textvariable = volume).grid(column = 2, row = len(answers) + 1 )


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# root.bind('<Return>', inches_to_gallons)
# root.bind('<Return>', calculate)

root.mainloop()




p = inches_to_gallons(inches.get())
print p