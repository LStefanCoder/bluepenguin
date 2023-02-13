import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

#1 inch equals 72 user units (https://kb.itextpdf.com/home/it5kb/faq/how-to-get-the-userunit-from-a-pdf-file)
#A4 is 8.3*11.7 in (210*297 mm) (https://en.wikipedia.org/wiki/ISO_216)

def completeDocument(document, numberofpages, eightorsixteen):

    #https://stackoverflow.com/questions/53010011/how-to-append-new-blank-page-at-the-end-of-pdf-file-using-python
    #https://pythonguides.com/pdffilewriter-python-examples/
    #inpdf = PyPDF2.PdfFileReader(document)
    inpdf = PdfFileReader(document)
    outPdf = PdfFileWriter()

    pagewidth = 597.6
    pageheight = 842.4

    for x in range(0,numberofpages):
        outPdf.addPage(inpdf.getPage(x))

    #print(outPdf.getNumPages())

    if (eightorsixteen == 8):
        if (numberofpages % 8 == 1):
            for x in range(1,8):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 2):
            for x in range(1,7):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 3):
            for x in range(1, 6):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 4):
            for x in range(1, 5):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 5):
            for x in range(1, 4):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 6):
            for x in range(1, 3):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 8 == 7):
            for x in range(1, 2):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        #else:
            #outPdf.addBlankPage(width=pagewidth, height=pageheight)

    elif (eightorsixteen == 16):

        if (numberofpages % 16 == 1):
            for x in range(1,16):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 2):
            for x in range(1,15):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 3):
            for x in range(1, 14):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 4):
            for x in range(1, 13):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 5):
            for x in range(1, 12):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 6):
            for x in range(1, 11):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 7):
            for x in range(1, 10):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 8):
            for x in range(1, 9):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 9):
            for x in range(1, 8):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 10):
            for x in range(1, 7):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 11):
            for x in range(1, 6):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 12):
            for x in range(1, 5):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 13):
            for x in range(1, 4):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 14):
            for x in range(1, 3):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        elif (numberofpages % 16 == 15):
            for x in range(1, 2):
                outPdf.addBlankPage(width=pagewidth, height=pageheight)
        #else:
            #outPdf.addBlankPage(width=pagewidth, height=pageheight)


    print(outPdf.getNumPages())

    return outPdf