This is the NEW and IMPROVED version of the CRES Python program. 

As of today 12/1/15, there are two versions of the main program. 
	-CRES.py which rins on a computer that has a monitor and
	-headless.py that does not require a monitor to function, though a keyboard is recommended. 

There ARE requirements that you'll need to meet that are NOT listed in this repo. 
	-google_creds dir needs to be located in your HOME directory and has to contain the proper .json file(s) to use the associated API's 
		
I have provided an updated requirements.txt file for pip install. If you're using Linux, some of the packages are not available via PIP so you're going to have to apt-get them yourself. The most recent version should work in every case. 
	I used to have the program do the installation itself, but I ran into loop problems. 
	If you get an error saying "you don't have <some module name>" you can install ALL the modules at once by running from the CRES directory.  
		sudo pip install requirements.txt   
