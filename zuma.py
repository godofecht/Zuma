from os import walk
import os
import string
from pathlib import Path



import avel


folder = os.getcwd()

filenames = os.listdir()

print(filenames)

if "zuma.exe" in filenames:
	filenames.remove("zuma.exe")

if "zuma.py" in filenames:
	filenames.remove("zuma.py")


index = 0
for filename in filenames:
	if(not os.path.exists(filename)):
		print(os.path.exists(filename))
		os.rename(filename,str(index)+".mp4")
		filenames[index] = str(index)+".mp4"
		index=index+1

print(filenames)



avel.combine_videos(filenames,"combined.mp4")
