from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

#create the about window
def aboutwindow(root):
    aboutwindowobject = Toplevel(root)
    aboutwindowobject.title("About BluePenguin")
    aboutwindowobject.iconbitmap('icon/BluePenguin.ico')
    aboutwindowobject.geometry("300x100")
    aboutwindowobject.minsize(300, 100)
    aboutwindowobject.maxsize(300, 100)

    aboutwindow_label1 = Label(aboutwindowobject, text="Blue Penguin")
    aboutwindow_label1.grid(row=0, column=0)
    aboutwindow_label2 = Label(aboutwindowobject, text="An A6 and A7-sized booklet creator by LStefanCoder")
    aboutwindow_label2.grid(row=1, column=0)
    aboutwindow_label3 = Label(aboutwindowobject, text="https://github.com/LStefanCoder/bluepenguin")
    aboutwindow_label3.grid(row=2, column=0)
    aboutwindow_label4 = Label(aboutwindowobject, text="Program licensed under GPL v3.0")
    aboutwindow_label4.grid(row=4, column=0)


#this function fills up the pagenumbers in the correct order
def pagenumberarray_filler(numberofpages, eightorsixteen):

    startarray = []
    finalarray = []

    for i in range(1, numberofpages + 1):
        startarray.append(i)

    if eightorsixteen == 16:

        #the del is needed to delete the number sliced from the original list
        #https://www.programiz.com/python-programming/del
        while(len(startarray) > 15):
            #front page
            finalarray.append(startarray[0])
            del startarray[0]
            finalarray.append(startarray[1])
            del startarray[1]
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]
            finalarray.append(startarray[len(startarray) - 2])
            del startarray[len(startarray) - 2]
            finalarray.append(startarray[2])
            del startarray[2]
            finalarray.append(startarray[3])
            del startarray[3]
            finalarray.append(startarray[len(startarray) - 3])
            del startarray[len(startarray) - 3]
            finalarray.append(startarray[len(startarray) - 4])
            del startarray[len(startarray) - 4]
            #back page
            finalarray.append(startarray[len(startarray) - 3])
            del startarray[len(startarray) - 3]
            finalarray.append(startarray[len(startarray) - 3])
            del startarray[len(startarray) - 3]
            finalarray.append(startarray[2])
            del startarray[2]
            finalarray.append(startarray[2])
            del startarray[2]
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]
            finalarray.append(startarray[0])
            del startarray[0]
            finalarray.append(startarray[0])
            del startarray[0]

    elif eightorsixteen == 8:

        while (len(startarray) > 7):
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]
            finalarray.append(startarray[0])
            del startarray[0]
            finalarray.append(startarray[len(startarray) - 2])
            del startarray[len(startarray) - 2]
            finalarray.append(startarray[1])
            del startarray[1]
            finalarray.append(startarray[0])
            del startarray[0]
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]
            finalarray.append(startarray[0])
            del startarray[0]
            finalarray.append(startarray[len(startarray) - 1])
            del startarray[len(startarray) - 1]


    return finalarray

#an array with as many numbers in it as there are pages in the final document
def finalnumberarray_filler(numberofpages):
    array = []
    for i in range(1, numberofpages+1):
        array.append(i)

    return array

def filesaving(outputpdf):
    #https://stackoverflow.com/questions/68447801/prompt-user-to-choose-the-name-and-location-when-saving-a-pdf-python
    save = filedialog.asksaveasfile(defaultextension="*.pdf", filetypes=(("PDF files", "*.pdf"),))
    if save is None:
        return

    # .name is needed to access the filename, otherwise error thrown
    #https://stackoverflow.com/questions/60206105/code-error-typeerror-expected-str-bytes-or-os-pathlike-object-not-io-textio
    outputfile = open(save.name, 'wb')
    outputpdf.write(outputfile)
    outputfile.close()
    outputpdf = PdfFileWriter()
    save.close()
