import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "The minister has been on the take from business interests for years."
spacy_streamlit.visualize(models, default_text)
