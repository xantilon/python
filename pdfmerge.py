import PyPDF2
import argparse

parser = argparse.ArgumentParser(description='Merge PDFs and write them to new PDF. Existing will be overwritten.')
parser.add_argument('dest_pdf', type=argparse.FileType('wb', 0))
parser.add_argument('source_pdf', type=argparse.FileType('rb', 0), nargs='+')


#parser.parse_args(['out.pdf','det.pdf','edi.pdf'])

args = parser.parse_args()

#print(args.source_pdf[0].name)
#parser.print_help()

merger = PyPDF2.PdfFileMerger()
for pdf in args.source_pdf:
  merger.append(pdf.name)
  
merger.write(args.dest_pdf.name)

