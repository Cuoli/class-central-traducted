import os
from bs4 import BeautifulSoup
from translate import Translator
import time


def translate_html(file_path, dest_language='hi'):
    with open(file_path, 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    translated_texts = {}

    for sstr in soup.strings:
        if not sstr:
            continue
        translator = Translator(provider='libre', to_lang=dest_language, base_url='http://localhost:5000')
        translated_text = translator.translate(sstr.strip())
        translated_texts[sstr] = translated_text

    html = str(soup)
    for original_text, translated_text in translated_texts.items():
        html = html.replace(f'>{original_text}<', f'>{translated_text}<')

    with open(file_path, 'w', encoding='UTF-8') as translated_file:
        translated_file.write(html)


start_time = time.time()
file_time = start_time
for root, dirs, files in os.walk("."):
    for file_name in files:
        if file_name.endswith(".html"):
            file_time = time.time()
            file_path = os.path.join(root, file_name)
            print(file_name)
            file_start_time = time.time()
            translate_html(file_path)
            print("File time: ", time.time() - file_start_time, " seconds")

end_time = time.time()
print('---------------------')
print("Total time taken: ", (end_time - start_time)/60, " minutes")
