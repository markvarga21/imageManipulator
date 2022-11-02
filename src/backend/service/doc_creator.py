import os
import uuid
import aspose.words as aw

from service.cleaner_service import clean_output_for_user


def save_doc_file_in_output_folder(text: str, font_size: int, user_name: str) -> str:
    clean_output_for_user(user_name=user_name)
    doc = aw.Document()

    builder = aw.DocumentBuilder(doc)

    font = builder.font
    font.size = font_size
    font.name = 'Times New Roman'

    paragraph_format = builder.paragraph_format
    paragraph_format.first_line_indent = 8
    paragraph_format.alignment = aw.ParagraphAlignment.JUSTIFY
    paragraph_format.keep_together = True

    builder.writeln(text)

    save_id = uuid.uuid4()
    name = f'OCR_{user_name}_{save_id}.doc'
    path = os.path.join('resources', 'output', name)
    doc.save(path)
    return path
