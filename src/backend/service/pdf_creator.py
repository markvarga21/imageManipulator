from tempfile import TemporaryFile
import uuid
import os
import pyrebase as pb

from fpdf import FPDF

from service.cleaner_service import clean_output_for_user

PAGE_WIDTH = 190
RATIO = 3

CONFIG = {
    'apiKey': "AIzaSyCT83UsUX2pnGtVa0l9q2rOwRAQFCdZbv4",
    'authDomain': "image-manipulator-f3cb8.firebaseapp.com",
    'projectId': "image-manipulator-f3cb8",
    'storageBucket': "image-manipulator-f3cb8.appspot.com",
    'messagingSenderId': "337971216404",
    'appId': "1:337971216404:web:f57da6af15fefe8d8ae701",
    'databaseURL': ''
}

FIREBASE = pb.initialize_app(config=CONFIG)
STORAGE = FIREBASE.storage()


FONT_PATH = 'fonts/roboto.ttf'


def save_pdf_file_in_output_folder(text: str, r: int, g: int, b: int, font_size: int, user_name: str) -> str:
    clean_output_for_user(user_name=user_name)
    pdf = FPDF()
    STORAGE.child(FONT_PATH).download(
        filename='roboto.ttf', path='./resources/')
    font_path = ('./roboto.ttf')
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
