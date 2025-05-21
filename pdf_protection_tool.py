import sys
import PyPDF2
from PyPDF2.errors import PdfReadError

def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        # Open the input PDF in binary read mode
        with open(input_pdf, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pdf_writer = PyPDF2.PdfWriter()

            # Copy all pages from reader to writer
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Encrypt the PDF with the given password
            pdf_writer.encrypt(password)

            # Write the encrypted PDF to the output file
            with open(output_pdf, "wb") as output_file:
                pdf_writer.write(output_file)

        print(f"Successfully created password-protected PDF: {output_pdf}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_pdf}' not found.")
    except PdfReadError:
        print(f"Error: Unable to read PDF file '{input_pdf}'. It might be corrupted or invalid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python pdf_protection_tool.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf, output_pdf, password)

if __name__ == "__main__":
    main()
