from googletrans import Translator
# import googletrans
# print(googletrans.LANGUAGES)
translator = Translator()
try:
    with open('./Fileio/test.txt', mode='r') as test_file:
        text = test_file.read()
        result = translator.translate(text, dest='ur')
        print(result.text)
except FileNotFoundError as e:
    print('File does not exists Silly!')