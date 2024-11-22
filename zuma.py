from os import walk
import os
import string
from pathlib import Path
from natsort import natsorted


import avel


folder = os.getcwd()

filenames = os.listdir()
filenames = natsorted(filenames)
print(filenames)

if "zuma.exe" in filenames:
	filenames.remove("zuma.exe")

if "zuma.py" in filenames:
	filenames.remove("zuma.py")

if "combined.mp4" in filenames:
        filenames.remove("combined.mp4")



index = 0
for filename in filenames:
	os.rename(filename,"vid"+str(index)+".mp4")
	filenames[index] = "vid"+str(index)+".mp4"
	index=index+1





avel.combine_videos(filenames,"combined.mp4")


