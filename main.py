import os
from PyPDF2 import PdfFileMerger


start_path = os.getcwd() + "/start"
end_path = os.getcwd() + "/end"


def process_files(pdf_files):
    merger = PdfFileMerger()
    for file in os.listdir(pdf_files):
        if file.endswith(".pdf"):
            merger.append(start_path + "/" + file)

    merger.write(end_path + '/results.pdf')
    merger.close()


def init():
    base_dir = os.getcwd()
    process_files(base_dir + '/start')


init()
