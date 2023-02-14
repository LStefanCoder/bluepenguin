import tkinter
from tkinter import *
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from tkinter import filedialog
from tkinter import ttk #for the styling among other things
from ttkthemes import ThemedTk #the theme
import sys #sys.exit to close the process

#importing from the other python files
from auxiliary import pagenumberarray_filler
from auxiliary import finalnumberarray_filler
from auxiliary import filesaving
from auxiliary import aboutwindow
from pagecompleter import completeDocument
from pageconcatenator import concatenator

#variable to check whether a file is open or not
isfileopen = False
numberofpages = 0
filename = ""
filenamearray = []
pdfFileObj = None
pdfReader = None
updated_numberofpages = 0
outputpdf = PdfFileWriter()
finalPdf = None


#https://www.reddit.com/r/Python/comments/lps11c/how_to_make_tkinter_look_modern_how_to_use_theme
root = ThemedTk(theme='yaru')
root.title('BluePenguin')
root.iconbitmap('icon/BluePenguin.ico')
#https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
root.geometry('350x150')
root.minsize(350, 150)


def fileopening():
    #https://www.youtube.com/watch?v=YXPyB4XeYLA, around 2:50
    root.filename = filedialog.askopenfilename(initialdir='/', title="Select a pdf file", filetypes=(("Pdf files", "*.pdf"),))
    #breaks out of this function if the user clicks cancel on the opening dialog
    if root.filename == '':
        return
    #https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
    pdfFileObj = open(root.filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    numberofpages = pdfReader.getNumPages()

    # code to print out the name of the file
    filename = os.path.basename(root.filename)
    #changes the filenamelabel to show the filename
    #based on https://www.tutorialspoint.com/python/tk_radiobutton.htm#
    filenamelabel.config(text=filename)
    rightlabel_1.config(text="Number of pages: " + str(numberofpages))

    # variable to distinguish between the opening state and the state after a file had been opened
    isfileopen = True


def converting():
    #.get() needed to get the appropriate value
    #based on second example here: https://www.inf-schule.de/software/gui/entwicklung_tkinter/auswahl/radiobutton
    eightorsixteen = fouroreight.get()
    print(eightorsixteen)
    if root.filename == '':
        return
    pdfFileObj = open(root.filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # counting the number of pages in the pdf file
    original_numberofpages = pdfReader.getNumPages()

    #adds blank pages to the document until it is processable by the next function
    completedDocument = completeDocument(pdfFileObj, original_numberofpages, eightorsixteen)

    # number of pages now that the document had been completed
    updated_numberofpages = completedDocument.getNumPages()

    #updates the label which shows the number of pages the document has
    rightlabel_2.config(text="Final number of pages: " + str(updated_numberofpages))

    # the array which contains the page numbers in the correct order
    numberarray = pagenumberarray_filler(updated_numberofpages, eightorsixteen)
    print(numberarray)

    newPdf = concatenator(completedDocument, eightorsixteen, updated_numberofpages, numberarray)

    finalnumberofpages = newPdf.getNumPages()
    finalnumberarray = finalnumberarray_filler(finalnumberofpages)


    finalPdf = PdfFileWriter()

    for i in range(0, len(finalnumberarray)):
        finalPdf.addPage(newPdf.getPage(finalnumberarray[i] - 1))
        #this is there to make the pdf accessible e.g. for the save as file dialog
        outputpdf.addPage(newPdf.getPage(finalnumberarray[i] - 1))


    return finalPdf

#def concatenating():

#radiobuttons for the user to select whether he wants a 4 or a 8 page layout and if he wants to add A4 or Letter-sized blank pages
fouroreight = IntVar()


#this button does the file opening dialog
openfilebutton = ttk.Button(root, text="Open file", command=fileopening, padding=5)
openfilebutton.grid(row=1, column=1)

filenamelabel = ttk.Label(root, text="Select a file")
filenamelabel.grid(row=2, column=1)

startconversionbutton = ttk.Button(root, text="Convert!", command=converting, padding=5)
startconversionbutton.grid(row=5, column=1)

radioframe = ttk.Frame(root)
radioframe.grid(row=3, column=1)

#anchor='w' doesn't seem to work with ttk
radiobutton_4p = ttk.Radiobutton(master=radioframe, text="4-page layout", value=8, variable=fouroreight)
radiobutton_4p.grid(row=4, column=1)
radiobutton_8p = ttk.Radiobutton(master=radioframe, text="8-page layout", value=16, variable=fouroreight)
radiobutton_8p.grid(row=4, column=2)
fouroreight.set(8)

rightlabel_1 = ttk.Label(root, text="Number of pages: " + str(numberofpages))
rightlabel_1.grid(row=1, column=2)
rightlabel_2 = ttk.Label(root, text="Final number of pages: " + str(updated_numberofpages))
rightlabel_2.grid(row=2, column=2)

#lambda used to enable passing arguments
savefilebutton = ttk.Button(root, text="Save file", command=lambda: filesaving(outputpdf), padding=5)
savefilebutton.grid(row=6, column=1)

#######menu
menubar = Menu(root)

root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Open file", command=fileopening)
filemenu.add_command(label="Convert file", command=converting)
filemenu.add_separator()
filemenu.add_command(label="Quit    (Ctrl+q)", command=sys.exit)

aboutmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='About', menu=aboutmenu)
aboutmenu.add_command(label="About software", command=lambda: aboutwindow(root))

######keyboard shortcuts
#root.bind("<Control-r>", converting())
#root.bind("<o>", fileopening())
root.bind("<Control-q>", sys.exit) #closes the program

#closing the pdf file if there is one, otherwise there would be an error thrown
if pdfFileObj is not None:
    pdfFileObj.close()

root.mainloop()
#window opened again when closed -- only to be used in when developing and the window appears again a second time -- error message can be ignored
#root.destroy()
#https://stackoverflow.com/questions/26222538/why-does-my-window-reopen-when-closed