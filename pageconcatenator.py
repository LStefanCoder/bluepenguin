import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter, PageObject, Transformation
import math

def concatenator(document, eightorsixteen, numberofpages, numberarray):

    pagewidth = 597.6
    pageheight = 842.4

    translationfactor_eight = 0.36
    translationfactor_four = 0.5



    documentreader = document

    outPdf = PdfFileWriter()

    #https://pypdf2.readthedocs.io/en/latest/user/cropping-and-transforming.html from the docs is important here
    if(eightorsixteen == 16):
        #doing this iteratively per page
        for i in range(1, int(numberofpages/8) + 1):
            # .createBlankPage is deprecated since version 1.28.0, acc. to the documentation
            #since this is a landscape page, values have to be inverted
            #refactored based on https://stackoverflow.com/questions/57477263/how-to-combine-5-pdfs-in-one-in-the-same-page

            #creates empty page
            grouppage = PageObject.create_blank_page(None, pageheight, pagewidth)

            page1 = documentreader.getPage(numberarray[0 + (i - 1) * 8] - 1)
            page2 = documentreader.getPage(numberarray[1 + (i - 1) * 8] - 1)
            page3 = documentreader.getPage(numberarray[2 + (i - 1) * 8] - 1)
            page4 = documentreader.getPage(numberarray[3 + (i - 1) * 8] - 1)
            page5 = documentreader.getPage(numberarray[4 + (i - 1) * 8] - 1)
            page6 = documentreader.getPage(numberarray[5 + (i - 1) * 8] - 1)
            page7 = documentreader.getPage(numberarray[6 + (i - 1) * 8] - 1)
            page8 = documentreader.getPage(numberarray[7 + (i - 1) * 8] - 1)

            #scaling all pages down equally
            transformation = Transformation().scale(sx=translationfactor_eight, sy=translationfactor_eight)

            page1.add_transformation(transformation)
            page2.add_transformation(transformation)
            page3.add_transformation(transformation)
            page4.add_transformation(transformation)
            page5.add_transformation(transformation)
            page6.add_transformation(transformation)
            page7.add_transformation(transformation)
            page8.add_transformation(transformation)

            #orienting all pages based on page8 surprisinly worked

            page8.mediabox = grouppage.mediabox
            grouppage.mergePage(page8)

            page6.add_transformation(
                Transformation().translate(page8.mediabox.right - (math.floor(pageheight * (3 / 4))), 0))
            page6.mediabox = grouppage.mediabox
            grouppage.mergePage(page6)

            page4.add_transformation(
                Transformation().translate(page8.mediabox.right - (math.floor(pageheight * (2 / 4))), 0))
            page4.mediabox = grouppage.mediabox
            grouppage.mergePage(page4)

            page2.add_transformation(
                Transformation().translate(page8.mediabox.right - (math.floor(pageheight * (1 / 4))), 0))
            page2.mediabox = grouppage.mediabox
            grouppage.mergePage(page2)

            page7.add_transformation(Transformation().translate(0, page8.mediabox.bottom + math.floor(pagewidth/2)))
            page7.mediabox = grouppage.mediabox  # ensure it is visible
            grouppage.mergePage(page7)

            page5.add_transformation(Transformation().translate(0 + (math.floor(pageheight * (1 / 4))), page8.mediabox.bottom + math.floor(pagewidth/2)))
            page5.mediabox = grouppage.mediabox
            grouppage.mergePage(page5)

            page3.add_transformation(Transformation().translate(0 + (math.floor(pageheight * (2 / 4))), page8.mediabox.bottom + math.floor(pagewidth/2)))
            page3.mediabox = grouppage.mediabox
            grouppage.mergePage(page3)

            page1.add_transformation(Transformation().translate(0 + (math.floor(pageheight * (3 / 4))), page8.mediabox.bottom + math.floor(pagewidth/2)))
            page1.mediabox = grouppage.mediabox
            grouppage.mergePage(page1)

            outPdf.addPage(grouppage)

    elif(eightorsixteen == 8):
        # doing this iteratively per page
        for i in range(1, int(numberofpages / 8) + 1):
            # .createBlankPage is deprecated since version 1.28.0, acc. to the documentation
            # since this is a landscape page, values have to be inverted
            # refactored based on https://stackoverflow.com/questions/57477263/how-to-combine-5-pdfs-in-one-in-the-same-page

            # creates empty page
            grouppage = PageObject.create_blank_page(None, pagewidth, pageheight)

            page1 = documentreader.getPage(numberarray[0 + (i - 1) * 4] - 1)
            page2 = documentreader.getPage(numberarray[1 + (i - 1) * 4] - 1)
            page3 = documentreader.getPage(numberarray[2 + (i - 1) * 4] - 1)
            page4 = documentreader.getPage(numberarray[3 + (i - 1) * 4] - 1)

            # scaling all pages down equally
            transformation = Transformation().scale(sx=translationfactor_four, sy=translationfactor_four)

            page1.add_transformation(transformation)
            page2.add_transformation(transformation)
            page3.add_transformation(transformation)
            page4.add_transformation(transformation)

            # orienting all pages based on page8 surprisinly worked

            page4.mediabox = grouppage.mediabox
            grouppage.mergePage(page4)

            page2.add_transformation(
                Transformation().translate(0 + math.floor(pagewidth / 2), 0))
            page2.mediabox = grouppage.mediabox
            grouppage.mergePage(page2)


            page3.add_transformation(Transformation().translate(0, page4.mediabox.bottom + math.floor(pageheight / 2)))
            page3.mediabox = grouppage.mediabox  # ensure it is visible
            grouppage.mergePage(page3)

            page1.add_transformation(Transformation().translate(0 + math.floor(pagewidth / 2), page4.mediabox.bottom + math.floor(pageheight / 2)))
            page1.mediabox = grouppage.mediabox
            grouppage.mergePage(page1)


            outPdf.addPage(grouppage)

    return outPdf
