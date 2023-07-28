import os
from PyPDF2 import PdfMerger


start_path = os.path.join(os.getcwd(), "start")
end_path = os.path.join(os.getcwd(), "end")


def process_files(pdf_files):
    merger = PdfMerger()
    for file in os.listdir(pdf_files):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(start_path, file)
            merger.append(pdf_path)

    output_path = os.path.join(end_path, "results.pdf")
    with open(output_path, "wb") as output_file:
        merger.write(output_file)


def init():
    base_dir = os.getcwd()
    process_files(os.path.join(base_dir, "start"))


init()
