from pypdf import PdfReader
import os, json

'''
Sửa phông chữ cũ TCVN3 của 1 số các pdf file
'''
# Phông cũ TCVN3
_TCVN3_FONTS = {"TT2A6t00", "TT2A7t00"}

# 2 bộ kí tự tcvn3 và unicode tương ứng
_TCVN3_CHARS = "µ¸¶·¹¨»¾¼½Æ©ÇÊÈÉË®ÌÐÎÏÑªÒÕÓÔÖ×ÝØÜÞßãáâä«åèæçé¬êíëìîïóñòô­õøö÷ùúýûüþ¡¢§£¤¥¦"
_UNICODE_CHARS = "àáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵĂÂĐÊÔƠƯ"


_TCVN3_TO_UNICODE = str.maketrans(_TCVN3_CHARS, _UNICODE_CHARS)

# Chữ ư bị thay thành dấu hyphen lol
_TCVN3_TO_UNICODE[ord("−")] = "ư" 


def _fix_font(page):
    parts = []

    def visit(text, _cm, _tm, font, _size):
        font_name = str((font or {}).get("/BaseFont", "")).rsplit("+", 1)[-1]          # Để lấy ra tên font thôi, k cần hiểu đâu =)) 
        if font_name in _TCVN3_FONTS:
            text = text.translate(_TCVN3_TO_UNICODE)
        parts.append(text)

    page.extract_text(visitor_text=visit)
    
    return "".join(parts)


def load_pdf(pdf_dir_path, pdf_name):
    pdf_path = pdf_dir_path + "/" + pdf_name
    pdf = PdfReader(pdf_path)

    # Nếu muốn lưu các file pdf thành json
    '''
    for page_number, page in enumerate(pdf.pages):
        pages.append({
            "text": _fix_font(page),
            "page": page_number,
            "source": str(pdf_path),
        })

    pdf_basename = os.path.splitext(pdf_name)
    with open("../../output/input_json/{pdf_basename}.json", "w", encoding= "utf-8") as file:
        json.dump(pages, file, ensure_ascii= False, indent = 2)
    '''
    

    full_text = " ".join([_fix_font(page) for page in pdf.pages])
    return full_text
