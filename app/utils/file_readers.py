import pandas as pd
import pdfplumber
from odf.opendocument import load

def read_pdf(file_path: str) -> str:
    with pdfplumber.open(file_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages)

def read_csv(file_path: str) -> str:
    return pd.read_csv(file_path).to_string()

def read_odt(file_path: str) -> str:
    doc = load(file_path)
    return "\n".join(paragraph.firstChild.data for paragraph in doc.text.getElementsByType('p'))

def read_csv2(file_path: str) -> str:
    #a =pd.read_csv(file_path)
    #transcripts = a['transcript']
    #uuids = a['uuid']
    return pd.read_csv(file_path)
    #return a