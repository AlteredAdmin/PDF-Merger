import os
from PyPDF2 import PdfFileMerger

# Define the path
path = input("Enter the folder location: ")

try:
    # Verify that path exists
    if not os.path.exists(path):
        raise IOError(f"The folder '{path}' does not exist. Please enter a valid folder location.")

    # Get all PDF files
    pdffiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.pdf')]

    if not pdffiles:
        raise IOError("No PDF files found in the provided directory.")

    print('\nList of PDF Files:\n')
    for file in pdffiles:
        print(file)

    # Define the result file
    resultFile = input("\nEnter the name of the result file : ")
    if not resultFile.endswith('.pdf'):
        resultFile += '.pdf'

    merger = PdfFileMerger()

    # Merge all pdf files
    for pdf in pdffiles:
        try:
            merger.append(os.path.join(path, pdf))
        except:
            print(f"Failed to merge {pdf}. Moving to the next file.")

    output_dir = os.path.join(path, 'Output')

    # Create output directory if not exists
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    output_file = os.path.join(output_dir, resultFile)

    # Write the output file
    merger.write(output_file)
    merger.close()

    print(f'\n{resultFile} Successfully created at {output_file}')
    os.startfile(output_file)

except Exception as e:
    print(f"An error occurred: {e}")
