### HERE I HAVE USED GOOGLETRANS API TO TRANSLATE THE TEXT FROM ONE LANGUAGE TO ANOTHER AND PLAY THE TRANSLATED TEXT
from get_lang_code import get_lang_code
from googletrans import Translator
from speak_text import speak_text

all_languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'burmese': 'my', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'finnish': 'fi', 'french': 'fr', 'western frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'gujarati': 'gu', 'hausa': 'ha', 'hebrew': 'he', 'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'kannada': 'kn', 'kazakh': 'kk', 'central khmer': 'km', 'korean': 'ko', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'oriya': 'or', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'russian': 'ru', 'samoan': 'sm', 'serbian': 'sr', 'shona': 'sn', 'sindhi': 'sd', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'southern sotho': 'st', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tagalog': 'tl', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def google_text_translate(text, dest_lang):
    translator = Translator()
    if len(text) == 0:
        return "Error!"
    return translator.translate(text, dest=dest_lang).text


# source_text = input("Enter a text: ")
# target_lang = input("Enter the language in which you want to translate: ")
#
# if target_lang.lower() in all_languages.keys():
#     dest = all_languages[target_lang.lower()]
#     translated_text = google_text_translate(source_text, dest)
#     print("Translated text:", translated_text)
#     speak_text(translated_text, dest)
# else:
#     print("Unknown target language")
