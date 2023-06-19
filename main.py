import base64

import streamlit as st
from translator import google_text_translate
from speak_text import speak_text


@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

if __name__ == "__main__":

    hide_streamlit_style = f"""
                <style>
                footer {{visibility: hidden;}}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    volume_button_img = get_base64_of_bin_file("volume.png")

    all_langs = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'burmese': 'my', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'finnish': 'fi', 'french': 'fr', 'western frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'gujarati': 'gu', 'hausa': 'ha', 'hebrew': 'he', 'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'kannada': 'kn', 'kazakh': 'kk', 'central khmer': 'km', 'korean': 'ko', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'oriya': 'or', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'russian': 'ru', 'samoan': 'sm', 'serbian': 'sr', 'shona': 'sn', 'sindhi': 'sd', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'southern sotho': 'st', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tagalog': 'tl', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

    st.markdown("<h1 style='text-align: center; color: rgb(211, 211, 211);'>LANGUAGE TRANSLATOR</h1>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------------------------')

    with st.container():
        uploaded_file = st.file_uploader("Choose a Text file or write the Text below", type=["txt"])

    st.markdown("<h1 style = 'text-align: center; color: rgb(211, 211, 211); '> OR</h1>", unsafe_allow_html= True)

    if uploaded_file is None:
        src_txt = st.text_area("Write the text to be translated")
    elif uploaded_file is not None:
        content = uploaded_file.getvalue().decode('utf-8')
        src_txt = st.text_area("Write the text to be translated", content)

    col1, col2 = st.columns(2, gap = 'large')

    with col1:
        options = all_langs.keys()
        lang = st.selectbox("Select the Target Language", options = options)

    with col2:
        st.write(" ")
        st.write(" ")
        trans_button = st.button('Translate')
        st.markdown("""<style>
                    [class = "css-pny9xi e1ewe7hr10"]{
                        height: 40px;
                        width: 300px;  
                        border: 5px;  
                        display: flex;  
                        justify-content: center;  
                        align-items: center;  
                    }
                    </style>
                    """, unsafe_allow_html= True)

    if trans_button:
        trans_text = google_text_translate(src_txt, lang)

        try:
            if trans_text == "Error!":
                st.warning('Source Text field is Empty!', icon ="⚠️")
            else:
                target_txt = st.text_area("Translated Text", trans_text)

        except:
            target_txt = st.text_area("Translated Text")

        if trans_text!="Error!":
            try:
                speak_text(trans_text, all_langs[lang.lower()])
            except Exception as e:
                st.write(e)


    #BELOW IS THE CODE TO MAKE A BUTTON THAT WILL PLAY THE TRANSLATED TEXT ON CLICKING IT

    # button_html = f'''
    # <button style="border:none; background:none;
    #     padding:0;
    #     display: block;
    #     margin-left: auto;
    #     margin-right: auto;
    #     width: 50%;">
    #     <img src="data:image/png;base64, {volume_button_img}" alt="Image Button" width="100" height="100">
    # </button>
    # '''
    #
    # play_butt = st.markdown(button_html, unsafe_allow_html= True)
    # if play_butt:
    #     try:
    #         speak_text(trans_text, all_langs[lang.lower()])
    #     except:
    #         st.warning('You need to Translate First!', icon ="⚠️")

    custom_styles = """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                text-align: center;
                padding: 10px;
                color: gray;
            }
            .footer a {
                color: gray;
            }
        </style>
    """

    # Custom footer content with hyperlink
    custom_footer = '''
        <div class="footer">
            Made by <a href="https://www.linkedin.com/in/aniket-kajania-0033271a0">Aniket Kajania</a>
        </div>
    '''

    # Render custom styles and footer
    st.markdown(custom_styles, unsafe_allow_html=True)
    st.markdown(custom_footer, unsafe_allow_html=True)
