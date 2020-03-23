import glob
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
from os import listdir
import time

root = tk.Tk()


output_path = ("C:/Users/MYost/Documents/Python Scripts")
path = "C:/Users/MYost/Documents/Python Scripts"

def pick_source_dir():
    global path
    print("Please select the directory with the pdfs you'd like to merge")
    root.withdraw()
    time.sleep(1)
    path = filedialog.askdirectory()


def get_pdf_file():
    input_paths =[]

    print(path)

    files = []
    # r=root, d=directories, f = files
    for file in listdir(path):

         if '.pdf' in file:
             files.append(os.path.join(file))
             input_paths.append(file)
    #input_paths.append(files)

            
        
    return input_paths
 
def merger(output_path, input_paths):

    print (output_path)
    pdf_merger = PdfFileMerger()
    file_handles = []
 
    for i in input_paths:
        pdf_merger.append(path+'/'+i)


    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)
 
if __name__ == '__main__':
    pick_source_dir()
    input_paths = get_pdf_file()
    print ("Name of the files to be combined: ")
    print (input_paths)
    paths = glob.glob('w9_*.pdf')
    paths.sort()
    pdf_file = input("What would you like to name the file?: ")
    merger(path+'/'+pdf_file+'.pdf', input_paths)





