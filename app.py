import streamlit as st
from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text(text, dest_language):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=dest_language)
        return translated_text.text
    except AttributeError as e:
        st.error("Google Translate API error: Please try again later.")
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return None

# Streamlit app
def main():
    st.title("Multilingual Translation App")
    
    # Input text
    input_text = st.text_area("Enter text to translate:")
    
    # Select destination language
    dest_languages = {lang_name: lang_code for lang_code, lang_name in LANGUAGES.items()}
    dest_language = st.selectbox("Select Destination Language:", list(dest_languages.keys()))
    
    # Translate button
    if st.button("Translate"):
        if input_text.strip():  # Check if input text is not empty or whitespace
            translated_text = translate_text(input_text, dest_languages[dest_language])
            if translated_text:
                st.info("Translated Text {dl}:{tt}".format(dl=dest_language,tt=translated_text))
                
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
