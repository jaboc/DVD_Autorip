#!/usr/bin/python2
"""Automatically rips dvd in drive."""   

__version__ = "1"
__date__ = "Fri Jun 26 23:54:39 EDT 2009"
__license__ = "GPL v2"

import os
import subprocess
import random
import string


# Specify DVD device:
dvdDev = "/dev/sr0"
# Specify the output directory
outdir = "/home/damonj/Videos/DVDRIP/"

# Try to run lsdvd. If it fails, throw an exception. Otherwise, grab all of the metadata from the disk.
dvd = subprocess.Popen(["lsdvd",dvdDev,"-Oy"],stdout=subprocess.PIPE)
dvd.wait()
if dvd.poll() != 0:
  raise IOError("No DVD in drive.") #should use error code & message from lsdvd.
exec(dvd.stdout)


# Create a random string incase the DVD Title isn't unique.
ranstr = (''.join(random.choice(string.ascii_uppercase) for i in range(12)))  


# For each track over 1200 seconds (15 minutes) run it through HandBrake
for x in lsdvd["track"]:
    if x["length"] > 900:
			#print "Track "+ str(x["ix"]) +" is longer than 20 minutes"
			outfile = lsdvd["title"] + "__" + ranstr + "__" + str(x["ix"])
			os.system("/usr/bin/HandBrakeCLI -i " + dvdDev + " -t " + str(x["ix"]) + " -o " + outdir + outfile + ".mkv" + " --preset=\"Jake Default\"" )


# Now we're finsihed eject the DVD so we can stick in a new one.
os.system("/usr/bin/eject " + dvdDev)
