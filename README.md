# PDF Merger Tool

A simple Python tool to merge multiple PDF files in a given directory into a single PDF file.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- PyPDF2 module. If not installed, run: `pip install pypdf2`

## Usage

1. Clone this repository:
    ```
    git clone https://github.com/AlteredAdmin/PDF-Merger
    ```

2. Navigate to the directory:
    ```
    cd [Directory Name]
    ```

3. Run the script:
    ```
    python PDFMerger.py
    ```

4. Enter the path of the folder containing the PDFs you wish to merge.

5. The program will list all the PDF files found in the directory.

6. Specify a name for the resulting merged PDF file. If you do not provide a `.pdf` extension, the program will append it for you.

7. The tool will merge all the PDFs and save the resulting file in an 'Output' directory located within the source directory.

8. After the process is complete, the merged PDF will automatically open.

## Notes

- If any PDF files fail to merge, the tool will notify you and move on to the next file.
- If the 'Output' directory does not exist, the tool will create one.

## Support the Developer

If you found this helpful, please consider:

- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)


