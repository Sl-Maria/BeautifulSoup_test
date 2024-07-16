import requests
from bs4 import BeautifulSoup
from googletrans import Translator

url = "https://randomword.com/"

def get_english_words():
   try:
       response = requests.get(url)
       soup = BeautifulSoup(response.content, "html.parser")
       english_words = soup.find("div", id="random_word").text.strip()
       word_definition = soup.find("div", id="random_word_definition").text.strip()
       return {
           "english_words": english_words,
           "word_definition": word_definition
       }
   except:
       print("Произошла ошибка")

def translate_word(text):
    translator = Translator()
    translation = translator.translate(text, src="en", dest="ru")
    return translation.text

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        russian_word = translate_word(word)
        russian_definition = translate_word(word_definition)
        #print(f"Английское определение: {word_definition}")
        print(f"Русское определение: {russian_definition}")
        user = input("Что это за слово? ")
        if user == russian_word:
            print("Все верно!")
        else:
            #print(f"Ответ неверный, было загадано это слово - {russian_word} ({word})")
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет ")
        if play_again != "да":
            print("Спасибо за игру!")
            break


word_game()