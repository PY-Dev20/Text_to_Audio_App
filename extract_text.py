import PyPDF2

file_path = "PDF_AUDIO_READER-Master/abc.pdf"

with open(file_path, "rb") as file_object:
    pdf_reader = PyPDF2.PdfReader(file_object)

    extracted_text = ""

    for page_num in range(len(pdf_reader.pages)):
        pdf_page_obj = pdf_reader.pages[page_num]
        extracted_text += pdf_page_obj.extract_text()

print(extracted_text)
