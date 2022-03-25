# ---------- Packages -----------

from docx2pdf import convert
import os
from os.path import isfile, join

# ------------ Start Execution -------------

# Folder path
path = os.getcwd() + r"\docx2pdf-files"


# Adding all available files in a list
all_files = [ f for f in os.listdir(path) if isfile(join(path, f))]

# Converting
for i in all_files:
    if i[-5:]=='.docx':
        convert(path+"\\"+i)
print("All files have been converted")
