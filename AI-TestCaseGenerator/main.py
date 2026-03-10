from image_extractor import extract_images
from ocr_reader import extract_text_from_image
from step_cleaner import extract_steps_from_text
from ai_generator import generate_test_case
import os

docx_file = "AI-TestCaseGenerator/input/TestSnagit.docx"

extract_images(docx_file)


image_folder = "images/word/media"

all_text = ""

for image in os.listdir(image_folder):

    if image.endswith(".png"):

        path = os.path.join(image_folder, image)

        text = extract_text_from_image(path)

        all_text += text + "\n"

steps = extract_steps_from_text(all_text)

print("\nDetected Steps:\n")

for step in steps:
    print(step)

print("\nGenerating Test Case...\n")

test_case = generate_test_case(steps)

print(test_case)