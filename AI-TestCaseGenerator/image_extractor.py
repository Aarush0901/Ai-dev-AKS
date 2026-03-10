import zipfile
import os

def extract_images(docx_path):

    output_folder = "images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with zipfile.ZipFile(docx_path, 'r') as docx:

        for file in docx.namelist():

            if file.startswith("word/media/"):

                docx.extract(file, output_folder)

    print("Images extracted successfully.")