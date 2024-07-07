from googletrans import Translator

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def translate_text(text, src_lang='te', dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

def main(file_path):
    telugu_text = read_text_file(file_path)
    print("Original Telugu Text:")
    print(telugu_text)
    
    translated_text = translate_text(telugu_text)
    print("\nTranslated English Text:")
    print(translated_text)

file_path = r'C:\Users\ramji\Desktop\telugu_text.txt'  # Use a raw string (r'') or double backslashes (\\)

if __name__ == '__main__':
    main(file_path)
