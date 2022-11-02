from tempfile import TemporaryFile
import uuid
import os

from fpdf import FPDF

from service.cleaner_service import clean_output_for_user

PAGE_WIDTH = 190
RATIO = 3


def save_pdf_file_in_output_folder(text: str, r: int, g: int, b: int, font_size: int, user_name: str) -> str:
    clean_output_for_user(user_name=user_name)
    pdf = FPDF()
    font_path = os.path.join(os.getcwd(), 'resources', 'Roboto-Light.ttf')
    pdf.add_font('Roboto', '', font_path, uni=True)
    pdf.add_page(orientation='portrait')
    pdf.set_text_color(r=r, g=g, b=b)
    pdf.set_font('Roboto', size=font_size)
    pdf.multi_cell(w=PAGE_WIDTH, h=font_size / RATIO, txt=text)

    save_id = uuid.uuid4()
    name = f'OCR_{user_name}_{save_id}.pdf'
    path = os.path.join('resources', 'output', name)
    pdf.output(path)
    return path
