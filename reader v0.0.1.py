# import packages
from PyPDF2 import PdfFileReader, PdfFileWriter
import re

# open the pdf file
Object = PdfFileReader("test.pdf")

# get number of pages
NumPages = Object.getNumPages()

# text identifier
String = "FAX COVER"

# Pdf Writer
CoverBlankWriter = PdfFileWriter()
NonCoverBlankWriter = PdfFileWriter()

for i in range(0, NumPages):
    PageObj = Object.getPage(i) 

    # Search for the text identifier
    Text = PageObj.extractText()

    # Check if page is a blank page
    if len(Text) < 1:
        CoverBlankWriter.addPage(PageObj)

    # If page is not blank then search for the Identifier
    else:

        # Search Results
        result = re.search(String, Text.upper())

        if result != None:
            CoverBlankWriter.addPage(PageObj)
        
        # If page is not blank and identifier not found
        else:
            NonCoverBlankWriter.addPage(PageObj)

# Save fax cover and blank page separately
OutputFileName = 'CoverBlankPage.pdf'

if CoverBlankWriter.getNumPages() > 0:
    with open(OutputFileName, 'wb') as Out:
        CoverBlankWriter.write(Out)

# Save non fax cover and blank page
OutputFileName = 'NonCoverBlank.pdf'

if NonCoverBlankWriter.getNumPages() > 0:
    with open(OutputFileName, 'wb') as Out:
        NonCoverBlankWriter.write(Out)