import streamlit as st
import pandas as pd
import openai
import json
import utils
from utils import get_message
from utils import get_system_prompt, get_companies_prompt, get_non_companies_prompt
from st_pages import show_pages, Page, add_page_title

# st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

if not utils.check_password():
    st.stop()

#  :home:, :atom_symbol:, :toolbox:
show_pages(
    [
        Page("demo.py", "Home", "🏠"),
        Page("pages/1_nlp_llm.py", "NLP Tasks via LLM", "⚛️"),
        Page("pages/2_nlp_spacy.py", "NLP Tasks via Spacy", "🧰"),
    ]
)

add_page_title()

demo_purpose = """<div style="text-align: justify;">
The purpose of the demo is to showcase the ways in which some of the common NLP tasks can be performed using various open source libraries.
The first section in the side bar is related to using <b> OpenAI </b> to perform entity recognition, topic classification etc.
The second section in the side bar is related to using <i> SpaCy</i> library to quickly perform various NLP tasks. 

</div>
"""

nlp_llm_text = """<div style="text-align: justify;">
One can use OpenAI models to perform certain NLP tasks such as entity recoginition, topic classification etc. However there are limitations to the
extent of NLP Analysis that can be performed via OpenAI models. One can enter any text and start with a default prompt for entity recognition. Subsequently
one can use prompt such as

- Identity PERSONS in the text
- Identify LOCATIONS in the text
- Identify Stock Symbols in the text
- How many entities can you recognize in the text ?
- Can you give relevance score for any entity
- Can you give confidence score for any entity
- Identify Topics in the text
- Identify Industries in the text
- Summarize the text in 10 lines

</div>
"""

nlp_llm_spacy = """
One can use <i> spaCy</i> library to perform common NLP tasks such as

- Tokenization
- Text Embedding
- Named Entity Recognition
- Dependency Parser and Named Entity recognition
- Vector Similarity

"""


st.header("Demo", divider="blue")
st.write(demo_purpose, unsafe_allow_html=True)
st.markdown("")
st.markdown("")


st.subheader("NLP Tasks via LLM", divider="red")
st.write(nlp_llm_text, unsafe_allow_html=True)
st.text("")

st.subheader("NLP Tasks via Spacy", divider="orange")
st.write(nlp_llm_spacy, unsafe_allow_html=True)
