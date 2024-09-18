import PyPDF2
import requests

def Document(url):
    # download and save pdf to file
    r = requests.get(url)
    with open(f'temp.pdf', 'wb') as f:
        f.write(r.content)
    text = []

    # read pdf in binary mode
    with open("temp.pdf", 'rb') as f:
        # Create a PDF object
        pdf = PyPDF2.PdfReader(f)
        # iterate over every page in PDF
        for page in range(len(pdf.pages)):
            # get the page object
            page_obj = pdf.pages[page]
            # extract text from page
            text.append(page_obj.extract_text())

    text = '\n'.join(text)