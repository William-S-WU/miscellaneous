"""
William Schmitt schmittw@wustl.edu
PDF to XLSX converter
creates excel file with the first sheet being all the text from the pdf.
All tables are saved in seperate sheets.   
"""

import os
import pandas as pd #may need numpy 
import camelot
import fitz  # called PyMuPDF
import re


def clean_text(text):  # Removes non-printable ASCII control characters from the text.

    # Define illegal characters
    illegal_chars_pattern = re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]')
    # Remove illegal characters
    return illegal_chars_pattern.sub('', text)

def extract_text(pdf_document):
    
    # Open the PDF file
    document = fitz.open(pdf_document)
    
    # Extract text from each page
    pdf_text = []
    for page_number in range(len(document)):
        page = document[page_number]
        text = page.get_text("text")  # Extract plain text
        pdf_text.append(text.strip().split('\n'))  # Split text by line and store each line
    
    # Convert extracted text to a DataFrame
    flattened_text = [line for page in pdf_text for line in page]
    df = pd.DataFrame(flattened_text, columns=['Text'])

    df = df.map(clean_text)

    
    #print(pdf_document, type(pdf_document))
    pdf_document = pdf_document.replace(" ","_")
    #print(pdf_document, type(pdf_document))
    pdf_document = "".join([pdf_document, ".xlsx"])
    #df.to_excel(pdf_document, sheet_name="text", index=False)
    return(df)

    #print(f"Text from {pdf_document} has been saved to xlsx_file.")

def extract_tables(filename, directory, df_text):
    tables = camelot.read_pdf(os.path.join(directory, filename), pages='all',flavor='stream')#stream used when tables are unclear, remove if tables are clearly boxed in for better results
    #print("pdf found")
    # Find the PDF name and save for new excel file
    output_filename = f'{os.path.splitext(filename)[0]}.xlsx'
    output_filename = output_filename.replace(" ","_")




    
    with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
        #first sheet
        df_text.to_excel(writer, sheet_name="full_text", index=False)
  
        # Iterate over each table
        for i, table in enumerate(tables):
            df = table.df
            # Set the first row as header
            df.columns = df.iloc[0]
            df = df[1:]
            sheet_name = f'Table_{i+1}'
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
    #print(f"Tables from {filename} have been saved to '{output_filename}'")







#print("Current working directory:", os.getcwd())  # Use to find current directory
directory = os.getcwd()  # Replace if working directory is not the desired directory

for filename in os.listdir(directory):
    #print("doing something")
    if filename.lower().endswith(".pdf"):
        #print("doing something")
        df_text = extract_text(filename)
        #print(type(df_text))
        extract_tables(filename, directory, df_text)

print("Program has finished running")
