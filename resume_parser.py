from pypdf import PdfReader


def read_resume(file):

    reader = PdfReader(file)

    text = ""


    for page in reader.pages:

        content = page.extract_text()

        if content:

            text += content + "\n"


    return text