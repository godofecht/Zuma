from os import walk
import os
import string
from pathlib import Path



import avel


folder = os.getcwd()

filenames = os.listdir(folder)

print(filenames)

if "zuma.exe" in filenames:
    filenames.remove("zuma.exe")


index = 0
for filename in filenames:
    if(os.path.exists(filename)):
    	print(os.path.exists(filename))
    	os.rename(filename,str(index)+".mp4")
    	index=index+1

print(index)



avel.combine_videos(filenames,"combined.mp4")
