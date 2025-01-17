Readme
pdftoxlsx
William Schmitt - schmittw@wustl.edu

To run script put this script in directory with all pdf's that need to be converted and run pdf_to_xlsx.py

First all text is scraped from pdf and placed in the first excel sheet. Next all extracts tables from pdf files. It saves each table into a sheet of a new excel file that has the same name as the original pdf.
This Process is repeated for all pdfs in the working directory.  

requirements 
python 
camelot-py
numpy==1.21.0
pandas
PyMuPDF
