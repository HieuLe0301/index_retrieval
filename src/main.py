from llm.prompts import heading_hirarchy
from llm.client import chat

from pipeline.input import load_pdf

def main():
    # response = 
    # print(response)

    pdf_dir_path = "input"
    pdf_name = "OOP_2013.pdf"
    pdf = load_pdf(pdf_dir_path, pdf_name)
    print(pdf[:10000])


if __name__ == '__main__':
    main()
