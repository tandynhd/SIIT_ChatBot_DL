from googletrans import Translator

text1 = input("Enter text: ")


translator = Translator()


print("Translate English to Thai : ", translator.translate(
    text1, src='en', dest='th').text)
