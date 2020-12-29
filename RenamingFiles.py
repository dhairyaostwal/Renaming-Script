import os
import sys
import re
import shutil

# Input the destination
destination = '/Users/anchit402/Desktop/Academics/OS'
# In Windows = D:\\aayushi\\Documents\\someFolder
directoryList = os.chdir(destination)
print(os.getcwd())

files = os.listdir()

# pattern = re.compile(r"SEM20\d\d-\d\d_(\w\w\w\d{4}).+\d-[A-Z][a-z][a-z]-20\d\d_(.+)$")
pattern2 = re.compile(r'\B\d\d-[A-Z][a-z][a-z]-20\d\d_(.+)$')

for f in [file for file in files if os.path.isfile(file)]:
	x=pattern2.search(f)
	name=f
    

	if x:
		name=x.group(0)
		name=re.sub(r"_"," ",name)
		name=re.sub(r"  +"," ",name)
		shutil.move(os.path.join(os.getcwd(),f),os.path.join(os.getcwd(),name))
		
