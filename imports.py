#!/usr/bin/python

# This py script should look if all the necessary libraries are installed
# If they are not installed, install them


# scriptname = '/Users/AsianCheddar/CRES/gui_class.py'
# import inspect, importlib as implib


# mod = implib.import_module( 'gui_class' )
# for i in inspect.getmembers(mod, inspect.ismodule ):
#     print i[0]


from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('/Users/AsianCheddar/CRES/gui_class.py')
for key in finder.modules:
	print key 

names = list(finder.modules.keys())
print 'Loaded modules:'
for name in names:
    print  name
    # print ','.join(mod.globalnames.keys()[:3])

print '-'*50
# print 'Modules not imported:'
# print '\n'.join(finder.badmodules.iterkeys())
basemods = sorted(set([name.split('.')[0] for name in names]))
# Print it nicely
print "\n".join(basemods)