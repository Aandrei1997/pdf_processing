import PyPDF2
import sys

def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(pdf)
  merger.write('super.pdf')

def pdf_watermark(pdf_file, watermark_file):
  with open(pdf_file, 'rb') as input_file, open(watermark_file, 'rb') as watermark_file:
    input_pdf = PyPDF2.PdfFileReader(input_file)
    watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    writer = PyPDF2.PdfFileWriter()

    for i in range(0, input_pdf.getNumPages()):
      pdf_page = input_pdf.getPage(i)
      pdf_page.mergePage(watermark_page)
      writer.addPage(pdf_page)

    with open('watermark_pdf_file.pdf', 'wb') as new_file:
      writer.write(new_file)

inputs = sys.argv[1:]

pdf_combiner(inputs)
pdf_watermark('super.pdf', 'wtr.pdf')
