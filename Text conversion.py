from googletrans import Translator

# Function to read the text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to translate text from Telugu to English
def translate_text(text, src_lang='te', dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

# Main function
def main(file_path):
    telugu_text = read_text_file(file_path)
    print("Original Telugu Text:")
    print(telugu_text)
    
    translated_text = translate_text(telugu_text)
    print("\nTranslated English Text:")
    print(translated_text)

# Specify the path to your text file
file_path = r'C:\Users\ramji\Desktop\telugu_text.txt'  # Use a raw string (r'') or double backslashes (\\)

# Run the main function
if __name__ == '__main__':
    main(file_path)
