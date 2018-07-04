

import subprocess 
import sys
p = subprocess.Popen(["python","sleeper.py"],close_fds = True, stdout=subprocess.PIPE )
import os
fh = open("sleeper.log","a")
#p.communicate( data )
while p.poll() is None:
	fh.flush()
	os.fsync(fh.fileno())
	data = p.stdout.readline()
	fh.write(data)
