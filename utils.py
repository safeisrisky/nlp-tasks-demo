import streamlit as st
import hmac


def get_message(role, prompt):
    return {"role": role, "content": prompt}


def get_system_prompt():
    prompt = """
    Assume you are a Natural Language Processing engine that can perform Entity Recognition,
    Topic Classification, Sentiment Analysis, Summarization and related NLP tasks
    """
    return prompt


def get_companies_prompt():
    prompt = """
    You will have to perform entity recognition and report ONLY companies and organizations.

The response should be a json array. For each of the entity recognized,  the json should contain the following keys:
1. Name of the entity
2. Type of the entity
3. Domicile
4. Country of Incorporation
5. IsPublic

IsPublic field is a value that says whether the entity is public or private. For entities that you don't have any idea, you can populate Domicile, Country of Incorporation, IPublic as blanks.

Make sure that you are able to recognize all types companies and organizations, public or private.
 
The response should be a json array and make sure that the results are made available in JSON under the key data.
The following is the text input for which the above analysis has to be done 

INPUT TEXT:  \n
"""
    return prompt


def get_non_companies_prompt():
    prompt = """
    
    Please analyze the text for 'Person' type entities. For each of the entity recognized,  the json should contain the following keys:
1. Name of the entity
2. Type of the entity
 
The response should be a json array and make sure that the results are made available in JSON under the key data.


The following is the text input for which the above analysis has to be done 

INPUT TEXT:  \n
"""
    return prompt


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Show input for password.
    pwd = st.empty()
    pwd.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        pwd.empty()
        return True

    if "password_correct" in st.session_state:
        st.error("Password incorrect")
    return False
