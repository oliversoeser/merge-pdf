from pypdf import PdfMerger
import sys

files = [file for file in sys.argv[1:] if file.endswith(".pdf")]

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write(files[0][:files[0].rfind("\\")] + "\\merge.pdf")
merger.close()