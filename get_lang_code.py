import requests
from bs4 import BeautifulSoup as bs
from googletrans import Translator
import translator

def get_lang_code():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
    # response.status_code
    html = response.text
    data = bs(html, 'html.parser')

    lang = {}
    for x in data.find_all('tr'):
        if x is not None:
            if x.find('td')!=None:
                if x.find_all('td')[0].string!=None and x.find_all('td')[1].string:
                    lang[x.find_all('td')[0].string.lower()] =  x.find_all('td')[1].string
    return lang

def remove_unrecognized_lang(d):
    translator = Translator()
    languages = []

    for lang in d.keys():
        try:
            translator.translate('power', dest=d[lang])
        except ValueError:
            languages.append(lang)

    for lang in languages:
        del d[lang]

    return d

# lang_code_dict = get_lang_code()  # Assuming get_lang_code() returns the dictionary of languages and codes
# updated_dict = remove_unrecognized_lang(lang_code_dict)
# print(updated_dict)